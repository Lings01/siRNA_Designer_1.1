def RunFun(a,b,c):
    sequence=open(a,'r')
    sirna=open(b,'w')
    line_seq=sequence.readlines()

    for j in range(int(len(line_seq)/2)):
        code=line_seq[2*(j+1)-1][:-1]
        name=line_seq[2*j][:-1]
        i=0
        while i <= len(code)-23:
    #数据预处理
            au_num1=0
            au_num2=0
            cg_num=0
            for k in range(5):
                if code[i+k+15]=='A' or code[i+k+15]=='T':
                    au_num1+=1
            for k in range(7):
                if code[i+k+13]=='A' or code[i+k+13]=='T':
                    au_num2+=1
            for k in range(23):
                if code[i+k]=='C' or code[i+k]=='G':
                    cg_num+=1
            rate_of_cg=cg_num/23
    #查找
            if code[i]=='G' or code[i]=='C': #第一位为G或C
                if code[i+18]=='A' or code[i+18]=='T': #19位为A或T
                    if au_num1>=3 or au_num2>=5: # 15~19 至少有3个A或U,或着13~19至少有5个A或U
                        if rate_of_cg>0.3 and rate_of_cg<0.52:
                            if code[i+15]=='C' and code[i+12]!='G':
                                if code[i+22]=='A':
                                    sirna.write(name+'_#'+str(i)+'\n'+code[i:i+23]+'\n')
                                    i+=1
                                else:
                                    i+=1
                            else:
                                i+=1
                        else:
                            i+=1
                    else:
                        i+=1
                else:
                    i+=1
            else:
                i+=1
    #    sirna.write('\n')
    sirna.close()
    sequence.close()

    presirna=open(b,'r')
    finalsirna=open(c,'w')

    line_presirna=presirna.readlines()


    for n in range(int(len(line_presirna)/2)):
        sirna_code=line_presirna[2*(n+1)-1][:-1]
        sirna_name=line_presirna[2*n][:-1]

    #antisense_code
        antisense_code=[]
        m=1
        for o in range(len(sirna_code)):
            if sirna_code[len(sirna_code)-m]=='A':
                antisense_code.append('T')
            elif sirna_code[len(sirna_code)-m]=='T':
                antisense_code.append('A')
            elif sirna_code[len(sirna_code)-m]=='C':
                antisense_code.append('G')
            elif sirna_code[len(sirna_code)-m]=='G':
                antisense_code.append('C')
            m+=1
        anticode="".join(antisense_code)
        finalsirna.write(sirna_name+"\n")
        finalsirna.write("ATAGTGAGTCGTATTAACGTACCAAC"+anticode+"ACTTG"+sirna_code+"TAGAGGCATATCCCT")
        finalsirna.write("\n")
    finalsirna.close()
    presirna.close()
