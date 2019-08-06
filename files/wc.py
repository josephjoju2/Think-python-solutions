def wordcount(filename):
    count=0
    for line in open(filename):
        for word in line.split():
            count+=1
    return count

def linecount(filename):
    return('nice '+filename)
    
if __name__=='__main__':
    print(wordcount('output.txt'))
