class Time(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))
    


    def __add__(self,other):
        if isinstance(other,Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self,other):
        return self.__add__(other)



    def add_time(self,other):
        seconds=self.time_to_int()+other.time_to_int()
        return int_to_time(seconds)
    def increment(self,other):
        incr=self.time_to_int()+other
        return int_to_time(incr)

    def time_to_int(self):
        minutes=self.hour*60+self.minute
        seconds=minutes*60+self.second
        return seconds

def int_to_time(x):
    time=Time()
    minutes,time.second=divmod(x,60)
    time.hour,time.minute=divmod(minutes,60)
    return time

extra=Time(0,15)
start=Time(1,5) 
duration=Time(1,10)
print(start+duration)


other=59
print(start+other)
print(other+duration)

total=sum([start,duration,extra])
print(total)
