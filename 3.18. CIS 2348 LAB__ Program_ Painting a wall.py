# Tri Dao
# 1954347
# Program: Painting a wall

import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width and height
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))

# Calculate and output wall area
print('Wall area:', wall_height * wall_width, 'square feet')
   
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
print('Paint needed: {:.2f} gallons'.format((wall_height * wall_width) / 350))

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
Cans = math.ceil((wall_height * wall_width) / 350)
print('Cans needed:', Cans,'can(s)')

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
color = input('\nChoose a color to paint the wall:\n')
print('Cost of purchasing {} paint: $'.format(color), end='')
print(paint_colors[color] * Cans)