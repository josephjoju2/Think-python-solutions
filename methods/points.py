class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    
    def print_point(self):
        print('x:%.2d,y:%.2d'%(self.x,self.y))

point=Point(3,2)
point.print_point()
