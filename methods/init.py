class Time(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))
    
time=Time(9,30,20)
time.print_time()
