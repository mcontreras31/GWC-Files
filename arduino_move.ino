#include <Servo.h>

Servo Right;
Servo Left;

void setup(){
Left.attach(13);
Right.attach(12);
Left.writeMicroseconds(1500);
Right.writeMicroseconds(1500);
}

void Righty(){
Left.writeMicroseconds(1300);
}

void Lefty(){
Right.writeMicroseconds(1700);
}



void loop() {
  // put your main code here, to run repeatedly:
  Righty();
  delay(3000);
  Lefty();
  delay(3000);
  
}
