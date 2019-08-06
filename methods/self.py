class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))
    def time_to_int(self):
        minutes=self.hour*60+self.minute
        seconds=minutes*60+self.second
        return seconds
    def time_incr(self,seconds):
        seconds+=self.time_to_int()
        return int_to_time(seconds)



def divmod(x,y):
    return x/y,x%y

def int_to_time(seconds):
    t=Time()
    minutes,t.second=divmod(seconds,60)
    t.hour,t.minute=divmod(minutes,60)
    return t

time=Time()
time.hour=10
time.minute=45
time.second=56

time.print_time()   

seconds=time.time_to_int()
print(seconds)

done=int_to_time(seconds)

done.print_time()


incr=time.time_incr(404)
incr.print_time()
