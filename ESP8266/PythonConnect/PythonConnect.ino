#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid =  "FBI Surveillance Van";
const char* password = "44651268";

WiFiUDP Udp;
// unsigned int localUdpPort = 8090;  // local port to listen on



char myArray[] = {'A', 0x00, 0xff, 0x00, 0x00, 0xf0, 0x0f, '?' };

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

  //Udp.begin(localUdpPort);
  //Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
}


void loop()
{
    
    Udp.beginPacket("192.168.0.150", 8090);
    Udp.write(myArray, 8);
    Udp.endPacket();
    delay(30);
  
}
