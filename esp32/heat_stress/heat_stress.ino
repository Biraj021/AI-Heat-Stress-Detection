#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"


// ==========================
// WiFi Configuration
// ==========================

const char* ssid = "hi";
const char* password = "12121314";


// ==========================
// Flask Backend URL
// ==========================

// Your computer IPv4 address
String serverURL = "http://10.142.179.149:5000/predict";


// ==========================
// DHT22 Configuration
// ==========================

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);


// ==========================
// Setup
// ==========================

void setup()
{
  Serial.begin(115200);

  delay(1000);

  Serial.println();
  Serial.println("==============================");
  Serial.println("AI Heat Stress Detection");
  Serial.println("==============================");


  dht.begin();


  // Connect WiFi

  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");


  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }


  Serial.println();

  Serial.println("WiFi Connected!");

  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

}


// ==========================
// Loop
// ==========================

void loop()
{

  float temperature = dht.readTemperature();

  float humidity = dht.readHumidity();



  if (isnan(temperature) || isnan(humidity))
  {
    Serial.println("DHT22 sensor error");

    delay(5000);

    return;
  }



  Serial.println();
  Serial.println("------------------------------");

  Serial.print("Ambient Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");


  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");



  if (WiFi.status() == WL_CONNECTED)
  {

    HTTPClient http;


    http.begin(serverURL);


    http.addHeader(
      "Content-Type",
      "application/json"
    );



    String json = 
    "{"
    "\"AmbientTemp\":"
    + String(temperature)
    +
    ",\"Humidity\":"
    + String(humidity)
    +
    "}";



    Serial.println("Sending data to server...");



    int httpResponseCode =
      http.POST(json);



    if (httpResponseCode > 0)
    {

      Serial.print("Server Response Code: ");

      Serial.println(httpResponseCode);



      String response =
        http.getString();



      Serial.println("AI Prediction:");

      Serial.println(response);

    }
    else
    {

      Serial.print("Connection failed: ");

      Serial.println(httpResponseCode);

    }



    http.end();

  }
  else
  {

    Serial.println("WiFi disconnected");

  }



  // wait 5 seconds

  delay(5000);

}