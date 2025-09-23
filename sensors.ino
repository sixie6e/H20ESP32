#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 4
#define WATER_SENSOR_PIN A0

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
  pinMode(WATER_SENSOR_PIN, INPUT);
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  int waterLevel = analogRead(WATER_SENSOR_PIN);
  Serial.print(tempC);
  Serial.print(",");
  Serial.println(waterLevel);

  delay(2000);
}
