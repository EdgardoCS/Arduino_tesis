#include "TimerOne.h"

int pin1 = 4;
int pin2 = 5;
int pin3 = 6;
int pin4 = 7;

unsigned long interval;
int i;
int sum;
int incomingbyte = 0;

int duration;
int temp1;
int temp2;

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
  if (Serial.available() > 0) {
    incomingbyte = Serial.read();
    if (incomingbyte == 49) {
      Serial.println("uno");
      Timer1.attachInterrupt(pulse_1);
    }
    else if (incomingbyte == 50) {
      Serial.println("dos");
      Timer1.attachInterrupt(pulse_2);
    }
    else if (incomingbyte == 51) {
      Serial.println("tres");
      Timer1.attachInterrupt(pulse_3);
    }
    else if (incomingbyte == 52) {
      Serial.println("cuatro");
      Timer1.attachInterrupt(pulse_4);
    }
    else if (incomingbyte == 53) {
      Serial.println("cinco");
      Timer1.attachInterrupt(pulse_5);
    }
    else if (incomingbyte == 54) {
      Serial.println("seis");
      Timer1.attachInterrupt(pulse_6);
    }
  }
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
}
///////////////////////////////////////////////////
void pulse_2() {
  duration = 72; // para 10mm/s
  temp1 = duration;
  temp2 = 0;

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
}

///////////////////////////////////////////////////
void pulse_3() {
  duration = 24; // para 30mm/s
  temp1 = duration;
  temp2 = 0;

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
}
///////////////////////////////////////////////////
void pulse_4() {
  duration = 14; // para 50mm/s -- 14.4 ~ 14
  temp1 = duration;
  temp2 = 0;

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
}
///////////////////////////////////////////////////
void pulse_5() {
  duration = 7; // para 100mm/s -- 7.2 ~ 7
  temp1 = duration;
  temp2 = 0;

  ++sum;

  if (sum < duration) {
    digitalWrite(pin1, !digitalRead(pin1));
  }
  temp2 = (duration * 2)+1;
  if (sum >= temp1 && sum < temp2) {
    digitalWrite(pin2, !digitalRead(pin2));
  }
  temp1 = temp2;
  temp2 = duration * 3;
  if (sum >= temp1 && sum < temp2) {
    digitalWrite(pin3, !digitalRead(pin3));
  }
  temp1 = temp2;
  temp2 = (duration * 4)+1;
  if (sum >= temp1 && sum < temp2) {
    digitalWrite(pin4, !digitalRead(pin4));
  }
}
///////////////////////////////////////////////////
void pulse_6() {
  duration = 4; // para 200mm/s -- 3.6 ~ 4
  temp1 = duration;
  temp2 = 0;

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
}
