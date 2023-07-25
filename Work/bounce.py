# bounce.py
#
# Exercise 1.5

"""
Ball drops from height of 100m , each time it hits 
the ground it bounces back 2/3rds of it's height

What's the balls height after the first 10 bounces?

"""

bounce_rate = 0.6
curr_height = 100
n = 0

while  n <= 10:
    print(n,curr_height)
    new_height = bounce_rate * curr_height
    curr_height = new_height
    n = n + 1

    



