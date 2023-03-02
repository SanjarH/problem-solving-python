# Learn Python together
"""A child is playing with a ball on the nth floor of a tall building. 
The height of this floor above ground level, h, is known.
He drops the ball out of the window. The ball bounces (for example), 
to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of 
her window (including when it's falling and bouncing?
Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, 
return a positive integer, otherwise return -1."""

def bouncing_ball(h, bounce, window):
     # check if input values are valid
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1  # count the first pass
    height = h * bounce  # height of the first bounce
    
    # keep bouncing the ball until it stops bouncing higher than the window
    while height > window:
        count += 2  # count the upward and downward passes
        height *= bounce  # height of the next bounce
    
    return count