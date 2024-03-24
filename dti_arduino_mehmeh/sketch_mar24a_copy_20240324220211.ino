const int leftPlate1 = 2;
const int leftPlate2 = 3;
const int rightPlate1 = 4;
const int rightPlate2 = 5;

void setup() {
  Serial.begin(9600);
  pinMode(leftPlate1, INPUT);
  pinMode(leftPlate2, INPUT);
  pinMode(rightPlate1, INPUT);
  pinMode(rightPlate2, INPUT);
}

void loop() {
  if(digitalRead(leftPlate1))
    Serial.println("A");
  else if(digitalRead(leftPlate2))
    Serial.println("C");
  else if(digitalRead(rightPlate1))
    Serial.println("B");
  else if(digitalRead(rightPlate2))
    Serial.println("D");
  else
    Serial.println("NIL");
  delay(500); // for connecting with python
  Serial.flush(); // For connecting with python
}
