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
