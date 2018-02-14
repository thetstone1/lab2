 
 void setup(){
  pinMode(3,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
   // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
}
 
int altitude = 0;
int magnitude = 0;

void loop(){
  while(Serial.available() == 0);
  char c = Serial.read();
  if (c == 'p'){
    altitude = analogRead(A5)/4;
    magnitude = analogRead(A4)/4; 
    Serial.print(altitude);
    Serial.print(',');
    Serial.println(magnitude);
  } 
  if (c == 'r'){
    analogWrite(3,255);
    analogWrite(5,0);
  }
  if (c == 'g'){
    analogWrite(3,0);
    analogWrite(5,255);    
  }
}
