import Turtle.*;
import processing.svg.*;

Turtle t;
int m = 0;

void recurse(int iteration, float length, float angle)
{
  if (iteration == 0) {
    //form leaf
    t.right(45);t.forward(1);t.left(90);t.forward(1);t.left(90);t.forward(1);t.left(90);t.forward(1);t.left(135);
    return;
  }
  
  float n = noise(m);
  float a = map(n, 0, 1, -6, 6);
  float l = map(n, 0, 1, -length/10, length/10);
  m += 1;
  
  //left branch
  t.forward(length);
  t.left(angle);
  recurse(iteration - 1, length/1.5 + l, angle + a);
  
  //right branch
  t.right(2 * (angle));
  recurse(iteration - 1, length/1.5 + l, angle + a);
  t.left(angle);
  t.back(length);
}

void setup() {
  size(500, 500);
  t = new Turtle(this);
  noLoop();
  String folder = "output";
  String fileName = "drawing-" + getDateString() + ".svg";
}

void draw() {
  noFill();
  t.penUp();
  t.back(150);
  t.penDown();
  recurse(9, 100, 30);
  line(0,400, 500, 400);
  drawStars();
}

void drawStars() {
  for(int i = 0; i < 35; i++) {
    float x = random(500);
    float y = random(300);
    circle(x,y,1);
  }
}

void keyPressed() { 
  // press 's' to save a svg of your drawing
  if (key == 's') {
    // Make file name with the currrent date/time
    String folder = "output";
    String fileName = "drawing-" + getDateString() + ".svg";
    beginRecord(SVG, folder + "/" + fileName);
    draw();
    endRecord();
    println("Saved to file: " + fileName);
  }
} 

String getDateString() {
  String time = str(hour()) + "_" + str(minute()) + "_" + str(second());
  String date = str(year()) + "_" + str(month()) + "_" + str(day());
  return date + "-" + time;
}
