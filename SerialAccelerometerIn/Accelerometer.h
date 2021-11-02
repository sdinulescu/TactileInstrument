class Accelerometer {
  private:
  int id = 0;
  int pastTimestamp = 0; 
  int xpin = 0; 
  int ypin = 0;
  int zpin = 0;

  public:
  Accelerometer(int id_, int xp, int yp, int zp) {
    id = id_;
    xpin = xp; 
    ypin = yp;
    zpin = zp;
  }
  
  void readAcc() {
    pastTimestamp = micros();
    int x = map(analogRead(xpin), 0, 4096, 0, 127);
    int y = map(analogRead(ypin), 0, 4096, 0, 127);
    int z = map(analogRead(zpin), 0, 4096, 0, 127);
//    String p = String(id) + " " + String(x) + " " + String(y) + " " + String(z);
//    Serial.println(p);
    Serial.print(id);
    Serial.print(",");
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.print(z);
    Serial.println(",");
  }

  int getTimestamp() { return pastTimestamp; }
};
