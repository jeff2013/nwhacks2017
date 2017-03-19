#include <stdio.h>
#define BUTTON_ON 1023
#define BUTTON_OFF 0
#define COUNTER_MAX 530
#define COUNTER_MIN 0
#define SERVO_PIN1 2
#define SERVO_PIN2 3
#define SERVO_PIN3 4
#define SERVO_PIN4 5
#define MOVE_PIN 0
#define RESET_PIN 0
#define SAD_BYTE 49
#define HAPPY_BYTE 50

int currentStep = 0;
int counter = 0;


void setup() {
  // Set our pins
  pinMode(SERVO_PIN1, OUTPUT);
  pinMode(SERVO_PIN2, OUTPUT);
  pinMode(SERVO_PIN3, OUTPUT);
  pinMode(SERVO_PIN4, OUTPUT);
  // Cycle motor
  digitalWrite(SERVO_PIN1, LOW);
  digitalWrite(SERVO_PIN2, LOW);
  digitalWrite(SERVO_PIN3, LOW);
  digitalWrite(SERVO_PIN4, LOW);
  
  Serial.begin(9600);
}

void cycleMotor(int phase) {
  switch(phase) {
        case 0: 
          digitalWrite(SERVO_PIN1, HIGH);
          digitalWrite(SERVO_PIN2, LOW);
          digitalWrite(SERVO_PIN3, LOW);
          digitalWrite(SERVO_PIN4, LOW);
          break;
        case 1:
          digitalWrite(SERVO_PIN1, LOW);
          digitalWrite(SERVO_PIN2, HIGH);
          digitalWrite(SERVO_PIN3, LOW);
          digitalWrite(SERVO_PIN4, LOW);
          break;
        case 2:
          digitalWrite(SERVO_PIN1, LOW);
          digitalWrite(SERVO_PIN2, LOW);
          digitalWrite(SERVO_PIN3, HIGH);
          digitalWrite(SERVO_PIN4, LOW);
          break;
        case 3:
          digitalWrite(SERVO_PIN1, LOW);
          digitalWrite(SERVO_PIN2, LOW);
          digitalWrite(SERVO_PIN3, LOW);
          digitalWrite(SERVO_PIN4, HIGH); 
          break;
  }
}

void pour() {
  if(counter < COUNTER_MAX) {
    cycleMotor(currentStep);
    currentStep = (currentStep+1) % 4;
    int pourSpeed = (counter > 350)? 30 : 10;      
    delay(pourSpeed);
    counter++;
  }
}

void reset() {
  if(counter > COUNTER_MIN) {
      cycleMotor(3 - currentStep);
      currentStep = (currentStep + 1) % 4;
      delay(10);
      counter--;
  }
}

void loop() {
  if(analogRead(RESET_PIN) == BUTTON_ON) {
    reset();
  } else if(analogRead(MOVE_PIN) == BUTTON_ON) {
      pour();
  } else if(Serial.available() > 0) {
    char incomingByte = Serial.read();
    if(incomingByte == SAD_BYTE) {
      pour();
    } else if(incomingByte == HAPPY_BYTE) {
      reset();
    }
  }
}
