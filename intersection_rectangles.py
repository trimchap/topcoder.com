def x_overlap_found(all_xs):
    x1_left, x1_right, x2_left, x2_right = all_xs
    if x1_left < x2_left and x1_right > x2_left:
        return True
    elif x2_left < x1_left and x2_right > x1_left:
        return True
    else:
        return False # no x overlap

def y_overlap_found(all_ys):
    y1_bottom, y1_top, y2_bottom, y2_top = all_ys
    if y1_bottom < y2_bottom and y1_top > y2_bottom:
        return True
    elif y2_bottom < y1_bottom and y2_top > y1_bottom:
        return True
    else:
        return False # no x overlap

all_xs = []
all_ys = []

my_rectangle = {
    'left_x' : 1,
    'bottom_y' : 1,
    'width' : 6,
    'height' : 3
}

your_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'  : 4,
    'bottom_y' : 2,

    # Width and height
    'width'    : 5,
    'height'   : 4
}

print(my_rectangle)
print(your_rectangle)


all_xs = []
all_ys = []

# unpack all x's and all y's
all_xs.append(my_rectangle['left_x'])
all_xs.append(my_rectangle['left_x'] + my_rectangle['width'])
all_xs.append(your_rectangle['left_x'])
all_xs.append(your_rectangle['left_x']+your_rectangle['width'])
all_ys.append(my_rectangle['bottom_y'])
all_ys.append(my_rectangle['bottom_y'] + my_rectangle['height'])
all_ys.append(your_rectangle['bottom_y'])
all_ys.append(your_rectangle['bottom_y'] + your_rectangle['height'])

print(all_xs)
print(all_ys)
# is there an intersection??
if (x_overlap_found(all_xs)) and (y_overlap_found(all_ys)):
    # if yes, sort the x's and y's and the intersecting rectangle will be the middle coefficients
    list.sort(all_xs)
    list.sort(all_ys)
    print(all_xs)
    print(all_ys)

    love_rectangle = {
        'left_x' : all_xs[1],
        'bottom_y' : all_ys[1],
        'width' : all_xs[2] - all_xs[1],
        'height' : all_ys[2] - all_ys[1]
    }

    print(love_rectangle)
else:
    print('no overlap - no love')
