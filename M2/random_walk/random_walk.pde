import processing.svg.*;

Walker w;

float m = 0;
float m2 = 0;

class Walker {
  float x, y; 
  
  Walker() { }
  
  void show() {
    point(x, y);
  }
  
  void step() {
    float n = noise(m);
    m += 0.1;
    float move = map(n, 0, 1, -2, 2);
    y += move;
    x++;
  }
  
  void set(int _x, int _y) {
    x = _x;
    y = _y;
  }  
}

void setup() {
  size(500, 500);
  w = new Walker();
  noLoop();
}

void draw() {
  background(255);
  for(int j = 0; j < 50; j++) {
    float variation = map(noise(m2), 0, 1, -100, 100);
    float variation2 = map(noise(m2+100), 0, 1, -100, 100);
    float variation3 = map(noise(m2+200), 0, 1, -100, 100);
    m2 += 1;
    stroke(50+variation,100+variation2,100+variation3);
    w.set(width/2 - 150, width/2);
    for(int i = 0; i < 300; i++) {
      w.step();
      w.show();
    }
  } 
}

void keyPressed() { 
  // press 's' to save a svg of your drawing
  if (key == 's') {
    // Make file name with the currrent date/time
    String folder = "output";
    String fileName = "drawing-" + getDateString() + ".jpg";
    save(folder + "/" + fileName);
    println("Saved to file: " + fileName);
  }
} 

String getDateString() {
  String time = str(hour()) + "_" + str(minute()) + "_" + str(second());
  String date = str(year()) + "_" + str(month()) + "_" + str(day());
  return date + "-" + time;
}
