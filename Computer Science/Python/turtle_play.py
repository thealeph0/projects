import turtle as trd

wn = trd.Screen()
wn.setup(500,500)

trt = trd.Turtle('triangle')
trt.color('green')
trt.left(90)


def increase_size():
    size = trt.turtlesize()
    increase = (2 * num for num in size)
    trt.turtlesize(*increase)
    trt.left(70)
    
def decrease_size():
    size = trt.turtlesize()
    decrease = (1/2 * num for num in size)
    trt.turtlesize(*decrease)
    trt.left(-45)

    
wn.onkey(increase_size, 'l')
wn.onkey(decrease_size, 's')
wn.listen()

