
String serialData = "";      // a String to hold incoming data

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  serialData.reserve(200);
}

void loop() {
  // put your main code here, to run repeatedly:
  //  if (Serial.available()>0){
  //    serialData=Serial.readString();
  //    }
  //  if(Serial.availableForWrite() && serialData!=""){
  //    int byteSent=Serial.write("Recieved: ");
  //    byteSent=Serial.print(serialData);

  if (Serial.availableForWrite()) {
    Serial.write("this is the arduino \n");
  }
  delay(3000);

}
