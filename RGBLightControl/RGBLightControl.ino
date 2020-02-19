#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

// wifi login information
const char* ssid =  "FBI Surveillance Van";
const char* password = "44651268";

// intial rgb values
char r = 0x00;
char g = 0xff;
char b = 0x00;

void setup()
{
  Serial.begin(115200);
  Serial.println();

  // attempt to connect to WiFi
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

    // port and IP of LED light
    const uint16_t port = 5577;
    const char* host = "192.168.0.193";  //Change to whatever your LED Controller IP is
    
    WiFiClient client;

    if (client.connect(host, port)) //Try to connect to Server
     {
        Serial.print("Connected to LED light... : ");
        //Serial.println(brightness);
          // The following format is for sending RGB values
          char command[] = {0x41, r, g, b, 0x00, 0xf0, 0x0f, '?' };
          delay(10);
          g--;
          uint16_t sum;
          for(int i=0;i<7;i++){
            // compute a check sum
            sum += command[i];
          }

          // set the checksum
          uint8_t checksum = sum & 0x00ff;
          Serial.println(checksum);
  
          command[7] = checksum;
          
          client.write((uint8_t *)command, sizeof(command));
          delay(50); 
     }

}
