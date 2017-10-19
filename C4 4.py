import turtle

def make_shape(turt,size,ang):
    for a in range(6):
        turt.right(ang)
        
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        
        for m in range(4):
            turt.backward(size)
            turt.left(90)
        
        for n in range(4):
            turt.backward(size)
            turt.right(90)
        
        for l in range(4):
            turt.forward(size)
            turt.right(90)
            

wn = turtle.Screen()
lo=turtle.Turtle()
wn.bgcolor("lightgreen")
lo.pensize(3)
lo.color("blue")

make_shape(lo,100,18)

wn.mainloop
