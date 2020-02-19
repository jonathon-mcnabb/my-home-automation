#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid =  "FBI Surveillance Van";
const char* password = "44651268";

char r = 0x00;
char g = 0xff;
char b = 0x00;

void setup()
{
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
}


void loop()
{

    const uint16_t port = 5577;
    const char* host = "192.168.0.193";  //Change to whatever your LED Controller IP is
    
    WiFiClient client;

    if (client.connect(host, port)) //Try to connect to TCP Server
     {
        Serial.print("Connected to LED light... : ");
        //Serial.println(brightness);
          char command[] = {0x41, r, g, b, 0x00, 0xf0, 0x0f, '?' };
          delay(10);
          g--;
          uint16_t sum;
          for(int i=0;i<7;i++){
            sum += command[i];
          }
          uint8_t checksum = sum & 0x00ff;
          Serial.println(checksum);

          command[7] = checksum;
          
          client.write((uint8_t *)command, sizeof(command));
          delay(50); 
     }

}
