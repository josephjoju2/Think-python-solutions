import math
class point1():
    pass
class point2():
    pass
first=point1()
second=point2()


first.x=3
x1=first.x
first.y=4
y1=first.y

second.x=7
x2=second.x
second.y=9
y2=second.y

dist=math.sqrt((x2-x1)+(y2-y1))
print(dist)

