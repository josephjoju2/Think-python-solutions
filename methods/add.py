class Time(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __str__(self):
        return('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))   

    def __add__(self,other):
        seconds=self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
        
    def time_to_int(self):
        minutes=self.hour*60 + self.minute
        seconds=minutes*60+ self.second
        return seconds

def int_to_time(t):
    time=Time()
    minutes,time.second=divmod(t,60)
    time.hour,time.minute=divmod(minutes,60)
    return time

now=Time(2,30)
duration=Time(2)
print(now+duration)
#extention=1800
#print(now+extention)
