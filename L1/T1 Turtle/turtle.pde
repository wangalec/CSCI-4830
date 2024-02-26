import Turtle.*;

Turtle t;

void setup() {
  size(700, 700);
  background(255);
  t = new Turtle(this);
  noLoop();
}

void draw() {
  //triangle
  //drawPolygon(100, 3);
  
  //pentagon
  //drawPolygon(75, 5);
  
  //circle
  //drawPolygon(1, 1000);
  
  //drawing I and T
  //drawIT();
  
}


void drawPolygon(float l, float k) {
  //get angle for a polygon with k sides
  float angle = ((k-2)/k) * 180;
  
  //form polygon. move at 180 - angle since drawing from the outside
  for(int i = 0; i < k; i++) {
    t.forward(l);
    t.left(180 - angle);
  }
}

void drawIT() {
  //I
  t.left(90);
  t.forward(40);
  t.penUp();
  t.back(20);
  t.penDown();
  t.right(90);
  t.forward(100);
  t.left(90);
  t.forward(20);
  t.penUp();
  t.back(20);
  t.penDown();
  t.back(20);
  
  //T
  t.penUp();
  t.back(50);
  t.penDown();
  t.back(40);
  t.penUp();
  t.forward(20);
  t.penDown();
  t.right(90);
  t.back(100);
}
