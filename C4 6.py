import turtle

wn = turtle.Screen()
lo=turtle.Turtle()
def draw_poly(turt,sz,num):
    for i in range(num):
        turt.forward(sz)
        turt.left(360/num)

def draw_equitriangle(t, sz):
    draw_poly(t,sz,3)
    
draw_equitriangle(lo,100)



wn.mainloop()
    
    