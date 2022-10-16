
String serialData = "";      // a String to hold incoming data
String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  serialData.reserve(200);
}

void loop() {
  if (stringComplete){
    Serial.println("rec: "+inputString);
    inputString="";
    stringComplete=false;}  
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
