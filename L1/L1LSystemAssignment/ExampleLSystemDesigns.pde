// ExampleLSystemDesigns - contains initialization methods
// to set up parameters and init the LSystem (from the main file)

import java.util.HashMap;

// [TODO]: create your own L-System initialization methods
// and use/test in the setup() method of L1LSystemAssignment file. 
// See example for Square Lsystem below.

// Square Lsystem initialization 
// This method returns an Lsystem object that uses
// The rules and axioms for a square based system
LSystem initSquare() {
  // initialize turtle variables
  float moveDist = 10;
  float rotateAngle = 90;
  float scaleFactor = 1;
  
  // The intial axiom / input string
  String axiom = "F+F+F+F";
  
  // Create any production rules
  HashMap<Character, String> rules = new HashMap<>();
  rules.put('F', "F+F-F-FF+F+F-F");
    
  // Create and return the Lsystem
  return new LSystem(axiom, rules, moveDist, rotateAngle, scaleFactor);
}

LSystem design1() {
  float moveDist = 20;
  float rotateAngle = 60;
  float scaleFactor = 1;
  
  String axiom = "+F++F++F";
  
  HashMap<Character, String> rules = new HashMap<>();
  rules.put('F', "F-F++F-F");
    
  return new LSystem(axiom, rules, moveDist, rotateAngle, scaleFactor);
}

ProbabilisticLSystem design2() {
  float moveDist = 10;
  float rotateAngle = 25;
  float scaleFactor = 1;
  float angleVariation = 10;
  float distanceVariation = 5;
  
  String axiom = "F";
  
  HashMap<Character, String[]> rules = new HashMap<>();
  rules.put('F', new String[]{
    "F[+F]F[-F]F", 
    "F[-F]F[+F]F", 
    "F[+F]F", 
    "F[-F]F", 
    "FF",
    "F[-F]F[+F][F]",
    "F[+F]F[-F][F]",
  });
    
  return new ProbabilisticLSystem(axiom, rules, moveDist, rotateAngle, scaleFactor, angleVariation, distanceVariation);
}

ProbabilisticLSystem design3() {
  float moveDist = 10;
  float rotateAngle = 20;
  float scaleFactor = 1;
  float angleVariation = 5;
  float distanceVariation = 5;
  
  String axiom = "X";
  
  HashMap<Character, String[]> rules = new HashMap<>();
  rules.put('F', new String[]{"FF"});
  rules.put('X', new String[]{
    "F[+X]F[-X]+X", 
    "F[-X]F[+X]-X", 
    "X[-X][+X]FX",
    "F[+X][-X]FX",
    "F-[[X]+X]+F[+FX]-X",
    "F+[[X]-X]-F[-FX]+X"
  });
    
  return new ProbabilisticLSystem(axiom, rules, moveDist, rotateAngle, scaleFactor, angleVariation, distanceVariation);
}
