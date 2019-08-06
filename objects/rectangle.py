class Point(object):
    pass
class Rectangle(object):
    pass

box=Rectangle()
box.height=13.0
box.width=20.0
box.corner=Point()
box.corner.x=0.0
box.corner.y=0.0

def center(rect):
    p=Point()
    p.x=rect.corner.x+rect.width/2.0
    p.y=rect.corner.y+rect.height/2.0
    return p

center_point=center(box)
print(center_point.x)
print(center_point.y)
print(box.corner.x)
