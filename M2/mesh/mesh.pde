import megamu.mesh.*;
import processing.svg.*;
import processing.pdf.*;

Voronoi v;

void setup() {
  size(500,500);
  
  //creating random points 
  //randomSeed(0);
  int num_points = 10;
  float[][] points = new float[num_points][2];
  
  for(int i = 0; i < num_points; i++) {
    points[i][0] = random(0, 500);
    points[i][1] = random(0, 500);
  }
  
  v = new Voronoi( points );
  noLoop();
}

void draw() {
  background(255);
  drawEdges();
  drawPatterns();
}

void drawEdges() {
  float[][] edges = v.getEdges();

  for(int i=0; i<edges.length; i++)
    line( edges[i][0], edges[i][1], edges[i][2], edges[i][3]);
}

void drawPatterns() {
  MPolygon[] myRegions = v.getRegions();

  for(int i=0; i<myRegions.length; i++)
  {
    float[][] coords = myRegions[i].getCoords();
    int l = coords.length;
    PVector[] polygon = new PVector[l];
    for (int j = 0; j < l; j++) {
      polygon[j] = new PVector(coords[j][0], coords[j][1]);
    }
    if (random(1) > 0.5) pfill(polygon);
  }
}

void pfill(PVector[] polygon) {
  noFill();
  
  int minDotSize = int(random(1,3));
  int maxDotSize = int(random(4,7)); 
  int density = int(random(8,15)); 

  //find bounds so we don't do as much computation
  float minX = 0, maxX = 500, minY = 0, maxY = 500;
  for (PVector vertex : polygon) {
    minX = min(minX, vertex.x);
    maxX = max(maxX, vertex.x);
    minY = min(minY, vertex.y);
    maxY = max(maxY, vertex.y);
  }

  for (float x = minX; x <= maxX; x += density) {
    for (float y = minY; y <= maxY; y += density) {
      float size = map(x, minX, maxX, minDotSize, maxDotSize);
      if (inPolygon(polygon, x, y) && 
          inPolygon(polygon, x + size, y) &&
          inPolygon(polygon, x, y + size) &&
          inPolygon(polygon, x - size, y) &&
          inPolygon(polygon, x, y - size)) {
        circle(x, y, size);
      }
    }
  }
}


boolean inPolygon(PVector[] polygon, float x, float y) {
  //ray casting algorithm
  boolean inside = false;
  for (int i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
    if (((polygon[i].y > y) != (polygon[j].y > y)) &&
       (x < (polygon[j].x - polygon[i].x) * (y - polygon[i].y) / (polygon[j].y-polygon[i].y) + polygon[i].x)) {
      inside = !inside;
    }
  }
  return inside;
}

void keyPressed() { 
  // press 's' to save a svg of your drawing
  if (key == 's') {
    save("test.png");
    //Make file name with the currrent date/time
    String folder = "output";
    String fileName = "drawing-" + getDateString() + ".svg";
    //save(folder + "/" + "drawing-" + getDateString() + ".jpeg");
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
