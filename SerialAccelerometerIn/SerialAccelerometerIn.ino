#include "Accelerometer.h"

const int samplingRate = 800;

Accelerometer acc1 {1, A0, A1, A2};
Accelerometer acc2 {2, A3, A4, A5};


void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  analogReadResolution(12);
}

void loop() {
  if (micros() - acc1.getTimestamp() >= samplingRate - 3) { acc1.readAcc(); }; // read from acc 1
  if (micros() - acc2.getTimestamp() >= samplingRate - 3) { acc2.readAcc();  Serial.println(acc1.getSample() + " " + acc2.getSample()); }; // read from acc 2
}
