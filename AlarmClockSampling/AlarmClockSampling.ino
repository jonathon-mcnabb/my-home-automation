#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#define CHANNEL_1   1
#define CHANNEL_2   2
#define CHANNEL_3   3
#define CHANNEL_4   4

#define PIN_1       1
#define PIN_2       3
#define PIN_3       15
#define PIN_4       13
#define PIN_5       12
#define PIN_6       14
#define PIN_7       2
#define PIN_8       0
#define PIN_9       4
#define PIN_10      5
#define PIN_11      16

uint8_t pinValues;

uint8_t channelOneValue;
uint8_t channelTwoValue;
uint8_t channelThreeValue;
uint8_t channelFourValue;

uint8_t chanOneDisplay = 8;
uint8_t chanTwoDisplay = 8;
uint8_t chanThreeDisplay = 8;
uint8_t chanFourDisplay = 8;

bool isPM;
bool alarmIsOn;

const char* ssid =  "FBI Surveillance Van";
const char* password = "44651268";

WiFiUDP Udp;

char myArray[] = {'A', 0x00, 0xff, 0x00, 0x00, 0xf0, 0x0f, '?' };

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  Serial.end();
  
  pinMode(PIN_1,  INPUT);
  pinMode(PIN_2,  INPUT);
  pinMode(PIN_3,  INPUT);
  pinMode(PIN_4,  INPUT);
  pinMode(PIN_5,  INPUT);
  pinMode(PIN_6,  INPUT);
  pinMode(PIN_7,  INPUT);
  pinMode(PIN_8,  INPUT);
  pinMode(PIN_9,  INPUT);
  pinMode(PIN_10, INPUT);
  pinMode(PIN_11, INPUT);

  // attach interrupts for each channel
  attachInterrupt(digitalPinToInterrupt(PIN_1), channelOneInterrupt, RISING);
  attachInterrupt(digitalPinToInterrupt(PIN_2), channelTwoInterrupt, RISING);
  attachInterrupt(digitalPinToInterrupt(PIN_3), channelThreeInterrupt, RISING);
  attachInterrupt(digitalPinToInterrupt(PIN_4), channelFourInterrupt, RISING);

}

ICACHE_RAM_ATTR void channelOneInterrupt() {
  // Pin 1 just rose. So we know channel 1 is displaying. We now need to sample pins 5-11
  samplePins();
  computeData(CHANNEL_1);
}

ICACHE_RAM_ATTR void channelTwoInterrupt() {
  samplePins();
  computeData(CHANNEL_2);
}

ICACHE_RAM_ATTR void channelThreeInterrupt() {
  samplePins();
  computeData(CHANNEL_3);
}

ICACHE_RAM_ATTR void channelFourInterrupt() {
  samplePins();
  computeFourData(CHANNEL_4);
}

void samplePins() {
  pinValues = 0;
  pinValues =  pinValues  | (digitalRead(PIN_5) << 0);
  pinValues =  pinValues  | (digitalRead(PIN_6) << 1);
  pinValues =  pinValues  | (digitalRead(PIN_6) << 2);
  pinValues =  pinValues  | (digitalRead(PIN_6) << 3);
  pinValues =  pinValues  | (digitalRead(PIN_6) << 4);
  pinValues =  pinValues  | (digitalRead(PIN_6) << 5);
  pinValues =  pinValues  | (digitalRead(PIN_6) << 6);
}

void computeData(int currentChannel) {
  int temp;
  if(pinValues = 0b01000000) {
    // 0
    temp = 0;
  } else if(pinValues = 0b01111001) {
    // 1
    temp = 1;
  } else if(pinValues = 0b00100100) {
    // 2
    temp = 2;
  } else if(pinValues = 0b00110000) {
    // 3
    temp = 3;
  } else if(pinValues = 0b00011001) {
    // 4
    temp = 4;
  } else if(pinValues = 0b00010010) {
    // 5
    temp = 5;
  } else if(pinValues = 0b00000010) {
    // 6
    temp = 6;
  } else if(pinValues = 0b01111000) {
    // 7
    temp = 7;
  } else if(pinValues = 0b00000000) {
    // 8
    temp = 8;
  } else if(pinValues = 0b00011000) {
    // 9
    temp = 9;
  }

  switch (currentChannel) {
    case CHANNEL_1:
      // statements
      channelOneValue = temp;
      break;
    case CHANNEL_2:
      // statements
      channelTwoValue = temp;
      break;
    case CHANNEL_3:
      // statements
      channelThreeValue = temp;
      break;
  }

  
}

void computeFourData(int currentChannel) {
  int temp = 0b00000110;
  pinValues = pinValues & temp;

  if(pinValues = 0b00000000) {
    // if the 1 is on
    channelFourValue = 1;
  } else {
    channelFourValue = 0;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  // only needs to display time value if it changes
  if(channelOneValue != chanOneDisplay) {
    // value has been updated
    chanOneDisplay = channelOneValue;
  }

  if(channelTwoValue != chanTwoDisplay) {
    // value has been updated
    chanTwoDisplay = channelTwoValue;
  }

  if(channelThreeValue != chanThreeDisplay) {
    // value has been updated
    chanThreeDisplay = channelThreeValue;
  }

  if(channelFourValue != chanFourDisplay) {
    // value has been updated
    chanFourDisplay = channelFourValue;
  }


  Udp.beginPacket("192.168.0.150", 8090);
  Udp.write(myArray, 8);
  Udp.endPacket();
  delay(30);
  
}
