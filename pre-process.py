#预处理
import re
import os,sys
def RunFun(a,b,c):
    fr=open(a,'r')
    fw=open(b,'w')
    line=fr.read()
    r=line.replace('\n','')
    s=re.sub('>','\n>',r)
    fw.write(s)
    fr.close()
    fw.close()

    f=open(b)
    o=open(c,'w')
    line_f=f.readlines()
    for eachline in line_f:
        ss=re.findall('>Unigene\d\d\d\d\d\d\d',eachline)
        sss=re.sub('>Unigene\d\d\d\d\d\d\d',''.join(ss)+'\n',eachline)
        o.write(sss)
    f.close()
    o.close()
    os.remove(b)
