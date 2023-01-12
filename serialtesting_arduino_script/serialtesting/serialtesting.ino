
String serialData = "";      // a String to hold incoming data
String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete
unsigned long int start_time=millis(); //start time of program
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  // reserve 200 bytes for the inputString:
  serialData.reserve(200);
}

void loop() {
  if (stringComplete){
    Serial.println("rec: "+inputString);
    inputString="";
    stringComplete=false;}
  else
    send_data(); 
}


void serialEvent() {
  //delay(3000);
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
    // add it to the inputString:
    inputString += inChar;
  }
}
void send_data(){
  //delay(1000);
  if (Serial.availableForWrite()){
    while (millis() > start_time + 15000){
      start_time=millis();
      int runtime =start_time/1000;
      Serial.println(runtime);
    } 
  } 
}