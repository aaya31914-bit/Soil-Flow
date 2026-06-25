//  PINS 
const int soilPin = A0;
const int tdsPin = A1;
const int pumpPin = 7;

//  THRESHOLDS 
int moistureThreshold = 35;
int tdsThreshold = 800;

void setup() {
  Serial.begin(9600);

  pinMode(pumpPin, OUTPUT);
  digitalWrite(pumpPin, LOW);
}

void loop() {
  //  average reading (10 samples taken)
  long sumTDS = 0;
  for(int i=0; i<10; i++) {
    sumTDS += analogRead(tdsPin);
    delay(10); // small delay between samples 
  }
  int tdsValue = sumTDS / 10; // average

  int soilValue = analogRead(soilPin);

  // convert
  float moisture = map(soilValue, 1023, 0, 0, 100);
  float tds = map(tdsValue, 0, 1023, 0, 1500);

  // send data ( more stable )
  Serial.print(moisture);
  Serial.print(",");
  Serial.println(tds);
  
 
  // ======  control pump ======
  if (moisture < moistureThreshold || tds > tdsThreshold) {
    digitalWrite(pumpPin, HIGH);  // turn on pump
  } else {
    digitalWrite(pumpPin, LOW);   // turn off pump
  }

  delay(2000);
}