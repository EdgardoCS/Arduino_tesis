import os
import math
import time
import serial
import numpy as np
from array import array


def distance(x, y):
    """
    Pythagorean theorem
    """
    return math.sqrt(x * x + y * y)


def brush(serial_port, x_dest, speed):
    y_dest = 0
    v_i = 0
    v_f = 0

    f_curr_x = 0
    f_curr_y = 0

    delta_x_inches = x_dest - f_curr_x
    delta_y_inches = y_dest - f_curr_y

    # Velocity inputs; clarify units.
    vi_inches_per_sec = v_i
    vf_inches_per_sec = v_f

    # Distance in inches that the motor+belt must turn through at Motor 1 and 2
    motor_dist1 = delta_x_inches + delta_y_inches
    motor_dist2 = delta_x_inches - delta_y_inches

    # Look at distance to move along 45-degree axes, for native motor steps:
    # Recall that StepScaleFactor gives a scaling factor for converting from inches to steps. It is *not* the native resolution
    # StepScaleFactor is Either 1016 or 2032, for 8X or 16X microstepping, respectively.

    # resolution = 1 # 16x microstepping
    resolution = 2  # 8x microstepping
    # print('Using resolution value of', resolution)

    if resolution == 2:
        StepScaleFactor = 1016.0
    else:
        StepScaleFactor = 1016.0 * 2  # Value from variable NativeResFactor in axidraw_conf.py

    # Round the requested motion to the nearest motor step.
    motor_steps1 = int(round(StepScaleFactor * motor_dist1))
    motor_steps2 = int(round(StepScaleFactor * motor_dist2))

    # Since we are rounding, we need to keep track of the actual distance moved,
    # not just the _requested_ distance to move.

    motor_dist1_rounded = float(motor_steps1) / (2.0 * StepScaleFactor)
    motor_dist2_rounded = float(motor_steps2) / (2.0 * StepScaleFactor)

    # Convert back to find the actual X & Y distances that will be moved:
    delta_x_inches_rounded = (motor_dist1_rounded + motor_dist2_rounded)
    delta_y_inches_rounded = (motor_dist1_rounded - motor_dist2_rounded)

    # If total movement is less than one step, skip this movement.
    if abs(motor_steps1) < 1 and abs(motor_steps2) < 1:
        print('Total movement less than one step, skipping this movement')

    segment_length_inches = distance(delta_x_inches_rounded, delta_y_inches_rounded)

    # From axidraw_conf
    # PenUpSpeed = 100        # Default pen-up speed (%).   Range: 1 - 110 %
    # PenDownSpeed = 100      #25 # Default pen-down speed (%). Range: 1 - 110 %

    PenUpSpeed = 72
    PenDownSpeed = 25

    SpeedLimXY_LR = 12
    # SpeedLimXY_LR = 3  #12.000 # Maximum XY speed allowed when in Low Resolution
    #                            # mode, in inches per second. Default: 12.000 Max:
    #                            # 17.3958
    # SpeedLimXY_HR = 1
    # SpeedLimXY_HR = 8.6979  #8.6979 # Maximum XY speed allowed when in High Resolution
    #                                 # mode, in inches per second. Default: 8.6979, Max:
    #                                 # 8.6979 Do not increase these values above Max;
    #                                 # they are derived from MaxStepRate and the
    #                                 # resolution.
    # SpeedLimXY_LR = speed
    # SpeedLimXY_HR = speed
    # Acceleration & Deceleration rates:

    # AccelRate = 100.0
    AccelRate = 40.0  # 40.0  # Standard acceleration rate, inches per second squared
    AccelRatePU = 60.0  # Pen-up acceleration rate, inches per second squared

    accel = 100  # 50    # Acceleration rate factor (1-100)
    TimeSlice = 0.025  # Interval, in seconds, of when to update the
    # motors. Default: TimeSlice = 0.025 (25 ms)
    MaxStepRate = 24.995  # Maximum allowed motor step rate, in steps per millisecond.
    # Note that 25 kHz is the absolute maximum step rate for the EBB.
    # Movement commands faster than this are ignored; may result in a crash (loss of position control).
    # We use a conservative value, to help prevent errors due to rounding.
    # This value is normally used _for speed limit checking only_.

    speed_pendown = PenDownSpeed * SpeedLimXY_LR / 110.0  # Speed given as
    # maximum inches/second
    # in XY plane
    speed_penup = PenUpSpeed * SpeedLimXY_LR / 110.0  # Speed given as
    # maximum
    # inches/second in XY
    # plane

    # Note: The value of `accel`, in the Inkscape extension, depends ot the
    # timing parameter "Acceleration"

    # <param indent="1" name="accelFactor" type="optiongroup"
    # appearance="minimal" _gui-text="Acceleration :">
    # <_option value="50">Standard</_option>
    # <_option value="100">Maximum</_option>
    # <_option value="75">High</_option>
    # <_option value="35">Slow</_option>
    # <_option value="10">Very slow</_option>
    # </param>

    pen_up = False
    if pen_up:
        speed_limit = speed_penup
    else:
        speed_limit = speed_pendown

    # Acceleration/deceleration rates:
    if pen_up:
        accel_rate = AccelRatePU * accel / 10
        0.0
    else:
        accel_rate = AccelRate * accel / 100.0

    # Maximum acceleration time: Time needed to accelerate from full stop to
    # maximum speed: v = a * t, so t_max = vMax / a
    t_max = speed_limit / accel_rate

    # Distance that is required to reach full speed, from zero speed:  x = 1/2 a t^2
    accel_dist = 0.5 * accel_rate * t_max * t_max

    if vi_inches_per_sec > speed_limit:
        vi_inches_per_sec = speed_limit
    if vf_inches_per_sec > speed_limit:
        vf_inches_per_sec = speed_limit

    # Times to reach maximum speed, from our initial velocity
    # vMax = vi + a*t  =>  t = (vMax - vi)/a
    # vf = vMax - a*t   =>  t = -(vf - vMax)/a = (vMax - vf)/a
    # -- These are _maximum_ values. We often do not have enough time/space to reach full speed.

    t_accel_max = (speed_limit - vi_inches_per_sec) / accel_rate
    t_decel_max = (speed_limit - vf_inches_per_sec) / accel_rate
    # Distance that is required to reach full speed, from our start at speed vi_inches_per_sec:
    # distance = vi * t + (1/2) a t^2
    accel_dist_max = (vi_inches_per_sec * t_accel_max) + (0.5 * accel_rate * t_accel_max * t_accel_max)
    # Use the same model for deceleration distance; modeling it with backwards motion:
    decel_dist_max = (vf_inches_per_sec * t_decel_max) + (0.5 * accel_rate * t_decel_max * t_decel_max)

    # time slices: Slice travel into intervals that are (say) 30 ms long.
    time_slice = TimeSlice  # Default slice intervals

    # Declare arrays: These are _normally_ 4-byte integers, but could
    # (theoretically) be 2-byte integers on some systems.  if so, this could
    # cause errors in rare cases (very large/long moves, etc.).  Set up an
    # alert system, just in case!

    duration_array = array('I')  # unsigned integer for duration -- up to
    # 65 seconds for a move if only 2 bytes.
    dist_array = array('f')  # float
    dest_array1 = array('i')  # signed integer
    dest_array2 = array('i')  # signed integer

    time_elapsed = 0.0
    position = 0.0
    velocity = vi_inches_per_sec
    speed_max = speed_limit  # We will reach _full cruising speed_!

    intervals = int(math.floor(t_accel_max / time_slice))  # Number of intervals during acceleration

    # If intervals == 0, then we are already at (or nearly at) full speed.
    if intervals > 0:
        time_per_interval = t_accel_max / intervals

        velocity_step_size = (speed_max - vi_inches_per_sec) / (intervals + 1.0)
        # For six time intervals of acceleration, first interval is at velocity (max/7)
        # 6th (last) time interval is at 6*max/7
        # after this interval, we are at full speed.

        for index in range(0, intervals):  # Calculate acceleration phase
            velocity += velocity_step_size
            time_elapsed += time_per_interval
            position += velocity * time_per_interval
            duration_array.append(int(round(time_elapsed * 1000.0)))
            dist_array.append(position)  # Estimated distance along direction of travel

            # Add a center "coasting" speed interval IF there is time for it.
        coasting_distance = segment_length_inches - (accel_dist_max + decel_dist_max)

        if coasting_distance > (time_slice * speed_max):
            # There is enough time for (at least) one interval at full cruising speed.
            velocity = speed  # speed_max
            cruising_time = coasting_distance / velocity
            time_elapsed += cruising_time
            duration_array.append(int(round(time_elapsed * 1000.0)))
            position += velocity * cruising_time
            dist_array.append(position)  # Estimated distance along direction of travel

        # Number of intervals during deceleration
        intervals = int(math.floor(t_decel_max / time_slice))

        time_per_interval = t_decel_max / intervals
        velocity_step_size = (speed_max - vf_inches_per_sec) / (intervals + 1.0)

        for index in range(0, intervals):  # Calculate deceleration phase
            velocity -= velocity_step_size
            time_elapsed += time_per_interval
            position += velocity * time_per_interval
            duration_array.append(int(round(time_elapsed * 1000.0)))
            dist_array.append(position)  # Estimated distance along direction of travel
        """
        The time & distance motion arrays for this path segment are now computed.
        Next: We scale to the correct intended travel distance,
        round into integer motor steps and manage the process
        of sending the output commands to the motors.
        """
        for index in range(0, len(dist_array)):
            # Scale our trajectory to the "actual" travel distance that we need:
            # Fractional position along the intended path
            fractional_distance = dist_array[index] / position
            dest_array1.append(int(round(fractional_distance * motor_steps1)))
            dest_array2.append(int(round(fractional_distance * motor_steps2)))

        sum(dest_array1)
        prev_motor1 = 0
        prev_motor2 = 0
        prev_time = 0

        for index in range(0, len(dest_array1)):
            move_steps1 = dest_array1[index] - prev_motor1
            move_steps2 = dest_array2[index] - prev_motor2
            move_time = duration_array[index] - prev_time
            prev_time = duration_array[index]

            if move_time < 1:
                move_time = 1  # don't allow zero-time moves.

            if abs(float(move_steps1) / float(move_time)) < 0.002:
                move_steps1 = 0  # don't allow too-slow movements of this axis
            if abs(float(move_steps2) / float(move_time)) < 0.002:
                move_steps2 = 0  # don't allow too-slow movements of this axis

            # Don't allow too fast movements of either axis: Catch rounding errors
            # that could cause an overspeed event
            while ((abs(float(move_steps1) / float(move_time)) >= MaxStepRate)
                   or (abs(float(move_steps2) / float(move_time)) >= MaxStepRate)):
                move_time += 1

            prev_motor1 += move_steps1
            prev_motor2 += move_steps2

            if move_steps1 != 0 or move_steps2 != 0:  # if at least one motor step
                # is required for this move.

                motor_dist1_temp = float(move_steps1) / (StepScaleFactor * 2.0)
                motor_dist2_temp = float(move_steps2) / (StepScaleFactor * 2.0)

                # Convert back to find the actual X & Y distances that will be moved:
                # X Distance moved in this subsegment, in inchse
                x_delta = (motor_dist1_temp + motor_dist2_temp)
                # Y Distance moved in this subsegment,
                y_delta = (motor_dist1_temp - motor_dist2_temp)

                f_new_x = f_curr_x + x_delta
                f_new_y = f_curr_y + y_delta

                # print('Command:', move_steps2, move_steps1, move_time)

                doXYMove(serial_port, move_steps2, move_steps1, move_time)
                if move_time > 50:
                    # print('sleep time', float(move_time - 10) / 1000.0)
                    time.sleep(float(move_time - 10) / 1000.0)  # pause before issuing next command

                f_curr_x = f_new_x  # Update current position
                f_curr_y = f_new_y
