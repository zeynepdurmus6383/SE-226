int LED1pin = 43;
int LED2pin = 44;
int LED3pin = 45;
int LED4pin = 46;
int button1pin = 38;
int button2pin = 39;
int counter=0;

byte lastButton1State=LOW;
byte lastButton2State=LOW;
byte ledState= LOW;
int systemBoolean = 0;


void setup() {
pinMode(LED1pin, OUTPUT);
pinMode(LED2pin, OUTPUT);
pinMode(LED3pin, OUTPUT);
pinMode(LED4pin, OUTPUT);
pinMode(button1pin, INPUT);
pinMode(button2pin, INPUT);
}
void allLedsOff() {
  digitalWrite(LED1pin, LOW);
  digitalWrite(LED2pin, LOW);
  digitalWrite(LED3pin, LOW);
  digitalWrite(LED4pin, LOW);
}
void mode1(){
  digitalWrite(LED1pin,HIGH);
  digitalWrite(LED2pin,HIGH);
  digitalWrite(LED3pin,HIGH);
  digitalWrite(LED4pin,HIGH);
  delay(1000);
  digitalWrite(LED1pin,LOW);
  digitalWrite(LED2pin,LOW);
  digitalWrite(LED3pin,LOW);
  digitalWrite(LED4pin,LOW);
  delay(1000);
}

void mode2(){
  digitalWrite(LED1pin,LOW);
  digitalWrite(LED4pin,HIGH);
  delay(1000);
  digitalWrite(LED4pin,LOW);
  digitalWrite(LED3pin,HIGH);
  delay(1000);
  digitalWrite(LED3pin,LOW);
  digitalWrite(LED2pin,HIGH);
  delay(1000);
  digitalWrite(LED2pin,LOW);
  digitalWrite(LED1pin,HIGH);
  delay(1000);
}

void mode3(){
  digitalWrite(LED4pin,LOW);
  digitalWrite(LED1pin,HIGH);
  delay(1000);
  digitalWrite(LED1pin,LOW);
  digitalWrite(LED2pin,HIGH);
  delay(1000);
  digitalWrite(LED2pin,LOW);
  digitalWrite(LED3pin,HIGH);
  delay(1000);
  digitalWrite(LED3pin,LOW);
  digitalWrite(LED4pin,HIGH);
  delay(1000);
}

void loop() {
  byte button1State = digitalRead(button1pin);
  byte button2State = digitalRead(button2pin);

  if(button1State != lastButton1State){
    lastButton1State = button1State;
    if(button1State == HIGH){ // Butona basıldığında (Bağlantınıza göre LOW da yapılabilir)
      if(systemBoolean == 0){
        systemBoolean = 1;
        counter = 1; // Sistem açıldığında 1. moddan başlasın
      } else {
        systemBoolean = 0;
        counter = 0;
        allLedsOff(); 
      }
       
    }
  }
  if(button2State != lastButton2State){
    lastButton2State = button2State;
    if(systemBoolean == 1 && button2State == LOW){ 
      counter++;
      if(counter == 4) counter = 1;
      
    }
  }

  if(systemBoolean == 1) {
    switch(counter){
      case 1:
        mode1();
        break;
      case 2:
        mode2();
        break;
      case 3:
        mode3();
        break;
    }  
  }
}

