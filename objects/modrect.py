import copy
class point(object):
    pass
p=point()
p.x=4.0
p.y=5.0

print(p.x)
print(p.y)

class Rectangle(object):
    pass
box=Rectangle()
box.height=100.0
box.width=50.0
box.corner=point()
box.corner.x=0.0
box.corner.y=0.0

def grow_rectangle(rect,dwidth,dheight):
    rect.width+=dwidth
    rect.height+=dheight

box2=copy.copy(box)
 
grow_rectangle(box2,50,50)
print(box2.height)
print(box2.width)

box3=copy.deepcopy(box)

def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy
move_rectangle(box3,2,3)
print(box3.corner.x)
print(box3.corner.y)


