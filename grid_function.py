# Learn Python together
"""Write a function that draw a grid"""  

# Solution 
def grid(n):
    plus ='+'
    minus = ' - '
    post = '|'
    space = '   '
    if n > 1:
        print(plus, minus*n, plus, minus*n, plus, end="\n")
        
        for i in range(n):
            print(post, space*n, post, space*n,post, end="\n")
        print(plus, minus*n, plus, minus*n, plus, end="\n")
    elif n == 1:
        print(plus, minus*n, plus, minus*n, plus, end="\n")
        print(post, space*n, post, space*n,post, end="\n")
        print(plus, minus*n, plus, minus*n, plus, end="\n")
    else:
        print("Error:Input only a positive numbers")

def do_twice(f,n):
    f(n)
    f(n)

print('Output for grid fuction is: ')
grid(1)
print('Output for do_twice fuction is: ')
do_twice(grid,4)


       
         