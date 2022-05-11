#include <Wire.h>

const int ledPin = 13; // onboard LED
static_assert(LOW == 0, "Expecting LOW to be 0");

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
   Wire.begin(0x8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // turn it off
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue0 = analogRead(A0);
  int sensorValue1 = analogRead(A1);
  int sensorValue2 = analogRead(A2);
  int sensorValue3 = analogRead(A3);
  int sensorValue4 = analogRead(A4);
  int sensorValue5 = analogRead(A5);
  String sensor1 = "One ";
  String Sens1 = sensor1 + sensorValue0;
  String sensor2 = "Two ";
  String Sens2 = sensor2 + sensorValue1;
  String sensor3 = "Three ";
  String Sens3 = sensor3 + sensorValue2;
  String sensor4 = "Four ";
  String Sens4 = sensor4 + sensorValue3;
  String sensor5 = "Five ";
  String Sens5 = sensor5 + sensorValue4;
  String sensor6 = "Six ";
  String Sens6 = sensor6 + sensorValue5;
  
  // print out the value you read:
  
  Serial.println(Sens1);
  delay(1000);
  Serial.println(Sens2);
  delay(1000);
  Serial.println(Sens3);
  delay(1000);
  Serial.println(Sens4);
  delay(1000);
  Serial.println(Sens5);
  delay(1000);
  Serial.println(Sens6);
  delay(1000);        // delay in between reads for stability
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(ledPin, c);
  }
}
