# def generate_lines():

#     lines = []
#     z = 0.3

#     lines.append([(0,0,z), (0,28,z)])
#     lines.append([(0,28,z), (28,28,z)])
#     lines.append([(28,28,z), (28,0,z)])
#     lines.append([(28,0,z), (0,0,z)])

#     for _ in range(4):

#         lines.append([(0,0,z), (0,0,z+7)])
#         lines.append([(0,0,z+7), (0,14,z)])
#         lines.append([(0,14,z), (0,14,z+7)])
#         lines.append([(0,14,z+7), (0,28,z)])

#         lines.append([(0,28,z), (0,28,z+7)])
#         lines.append([(0,28,z+7), (14,28,z)])
#         lines.append([(14,28,z), (14,28,z+7)])
#         lines.append([(14,28,z+7), (28,28,z)])

#         lines.append([(28,28,z), (28,28,z+7)])
#         lines.append([(28,28,z+7), (28,14,z)])
#         lines.append([(28,14,z), (28,14,z+7)])
#         lines.append([(28,14,z+7), (28,0,z)])

#         lines.append([(28,0,z), (28,0,z+7)])
#         lines.append([(28,0,z+7), (14,0,z)])
#         lines.append([(14,0,z), (14,0,z+7)])

#         z += 7

#         lines.append([(0,0,z), (0,28,z)])
#         lines.append([(0,28,z), (28,28,z)])
#         lines.append([(28,28,z), (28,0,z)])
#         lines.append([(28,0,z), (0,0,z)])

#     shifted_lines = []

#     for start, end in lines:
#         # Adjusting the start coordinates
#         adjusted_start = (start[0] + 10layer_height, start[1] + 10layer_height, start[2])
        
#         # Adjusting the end coordinates
#         adjusted_end = (end[0] + 10layer_height, end[1] + 10layer_height, end[2])
        
#         # Append the adjusted line segment to the new list
#         shifted_lines.append((adjusted_start, adjusted_end))
    
#     return shifted_lines

# print(generate_lines())


def generate_lines_small():
    layer_height = 5

    lines = []
    z = 0.3

    lines.append([(0,0,z), (0,20,z)])
    lines.append([(0,20,z), (20,20,z)])
    lines.append([(20,20,z), (20,0,z)])
    lines.append([(20,0,z), (0,0,z)])

    for _ in range(4):
        lines.append([(0,0,z), (0,0,z+layer_height)])
        lines.append([(0,0,z+layer_height), (0,10,z)])
        lines.append([(0,10,z), (0,10,z+layer_height)])
        lines.append([(0,10,z+layer_height), (0,20,z)])

        lines.append([(0,20,z), (0,20,z+layer_height)])
        lines.append([(0,20,z+layer_height), (10,20,z)])
        lines.append([(10,20,z), (10,20,z+layer_height)])
        lines.append([(10,20,z+layer_height), (20,20,z)])

        lines.append([(20,20,z), (20,20,z+layer_height)])
        lines.append([(20,20,z+layer_height), (20,10,z)])
        lines.append([(20,10,z), (20,10,z+layer_height)])
        lines.append([(20,10,z+layer_height), (20,0,z)])

        lines.append([(20,0,z), (20,0,z+layer_height)])
        lines.append([(20,0,z+layer_height), (10,0,z)])
        lines.append([(10,0,z), (10,0,z+layer_height)])

        z += layer_height

        lines.append('retract')
        lines.append('fan_off')
        lines.append([(0,0,z), (0,20,z)])
        lines.append([(0,20,z), (20,20,z)])
        lines.append([(20,20,z), (20,0,z)])
        lines.append([(20,0,z), (0,0,z)])
        lines.append('fan_on')
    
    return shift_lines(lines)



# def generate_lines():
#     lines = []
#     x, y, z, = 0, 0, 0.3
#     move_h = 10
#     move_v = layer_height

#     lines.append([(x, y, z), (x, y + 20, z)])
#     lines.append([(x, y + 20, z), (x + 20, y + 20, z)])
#     lines.append([(x + 20, y + 20, z), (x + 20, y, z)])
#     lines.append([(x + 20, y, z), (x, y, z)])

#     for _ in range(4):

#         direction_x = 0
#         direction_y = 1

#         lines.append([(x, y, z), (x, y, z + layer_height)])



def generate_lines_2():

    layer_height = 4

    lines = []
    z = 0.3

    lines.append([(0,0,z), (0,20,z)])
    lines.append([(0,20,z), (20,20,z)])
    lines.append([(20,20,z), (20,0,z)])
    lines.append([(20,0,z), (0,0,z)])

    lines.append([(0,0,z), (0,0,z+layer_height)])
    lines.append([(0,0,z+layer_height), (0,10,z)])
    lines.append([(0,10,z), (0,10,z+layer_height)])
    lines.append([(0,10,z+layer_height), (0,20,z)])

    lines.append([(0,20,z), (0,20,z+layer_height)])
    lines.append([(0,20,z+layer_height), (10,20,z)])
    lines.append([(10,20,z), (10,20,z+layer_height)])
    lines.append([(10,20,z+layer_height), (20,20,z)])

    lines.append([(20,20,z), (20,20,z+layer_height)])
    lines.append([(20,20,z+layer_height), (20,10,z)])
    lines.append([(20,10,z), (20,10,z+layer_height)])
    lines.append([(20,10,z+layer_height), (20,0,z)])

    lines.append([(20,0,z), (20,0,z+layer_height)])
    lines.append([(20,0,z+layer_height), (10,0,z)])
    lines.append([(10,0,z), (10,0,z+layer_height)])

    z += layer_height

    lines.append([(10,0,z), (0,0,z)])
    lines.append([(0,0,z), (0,20,z)])
    lines.append([(0,20,z), (20,20,z)])
    lines.append([(20,20,z), (20,0,z)])
    lines.append([(20,0,z), (10,0,z)])

    lines.append([(10,0,z), (10,0,z+layer_height)])
    lines.append([(10,0,z+layer_height), (0,0,z)])

    lines.append([(0,0,z), (0,0,z+layer_height)])
    lines.append([(0,0,z+layer_height), (0,10,z)])
    lines.append([(0,10,z), (0,10,z+layer_height)])
    lines.append([(0,10,z+layer_height), (0,20,z)])

    lines.append([(0,20,z), (0,20,z+layer_height)])
    lines.append([(0,20,z+layer_height), (10,20,z)])
    lines.append([(10,20,z), (10,20,z+layer_height)])
    lines.append([(10,20,z+layer_height), (20,20,z)])

    lines.append([(20,20,z), (20,20,z+layer_height)])
    lines.append([(20,20,z+layer_height), (20,10,z)])
    lines.append([(20,10,z), (20,10,z+layer_height)])
    lines.append([(20,10,z+layer_height), (20,0,z)])

    lines.append([(20,0,z), (20,0,z+layer_height)])

    z += layer_height

    lines.append([(20,0,z), (0,0,z)])
    lines.append([(0,0,z), (0,20,z)])
    lines.append([(0,20,z), (20,20,z)])
    lines.append([(20,20,z), (20,0,z)])

    return shift_lines(lines)



def shift_lines(lines):
    shifted_lines = []
    for line in lines:
        if isinstance(line, str):
            shifted_lines.append(line)
            continue
        start, end = line
        adjusted_start = (start[0] + 105, start[1] + 105, start[2])
        adjusted_end = (end[0] + 105, end[1] + 105, end[2])
        shifted_lines.append((adjusted_start, adjusted_end))
    
    return shifted_lines

def shift_lines_point(lines):
    shifted_lines = []
    for line in lines:
        shifted_lines.append((line[0] + 105, line[1] + 105, line[2]))
    return shifted_lines

def generate_point_to_lines(points):
    lines = []
    for i in range(len(points) - 1):
        lines.append([points[i], points[i+1]])
    return lines


def generate_lines_general(x_length=16, y_length=16, layers=2, layer_height = 4):
    lines = [(0, 0, 0.3), (0, y_length, 0.3), (x_length, y_length, 0.3), (x_length, 0, 0.3), (0, 0, 0.3)]
    x, y, z = 0, 0, 0.3

    x_move, y_move = 8, 8
    direction = (-1, 0) #x, y

    direction_map = {
        (0,1): (1,0),
        (1,0): (0,-1),
        (0,-1): (-1,0),
        (-1,0): (0,1)
    }

    corner_map = {
        (0,1): (0, y_length),
        (1,0): (x_length, y_length),
        (0,-1): (x_length, 0),
        (-1,0): (0, 0)
    }

    corners = set([(0,0), (0, y_length), (x_length, y_length), (x_length, 0)])

    for _ in range(layers):
        layer_start_point = (x, y, z)

        form_wireframe = True
        while form_wireframe:
            direction = direction_map[direction]
            while True:
                lines.append((x, y, z+layer_height))
                if x+x_move*direction[0] == layer_start_point[0] and y+y_move*direction[1] == layer_start_point[1]:
                    form_wireframe = False
                    break
                lines.append((x+x_move*direction[0], y+y_move*direction[1], z))
                x += x_move*direction[0]
                y += y_move*direction[1]
                
                if (x, y) in corners:
                    break
        
        z += layer_height
        layer_end_point = (x, y, z)

        if (layer_end_point[0], layer_end_point[1]) in corners:
            xt, yt = corner_map[direction]
            lines.append((xt, yt, z))
            for _ in range(3):
                direction = direction_map[direction]
                xt, yt = corner_map[direction]
                lines.append((xt, yt, z))
        else:
            xt, yt = corner_map[direction]
            lines.append((xt, yt, z))
            for _ in range(3):
                direction = direction_map[direction]
                xt, yt = corner_map[direction]
                lines.append((xt, yt, z))
            lines.append(layer_end_point)
        x, y, z = layer_end_point        
    
    return generate_point_to_lines(shift_lines_point(lines))