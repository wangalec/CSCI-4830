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
#         adjusted_start = (start[0] + 105, start[1] + 105, start[2])
        
#         # Adjusting the end coordinates
#         adjusted_end = (end[0] + 105, end[1] + 105, end[2])
        
#         # Append the adjusted line segment to the new list
#         shifted_lines.append((adjusted_start, adjusted_end))
    
#     return shifted_lines

# print(generate_lines())


def generate_lines_small():

    lines = []
    z = 0.3

    lines.append([(0,0,z), (0,20,z)])
    lines.append([(0,20,z), (20,20,z)])
    lines.append([(20,20,z), (20,0,z)])
    lines.append([(20,0,z), (0,0,z)])

    for _ in range(4):
        lines.append([(0,0,z), (0,0,z+5)])
        lines.append([(0,0,z+5), (0,10,z)])
        lines.append([(0,10,z), (0,10,z+5)])
        lines.append([(0,10,z+5), (0,20,z)])

        lines.append([(0,20,z), (0,20,z+5)])
        lines.append([(0,20,z+5), (10,20,z)])
        lines.append([(10,20,z), (10,20,z+5)])
        lines.append([(10,20,z+5), (20,20,z)])

        lines.append([(20,20,z), (20,20,z+5)])
        lines.append([(20,20,z+5), (20,10,z)])
        lines.append([(20,10,z), (20,10,z+5)])
        lines.append([(20,10,z+5), (20,0,z)])

        lines.append([(20,0,z), (20,0,z+5)])
        lines.append([(20,0,z+5), (10,0,z)])
        lines.append([(10,0,z), (10,0,z+5)])

        z += 5

        lines.append('retract')
        lines.append('fan_off')
        lines.append([(0,0,z), (0,20,z)])
        lines.append([(0,20,z), (20,20,z)])
        lines.append([(20,20,z), (20,0,z)])
        lines.append([(20,0,z), (0,0,z)])
        lines.append('fan_on')
    
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



# def generate_lines():
#     lines = []
#     x, y, z, = 0, 0, 0.3
#     move_h = 10
#     move_v = 5

#     lines.append([(x, y, z), (x, y + 20, z)])
#     lines.append([(x, y + 20, z), (x + 20, y + 20, z)])
#     lines.append([(x + 20, y + 20, z), (x + 20, y, z)])
#     lines.append([(x + 20, y, z), (x, y, z)])

#     for _ in range(4):

#         direction_x = 0
#         direction_y = 1

#         lines.append([(x, y, z), (x, y, z + 5)])