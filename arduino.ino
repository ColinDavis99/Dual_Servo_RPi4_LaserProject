// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

boolean enabled = true;
// the loop routine runs over and over again forever:
void loop() {

  //if (!enabled){
    //return; 
   //}
  
  //for (int i = 0; i < 5; i++) {
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
  delay(50);
  Serial.println(Sens2);
  delay(50);
  Serial.println(Sens3);
  delay(50);
  Serial.println(Sens4);
  delay(50);
  Serial.println(Sens5);
  delay(50);
  Serial.println(Sens6);
  delay(50);        // delay in between reads for stability
    
  }

  //enabled = false;
  
//}