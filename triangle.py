# Learn Python together

""" Write a function named is_triangle that takes three integers
as arguments,and that prints either Yes or No, depending on whether
you can or cannot  form a triangle from sticks with the given lengths"""

#Solution
def is_triangle(x,y,z):
    if x <= 0 or y <= 0 or z <= 0:
        print("Error! Input only a positive numbers for triangle")
    elif type(x) != int or type(y) != int or type (z) != int:
        print("TypeError: Arguments must be only integers")
    elif (x+y) < z or (y+z) < x or (z+x) < y:
        print("No, it's not triangle") 
    else:
        print("Yes, it's triangle") 

#check
is_triangle(3.5,8,5)
# Output-> TypeError: Arguments must be only integers
is_triangle(14,-5,5)
# Output-> Error! Input only a positive numbers for triangle
is_triangle(15,8,5)
# Output-> No, it's not triangle
is_triangle(4,8,5)
# Output-> Yes, it's triangle

    