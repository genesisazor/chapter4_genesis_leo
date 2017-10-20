import turtle

wn = turtle.Screen()
lo=turtle.Turtle()
wn.bgcolor("lightgreen")
lo.pensize(3)
lo.color("hotpink")
lo.speed(10)

def draw_stars(turt,size):
    for n in range (5):
        for i in range (5):
            turt.forward(size)
            turt.right(144)
        turt.penup()
        turt.forward(350)
        turt.right(144)
        turt.pendown()
  
draw_stars(lo,100)
wn.mainloop()
        