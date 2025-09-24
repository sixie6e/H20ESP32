#include <OneWire.h>
#include <DallasTemperature.h>
#define one_wire_bus 4
#define water_sensor A0

OneWire oneWire(one_wire_bus);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
  pinMode(water_sensor, INPUT);
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  int waterLevel = analogRead(water_sensor);
  Serial.print(tempC);
  Serial.print(",");
  Serial.println(waterLevel);

  delay(2000);
}
