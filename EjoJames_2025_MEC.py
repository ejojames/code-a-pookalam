import turtle,math

'''
uncomment the next line to skip turtle drwaing on canvas
'''
#turtle.tracer(0) 

turtle.speed(100)
turtle.bgcolor("white")

def square(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    
def circle(color_out,color_in, r):
    turtle.penup()
    turtle.goto(0, -r)   # Move to bottom of circle
    turtle.pendown()
    turtle.pensize(2.5)
    turtle.color(color_out, color_in)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    
    

def polygon_flower(sides=6, petals=12, size=80, colors=None,
                   outline="black", border=2, offset=0):
    if colors is None:  
        colors = ["orange"] * petals
    turtle.left(offset)  #rotation
    for i in range(petals):
        polygon(sides, size, outline, colors[i % len(colors)], border)
        turtle.left(360 / petals)
    turtle.right(offset)
    
def polygon(sides=6, size=80, outline="black", fill="orange", border=2):
    turtle.pensize(border)
    turtle.color(outline, fill)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(360 / sides)
    turtle.end_fill()
    turtle.pensize(1)

def hexagon(radius=100, color="orange", outline="black", border=2, offset=0):

    turtle.pensize(border)
    turtle.color(outline, color)

    #hexagon vertices
    vertices = []
    for i in range(6):
        angle = math.radians(offset + i * 60)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y))

    #first vertex
    turtle.penup()
    turtle.goto(vertices[0])
    turtle.pendown()

    # draw hexagon
    turtle.begin_fill()
    for v in vertices[1:]:
        turtle.goto(v)
    turtle.goto(vertices[0])  # close shape
    turtle.end_fill()

def diamond_petal(length, angle, color="red"):
    
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(length)
        turtle.left(angle)
        turtle.forward(length)
        turtle.left(180 - angle)
    turtle.end_fill()
    
def petal(r, angle, color):

    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(r, angle)    # arc
        turtle.left(180 - angle)   
    turtle.end_fill()


def arc_flower(radius, angle, petals, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(petals):
        turtle.circle(radius, angle)     # draw arc
        turtle.left(180 - angle)
        turtle.circle(radius, angle)     #mirror arc
        turtle.left(360 / petals)
    turtle.end_fill()

def leaf(length=100, angle=60, outline="green", fill="lightgreen", border=2):
    
    turtle.pensize(border)
    turtle.color(outline, fill)
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(length, angle)   
        turtle.left(180 - angle)       
    turtle.end_fill()
    turtle.pensize(1)
    
def leaf_circle(leaves=12, length=100, angle=60, outline="green", fill="lightgreen", border=2):
    
    for _ in range(leaves):
        leaf(length, angle, outline, fill, border)
        turtle.left(360 / leaves)

    

def petal_circle(petals=12, r=100, angle=60, offset=0, outline="black", fill="orange", border=2):
    turtle.pensize(border)
    turtle.color(outline, fill)
    turtle.begin_fill()
    turtle.left(offset)  # rotate whole flower
    for _ in range(petals):
        for _ in range(2):           # one petal (two arcs)
            turtle.circle(r, angle)
            turtle.left(180 - angle)
        turtle.left(360 / petals)    # move to next petal
    turtle.right(offset)  # reset orientation
    turtle.end_fill()
    turtle.pensize(1)
  

def petal(radius=100, angle=60, fill="pink", outline="black", border=2):
   
    turtle.pensize(border)
    turtle.color(outline, fill)
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(radius, angle)
        turtle.left(180 - angle)
    turtle.end_fill()

def flower(x=0, y=0, petals=6, radius=100, angle=60,
           petal_color="pink", outline="black", border=2,
           center_color="yellow", center_radius=40,
           bg_circle_radius=None, bg_color="lightblue", bg_outline="black"):

    if bg_circle_radius:
        turtle.penup()
        turtle.goto(x, y - bg_circle_radius)
        turtle.pendown()
        turtle.color(bg_outline, bg_color)
        turtle.begin_fill()
        turtle.circle(bg_circle_radius)
        turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    step = 360 / petals
    for _ in range(petals):
        petal(radius, angle, petal_color, outline, border)
        turtle.left(step)

    # Draw the center
    turtle.penup()
    turtle.goto(x, y - center_radius)
    turtle.pendown()
    turtle.color(outline, center_color)
    turtle.begin_fill()
    turtle.circle(center_radius)
    turtle.end_fill()

    turtle.penup()
    turtle.home()
    turtle.pendown()


circle("black","brown",400)
circle("red","#FFFF3E",380)

for k in range(37):
    square(268.5,"red")
    turtle.rt(10)
turtle.home()
circle("black","orange",350)
circle("red","#FFFC43",340)
circle("maroon","#066B24",330)

polygon_flower(sides=8, petals=22, size=125,
               colors=["#FF2727", "#FF7C17","#FFFB0A", "#FF2600"],
               border=1)

circle("maroon","#FCFF9C",305)

for i in range(100):
    diamond_petal(150, 20, "#FFFB22")
    turtle.left(360/100)

for i in range(100):
    diamond_petal(150, 10, "#FF3B21")
    turtle.left(360/100)


hexagon(radius=300, color="#FF2B10", outline="maroon", border=3)
hexagon(radius=290, color="#FFEB12", outline="red", border=2, offset=90)
turtle.home()


#circle("maroon","#241717",250)
circle("maroon","#035A34",230)


leaf_circle(
    leaves=24,
    length=250,
    angle=60,
    outline="",
    fill="#FF0000",
    border=3
)
leaf_circle(
    leaves=12,
    length=250,
    angle=60,
    outline="",
    fill="#FF6912",
    border=3
)
leaf_circle(
    leaves=6,
    length=250,
    angle=60,
    outline="",
    fill="#F15D01",
    border=3
)
leaf_circle(
    leaves=4,
    length=250,
    angle=60,
    outline="",
    fill="#E26111",
    border=3
)


circle("","#FF0084",200)
circle("","#FA0D0D",195)
circle("","#FF8C11",180)
circle("","#F7BF07",170)
circle("","#EFE70A",160)
circle("maroon","#ff0000",150)

# Layer 1
petal_circle(petals=12, r=150, angle=60, offset=0, outline="red", fill="orange", border=2)

# Layer 2 
petal_circle(petals=12, r=150, angle=60, offset=20, outline="red", fill="yellow", border=2)

# Layer 3 
petal_circle(petals=12, r=150, angle=60, offset=40, outline="red", fill="maroon", border=2)

flower(x=0, y=0, petals=10, radius=20, angle=60,
       petal_color="#FF0A0A", outline="#FFE30E", center_color="yellow", center_radius=0,
       bg_circle_radius=20, bg_color="black", bg_outline="")


turtle.home()
turtle.done()