import random

def is_in_scope(pos, edge_size):
    y_should_be = edge_size - pos[0]
    return pos[1] <= y_should_be

def same_edge_sized_triangle_area(total,edge_size):
    counter = 0
    for i in range(total):
        pos_x = random.uniform(0,edge_size)
        pos_y = random.uniform(0,edge_size)
        # --------------------------------------------
        pos = (pos_x, pos_y)
        #print('position: x = '+str(pos[0])+' y = '+str(pos[1]))
        if is_in_scope(pos, edge_size):
            counter += 1
    return float(counter)/float(total)*edge_size**2

total = 100000
area = same_edge_sized_triangle_area(total,5)
print("area: ", round(area, 1))
