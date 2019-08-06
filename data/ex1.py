t=['a','b','a','c']
def histogram(x):
    count=dict()
    for i in x:
        if i not in count:
            count.setdefault(i,1)
        else:
            count[i]+=1
    print(count)

    total=0
    for i in count.values():
        total+=i
    print (total)
    

    
(histogram(t))
