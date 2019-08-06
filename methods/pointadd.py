class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x 
        self.y=y
    def __str__(self):
        return('%.2d:%.2d'%(x.Point,y.point))
    def __add__(self,other):
        if isinstance(other,Point):
            return(self.x+other.x,self.y+other.y)
        else:
            return self.addpoint(other)
    def addpoint(self,other):
        return(self.x+other[0],self.y+other[1])
    def __radd__(self,other):
        return self.__add__(other)


p1=Point(2,3)
p2=Point(3,3)

p3=(4,4)
p4=Point(5,5)

print(p1+p2)
print(p1+p3)
print(p3+p1)

#total=sum([p1,p2,p4])
#print(total)
