import turtle

def draw_text(t, text, colors):
    color_index = 0
    for i, char in enumerate(text):
        t.pencolor(colors[color_index])
        t.write(char, font=("Arial", 36, "normal"), align="center")
        t.forward(25)
        if (i + 1) % 4 == 0:
            color_index = (color_index + 1) % len(colors)
 
t = turtle.Turtle()
t.speed(10)
text = "CodeYourPath"
colors = ["purple", "blue"]
draw_text(t, text, colors)
t.right(180)
t.penup()
t.forward(25 * len(text))
t.pendown()
t.right(180)
turtle.done()