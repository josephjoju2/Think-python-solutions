def divmod(x,y):
    return x/y , x%y
class Time(object):
    pass

def print_time(t):
    print('%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))

def time_to_int(time):
    minutes=time.hour*60+time.minute
    seconds=minutes*60+time.second
    return seconds

time=Time()
time.hour=10
time.minute=45
time.second=55

seconds=time_to_int(time)
print(seconds)

def int_to_time(seconds):
    t=Time()
    minutes,t.second=divmod(seconds,60) 
    t.hour,t.minute=divmod(minutes,60) 
    return t

done=int_to_time(seconds)  
print_time(done)

print(time_to_int(int_to_time(36000))==36000)

def add_time(t1,t2):
    seconds=time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)
    

start=Time()
start.hour=2
start.minute=30
start.second=38

summ=add_time(time,start)
print_time(summ)

if __name__==__main__:
    pass
