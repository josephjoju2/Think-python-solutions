

def sed(pat,rep,file1,file2):

    f1=open(file1,'r')
    text=f1.read()
    f2=open(file2,'r+')
    f2.write(text)
    f1.close()
    for line in f2:
        for word in line.split():
            if word==pat:
                word=rep
        print(line)
                
    f2.close()
if __name__=='__main__':
    sed('import','export','ex5.py','new')
