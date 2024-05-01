"""
    This file contains parameters, helpers, and setup to 
    create a basic gcode generation algorithm from line segments.
    
    The main 
    
    
    Inputs:
        lines: the line segments to be converted into gcode commands for extrusion 
        nozzle_diameter: the diameter of the 3D printer's nozzle
        filament_diameter: the diameter of the 3d printing filament
        layer_height: the height of each layer in the print
        extrusion_width: the width of the extruded line from the printer
        travel_feed_rate: the speed at which the extruder moves in X and Y
        layer_change_feed_rate: the speed at which teh extruder moves when 
            changing layers in the Z direction
        extrusion_feed_rate: the speed at which the extruder move when extruding

    Output:
        gcode_output: a string with gcode commands separate by new-lines"""

# import rhinoscriptsyntax as rs
import math
import base as base
import generate_lines as generate_lines
import datetime


########## CONSTANTS BELOW ###############

layer_height = 0.3
extrusion_width = 0.48
nozzle_diameter = 0.4
layer_change_feed_rate = 720
extrusion_feed_rate = 600
travel_feed_rate = 1200
filament_diameter = 1.75

# lines = [
#     [(105,141.36,0.3), (105,105,0.3)], 
#     [(105,105,0.3), (105,105,7.3)], #vertical
#     [(105,105,7.3), (105,117.12,0.3)],
#     [(105,117.12,0.3), (105,117.12,7.3)], #vertical
#     [(105,117.12,7.3), (105,129.24,0.3)], #horizontal
#     [(105,129.24,0.3), (105,129.24,7.3)], #vertical
#     [(105,129.24,7.3), (105,141.36,0.3)], #horizontal
# ]

lines = generate_lines.generate_lines_general(x_length=24, y_length=16, layers=3)

# GCODE COMMANDS
COMMAND_MOVE = "G1"

# GCODE PARAM NAMES
PARAM_X = "X"
PARAM_Y = "Y"
PARAM_Z = "Z"
PARAM_E = "E"
PARAM_F = "F"

# Separates commands
COMMAND_DELIMITER = "\n"

# Precision for converting floats to strings
E_VALUE_PRECISION = 5
XYZ_VALUE_PRECISION = 3

# Float equality precision
FLOAT_EQUALITY_PRECISION = 5

#########################################################################

# Converts a float (f) to a string with some precision of decimal places
# For example: 
# Input: f=0.1234, precision=3 
# Output: "0.123"
def float_to_string(f, precision=XYZ_VALUE_PRECISION): 
    f = float(f)
    str_format = "{value:." + str(precision) +"f}"
    return str_format.format(value=f)
    
# Helper to convert the E value to the proper precision
def e_value_to_string(e):
    return float_to_string(e, E_VALUE_PRECISION)

# Helper to convert the XYZ value to the proper precision
def xyz_value_to_string(e):
    return float_to_string(e, XYZ_VALUE_PRECISION)

#########################################################################

# Helper function to compare floats in grasshopper/python due to float precision errors
def are_floats_equal(f1, f2, epsilon=10**(-FLOAT_EQUALITY_PRECISION)):
    f1 *= 10**FLOAT_EQUALITY_PRECISION
    f2 *= 10**FLOAT_EQUALITY_PRECISION
    return math.fabs(f2 - f1) <= epsilon
    
# Helper function to compare if two points are equal (have the same coordinates)
# by handling float precision comparisons
def is_same_pt(ptA, ptB):
    return are_floats_equal(ptA[0], ptB[0]) and are_floats_equal(ptA[1], ptB[1]) and are_floats_equal(ptA[2], ptB[2])
     
     
########################################################################
# creates a string consisting of a G1 move command and 
# any associated parameters
def gcode_move(current_pos, next_pos, feed_rate=None, should_extrude=False, extrusion_multiplier=1.1):
    # Start with "G1" as command
    move_command_str = COMMAND_MOVE
    
    # Compare X positions
    if (not are_floats_equal(current_pos[0],next_pos[0])):
        # we have a different x position so add it as a parameter to the command
        x_value = float_to_string(next_pos[0], precision=XYZ_VALUE_PRECISION)
        # Add X<x_value> to move string, e.g., X100.00
        move_command_str += " " + PARAM_X + x_value
    
    # Compare Y positions
    if (not are_floats_equal(current_pos[1], next_pos[1])):
        # we have a different y position so add the new position as a parameter
        y_value = float_to_string(next_pos[1], precision=XYZ_VALUE_PRECISION)
        # Add Y<y_value> to move string, e.g., Y100.00
        move_command_str += " " + PARAM_Y + y_value
    
    # Compare Z position
    if (not are_floats_equal(current_pos[2], next_pos[2])):
        # we have a different z position so add the new position as a parameter
        z_value = float_to_string(next_pos[2], precision=XYZ_VALUE_PRECISION)
        # Add Z<z_value> to move string, e.g., Z100.00
        move_command_str += " " + PARAM_Z + z_value
    
    # [TODO]: handle "should_extrude" == true by determining the proper amount to
    # extrude using the capsule model, then append the E parameter and value
    # to the move command.
    # NOTE: YOUR FLOAT PRECISION MUST MATCH E_VALUE_PRECISION
    if (should_extrude == True):
        # distance = ((current_pos[0]-next_pos[0])**2 + (current_pos[1]-next_pos[1])**2 + (current_pos[2]-next_pos[2])**2) ** 0.5
        # V_out = (layer_height * (extrusion_width - layer_height) + math.pi * (layer_height/2) ** 2) * distance
        # A_in = math.pi * (filament_diameter/2) ** 2
        # extrusion = V_out / A_in
        e_value = float_to_string(calculate_extrusion(current_pos, next_pos)*extrusion_multiplier, precision=E_VALUE_PRECISION)
        move_command_str += " " + PARAM_E + e_value
    
    
    # See if we have a feedrate to use, and handle it differently than other 
    # parameters as it is an integer value
    if (feed_rate is not None):
        # feed rate is an int
        feed_rate_value = round(feed_rate)
        # Add F<feed_rate_value> to move string, e.g., F2000
        move_command_str += " " + PARAM_F + str(feed_rate_value)   
    
    # Remove excess whitespace on ends
    move_command_str = move_command_str.strip(" ")
    return move_command_str

def calculate_extrusion(current_pos, next_pos):
    distance = ((current_pos[0]-next_pos[0])**2 + (current_pos[1]-next_pos[1])**2 + (current_pos[2]-next_pos[2])**2) ** 0.5

    if are_floats_equal(current_pos[2], next_pos[2]):
        V_out = (layer_height * (extrusion_width - layer_height) + math.pi * (layer_height/2) ** 2) * distance
        A_in = math.pi * (filament_diameter/2) ** 2
        extrusion = V_out / A_in
        return extrusion
    else:
        V_out = (math.pi * (nozzle_diameter/2) ** 2) * distance
        A_in = math.pi * (filament_diameter/2) ** 2
        extrusion = V_out / A_in
        return extrusion


############################################
############################################
############################################
    
''' Here's the main method of the script that uses the helper methods above '''

def generate_gcode():

    # [TODO]: Implement the algorithm to generate gcode for each layer by 
    # first to moveing to the layer height, then moving to each line segment.
    # Once at a line segment, you should move and extrude along it, 
    # then move (travel) to the next line until there are no lines left
    # For each of these movements, you should append the command to
    # the list: `all_move_commands`
    current_position = [0, 0, 0]        # start extruder at the origin
    all_move_commands = []              # list to hold for all the move commands

    for i in range(0, len(lines)):
        # Get pts of the line segment
        line = lines[i]

        if line == 'retract':
            all_move_commands.append('G10')
            all_move_commands.append('G11')
            continue
        elif line == 'fan_off':
            all_move_commands.append('M107')
            continue
        elif line == 'fan_on':
            all_move_commands.append('M106')
            continue

        line_start_position = line[0]
        line_end_position = line[1]
        
        # [TODO]: Handle moving to the next layer (Z Position)
        # NOTE- ALL Z MOVEMENTS SHOULD:
        # 1) BE INDEPENDENT MOVES(e.g., G1 Z# and not move with other positions like XYE) 
        # 2) USE THE `layer_change_feedrate`
        # 3) BE IN INCREASING ORDER
        if not are_floats_equal(line_start_position[2], current_position[2]):
            temp_position = [current_position[0], current_position[1], line_start_position[2]]
            move_command = gcode_move(current_position, temp_position, feed_rate=layer_change_feed_rate)
            all_move_commands.append('G04 P1000')
            all_move_commands.append(move_command)
            current_position = temp_position
        

        # Now if our current_position is not the start of our line segment
        # we need to move (travel) to the line segment's starting point
        if not is_same_pt(current_position, line_start_position):
            # [Move to the the line_start_position
            move_to_line_start_command = gcode_move(current_position, line_start_position, feed_rate=travel_feed_rate)
            # A ppend command
            all_move_commands.append(move_to_line_start_command)
        
        # [TODO]: Once our extruder is at the start of the line, create a 
        # command to move AND extrude along 
        # the line segment using `extrusion_feed_rate`
        move_and_extrude_command = gcode_move(line_start_position, line_end_position, feed_rate=extrusion_feed_rate, should_extrude=True)

        # [TODO]: Append the move command across the line segment 
        all_move_commands.append(move_and_extrude_command)

        if are_floats_equal(line_start_position[0], line_end_position[0]) and are_floats_equal(line_start_position[1], line_end_position[1]):
            all_move_commands.append('G1 E-0.1')
            all_move_commands.append('G04 P1500')
            all_move_commands.append('G1 E0.1')
        
        # [TODO]: Update the current position of our extruder to be at the end of the line
        current_position = line_end_position
        
    # End of for-loop above -- now create the full set of commands


    # [TODO]: Once you have all of the move commands stored as a list in
    # `all_move_commands`, combine the `start_gcode`, `all_move_commands`, and `end_gcode`
    # into one list called `gcode_lines`   
    all_move_commands.append('G10')
    all_move_commands.append('G04 P1000')
    gcode_lines = base.start_gcode_lines + all_move_commands + base.end_gcode_lines

    # --- DO NOT EDIT BELOW ----
    # The takes the combined gcode_lines list and creates a string containing each line
    # separated by a COMMAND_DELIMITER (the new-line character), and sets it 
    # to the `gcode_output`variable of this component
    output = COMMAND_DELIMITER.join(gcode_lines)
    
    return output
    
''' RUN THE MAIN FUNCITON ABOVE - DO NOT EDIT '''
# this sets the gcode commands to be the the `gcode_output` variable of this grasshopper component
gcode_output = generate_gcode()

timestamp = datetime.datetime.now().strftime("%m%d-%H%M%S")
filename = f"gcode/output-{timestamp}.gcode"
with open(filename, 'w') as file:
    file.write(gcode_output)


#1200 no pause fell over