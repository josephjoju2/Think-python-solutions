class Time(object):
    def is_after(self,other):
        return (time_to_int(other) > time_to_int(self))

def time_to_int(sel):
    minutes=sel.hour*60 +sel.minute
    seconds=sel.minute*60+sel.second
    return seconds

now=Time()
now.hour=4
now.minute=23
now.second=33

after=Time()
after.hour=4
after.minute=25
after.second=55

print(now.is_after(after))
