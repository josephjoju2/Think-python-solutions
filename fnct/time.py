class Time(object):
    pass

time=Time()
time.hour=2
time.minute=5
time.second=30

def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

print_time(time)

start=Time()
start.hour=1
start.minute=56
start.second=40

def total_time(t1,t2):
    su=Time()
    su.hour=t1.hour+t2.hour
    su.minute=t1.minute+t2.minute
    su.second=t1.second+t2.second
    if su.second>=60:
        su.second-=60
        su.minute+=1
    if su.minute>=60:
        su.minute-=60
        su.hour+=1
    return su

done=total_time(time,start)
print_time(done)

       
