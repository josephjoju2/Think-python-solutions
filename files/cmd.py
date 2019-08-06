import os
cmd='ls -l'
fp=os.popen(cmd)
res=fp.read()
print(res)
stat=fp.close()
print(stat)
