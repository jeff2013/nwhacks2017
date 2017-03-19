#include <Stepper.h>
#include <stdio.h>

int in1Pin = 2;
int in2Pin = 3;
int in3Pin = 4;
int in4Pin = 5;

int currentStep = 0;

int toggleMovementPin = 0;
int resetPin = 1;
int toggleMovementPinVal = 0;

bool pouring = true; 
long counter = 0;

//Speed of the pour
//use 10 for the initial movement, 20 or 30 for the fine pour
int pourSpeed = 10;

int incomingByte = 0;

void setup() {
  
  // put your setup code here, to run once:
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);

  //trigger code

  
  Serial.begin(9600);
}

void loop() {
  
  toggleMovementPinVal = analogRead(toggleMovementPin);
  if(analogRead(resetPin) == 1023){
    pouring = false;
  }
  if(Serial.available() >0){
    incomingByte = Serial.read();
    Serial.print("I recieved: ");
    Serial.println(incomingByte, DEC);
  }
  //!pouring
  //analogRead(resetPin) == 1023
  if(!pouring && counter >0){
    int directionStep = pouring?currentStep:(4-1)-currentStep;
    switch(directionStep){
      case 0:
        digitalWrite(in1Pin, HIGH);
        digitalWrite(in2Pin, LOW);
        digitalWrite(in3Pin, LOW);
        digitalWrite(in4Pin, LOW);
        break;
      case 1:
        digitalWrite(in1Pin, LOW);
        digitalWrite(in2Pin, HIGH);
        digitalWrite(in3Pin, LOW);
        digitalWrite(in4Pin, LOW);
        break;
      case 2:
        digitalWrite(in1Pin, LOW);
        digitalWrite(in2Pin, LOW);
        digitalWrite(in3Pin, HIGH);
        digitalWrite(in4Pin, LOW);
        break;
      case 3:
        digitalWrite(in1Pin, LOW);
        digitalWrite(in2Pin, LOW);
        digitalWrite(in3Pin, LOW);
        digitalWrite(in4Pin, HIGH); 
        break;
      }
      currentStep = (++currentStep<4)? currentStep:0;
      delay(10);
      counter--;
      if(counter == 0){
        pouring = true;
      }
  }else{
    if(toggleMovementPinVal == 1023 && counter < 530){
     int directionStep = pouring?currentStep:(4-1)-currentStep;
      switch(directionStep){
        case 0: 
          digitalWrite(in1Pin, HIGH);
          digitalWrite(in2Pin, LOW);
          digitalWrite(in3Pin, LOW);
          digitalWrite(in4Pin, LOW);
          break;
        case 1:
          digitalWrite(in1Pin, LOW);
          digitalWrite(in2Pin, HIGH);
          digitalWrite(in3Pin, LOW);
          digitalWrite(in4Pin, LOW);
          break;
        case 2:
          digitalWrite(in1Pin, LOW);
          digitalWrite(in2Pin, LOW);
          digitalWrite(in3Pin, HIGH);
          digitalWrite(in4Pin, LOW);
          break;
        case 3:
          digitalWrite(in1Pin, LOW);
          digitalWrite(in2Pin, LOW);
          digitalWrite(in3Pin, LOW);
          digitalWrite(in4Pin, HIGH); 
          break;
      }
      currentStep = (++currentStep<4)? currentStep:0;
      pourSpeed = (counter > 350 && pouring)? 30 : 10;
      delay(pourSpeed);
      counter++;
    }else{
    }
  }
  
}
 
