#include "TimerOne.h"

int pin1 = 4;
int pin2 = 5;
int pin3 = 6;
int pin4 = 7;

unsigned long interval;
int i;
int sum;
int incomingbyte = 0;

int flag = 0;
int forflag = 0;
int duration;
int temp1;
int temp2;

int limit = 30;
int wait_interval = 20 * 1000;

int duration1 = 24 * 1000;
int duration2 = 8 * 1000;
int duration3 = 3 * 1000;
int duration4 = 2 * 1000;
int duration5 = 1 * 1000;
int duration6 = 1 * 1000;

// 1 = 3; 2 = 10; 3 = 30; 4 = 50; 5 = 100; 6 = 200
int shuffle_speed[] = {
  5, 3, 4, 2, 1, 6,
  2, 6, 3, 1, 5, 4, 
  1 , 6, 3, 5, 2, 4,
  5, 2, 6, 4, 3, 1, 
  1, 3 , 2, 5, 6, 4
};


void setup() {
  Serial.begin(9600);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);

  interval = 25000; //25ms
  Timer1.initialize(interval);

  /*
    Timer1.attachInterrupt(pulse_1);
    delay (5000); // wait 5s
    Timer1.attachInterrupt(pulse_2);
    delay (5000); // wait 5s
    Timer1.attachInterrupt(pulse_3);
    delay (5000); // wait 5s
    Timer1.attachInterrupt(pulse_4);
    delay (5000); // wait 5s
    Timer1.attachInterrupt(pulse_5);
    delay (5000); // wait 5s
    Timer1.attachInterrupt(pulse_6);
    delay (5000); // wait 5s
  */
}

void loop() {
  //if (Serial.available() > 0) {

  for (int u = 0; u < limit; u++) {
    // Serial.println(u);
    if (forflag == 0) {
      Serial.print("trial: ");
      Serial.println(u + 1);
      //Serial.println(shuffle_speed[u]);
      if (shuffle_speed[u] == 1) {
        Serial.println("3mm/s");
        flag = 0;
        Timer1.attachInterrupt(pulse_1);
        //delay(duration1);
        delay(duration1);
        delay(wait_interval);
      }

      if (shuffle_speed[u] == 2) {
        Serial.println("10mm/s");
        flag = 0;
        Timer1.attachInterrupt(pulse_2);
        //delay(duration2);
        delay(duration2 + wait_interval);
      }

      if (shuffle_speed[u] == 3) {
        Serial.println("30mm/s");
        flag = 0;
        Timer1.attachInterrupt(pulse_3);
        //delay(duration3);
        delay(duration3 + wait_interval);
      }

      if (shuffle_speed[u] == 4) {
        Serial.println("50mm/s");
        flag = 0;
        Timer1.attachInterrupt(pulse_4);
        //delay(duration4);
        delay(duration4 + wait_interval);
      }

      if (shuffle_speed[u] == 5) {
        Serial.println("100mm/s");
        flag = 0;
        Timer1.attachInterrupt(pulse_5);
        //delay(duration5);
        delay(duration5 + wait_interval);
      }

      if (shuffle_speed[u] == 6) {
        Serial.println("200mm/s");
        flag = 0;
        Timer1.attachInterrupt(pulse_6);
        //delay(duration6);
        delay(duration6 + wait_interval);
      }
    }
    if (u == limit - 1) {
      forflag = 1;
      Serial.println("End");
    }
  }
  /*
    incomingbyte = Serial.read();
    if (incomingbyte == 49) {
      Serial.println("3mm/s");
      flag = 0;
      Timer1.attachInterrupt(pulse_1);
    }
    else if (incomingbyte == 50) {
      Serial.println("10mm/s");
      flag = 0;
      Timer1.attachInterrupt(pulse_2);
    }
    else if (incomingbyte == 51) {
      Serial.println("30mm/s");
      flag = 0;
      Timer1.attachInterrupt(pulse_3);
    }
    else if (incomingbyte == 52) {
      flag = 0;
      Serial.println("50mm/s");
      Timer1.attachInterrupt(pulse_4);
    }
    else if (incomingbyte == 53) {
      flag = 0;
      Serial.println("100mm/s");
      Timer1.attachInterrupt(pulse_5);
    }
    else if (incomingbyte == 54) {
      flag = 0;
      Serial.println("200mm/s");
      Timer1.attachInterrupt(pulse_6);
    }
  */
  //}
}
///////////////////////////////////////////////////
/* duration calculation
  v= 3mm/s
  72mm / 3mm/s = 24s
  t = 24s; /4(n tactors) = 6s;
  t = 6s = 6000ms;
  6000ms / 25ms = 240
*/
///////////////////////////////////////////////////
void pulse_1() {
  duration = 240; //para 3mm/s
  temp1 = duration;
  temp2 = 0;

  if (flag == 0) {

    ++sum;

    if (sum < duration + 1) {
      digitalWrite(pin1, !digitalRead(pin1));
    }
    temp2 = duration * 2;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin2, !digitalRead(pin2));
    }
    temp1 = temp2;
    temp2 = duration * 3;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin3, !digitalRead(pin3));
    }
    temp1 = temp2;
    temp2 = duration * 4;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin4, !digitalRead(pin4));
    }
    if (sum >= duration * 4) {
      sum = 0;
      flag = 1;
    }
  }
}
///////////////////////////////////////////////////
void pulse_2() {
  duration = 72; // para 10mm/s
  temp1 = duration;
  temp2 = 0;

  if (flag == 0) {

    ++sum;

    if (sum < duration + 1) {
      digitalWrite(pin1, !digitalRead(pin1));
    }
    temp2 = duration * 2;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin2, !digitalRead(pin2));
    }
    temp1 = temp2;
    temp2 = duration * 3;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin3, !digitalRead(pin3));
    }
    temp1 = temp2;
    temp2 = duration * 4;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin4, !digitalRead(pin4));
    }
    if (sum >= duration * 4) {
      sum = 0;
      flag = 1;
    }
  }
}

///////////////////////////////////////////////////
void pulse_3() {
  duration = 24; // para 30mm/s
  temp1 = duration;
  temp2 = 0;

  if (flag == 0) {

    ++sum;

    if (sum < duration + 1) {
      digitalWrite(pin1, !digitalRead(pin1));
    }
    temp2 = duration * 2;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin2, !digitalRead(pin2));
    }
    temp1 = temp2;
    temp2 = duration * 3;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin3, !digitalRead(pin3));
    }
    temp1 = temp2;
    temp2 = duration * 4;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin4, !digitalRead(pin4));
    }
    if (sum >= duration * 4) {
      sum = 0;
      flag = 1;
    }
  }
}
///////////////////////////////////////////////////
void pulse_4() {
  duration = 14; // para 50mm/s -- 14.4 ~ 14
  temp1 = duration;
  temp2 = 0;

  if (flag == 0) {

    ++sum;

    if (sum < duration + 1) {
      digitalWrite(pin1, !digitalRead(pin1));
    }
    temp2 = duration * 2;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin2, !digitalRead(pin2));
    }
    temp1 = temp2;
    temp2 = duration * 3;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin3, !digitalRead(pin3));
    }
    temp1 = temp2;
    temp2 = duration * 4;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin4, !digitalRead(pin4));
    }
    if (sum >= duration * 4) {
      sum = 0;
      flag = 1;
    }
  }
}
///////////////////////////////////////////////////
void pulse_5() {
  duration = 7; // para 100mm/s -- 7.2 ~ 7
  temp1 = duration;
  temp2 = 0;

  if (flag == 0) {

    ++sum;

    if (sum < duration) {
      digitalWrite(pin1, !digitalRead(pin1));
    }
    temp2 = (duration * 2) + 1;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin2, !digitalRead(pin2));
    }
    temp1 = temp2;
    temp2 = duration * 3;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin3, !digitalRead(pin3));
    }
    temp1 = temp2;
    temp2 = (duration * 4) + 1;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin4, !digitalRead(pin4));
    }
    if (sum >= duration * 4) {
      sum = 0;
      flag = 1;
    }
  }
}
///////////////////////////////////////////////////
void pulse_6() {
  duration = 4; // para 200mm/s -- 3.6 ~ 4
  temp1 = duration;
  temp2 = 0;

  if (flag == 0) {

    ++sum;

    if (sum < duration + 1) {
      digitalWrite(pin1, !digitalRead(pin1));
    }
    temp2 = duration * 2;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin2, !digitalRead(pin2));
    }
    temp1 = temp2;
    temp2 = duration * 3;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin3, !digitalRead(pin3));
    }
    temp1 = temp2;
    temp2 = duration * 4;
    if (sum >= temp1 && sum < temp2) {
      digitalWrite(pin4, !digitalRead(pin4));
    }
    if (sum >= duration * 4) {
      sum = 0;
      flag = 1;
    }
  }
}
