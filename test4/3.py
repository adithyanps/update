class poly:
    def __init__(self,fname):
        f=open(fname,'r').readlines()
        co=[]
        exp=[]
        for x in f:
            co.append(int(x.split(',')[0]))
            exp.append(int(x.split(',')[1]))
        d={}
        for x in range(len(co)):
            if exp[x] in d:
                d[exp[x]]+=co[x]
            else:
                d[exp[x]]=co[x]
        c1=[]
        e1=[]
        for x in sorted(d.keys(),reverse=True):
            c1.append(d[x])
            e1.append(x)
        self.co=c1
        self.exp=e1
    def __str__(self):
        s=''
        for x in range(len(self.co)):
            if x==len(self.co)-1:
                s+=str(self.co[x])+'x^'+str(self.exp[x])
            else:
                s+=str(self.co[x])+'x^'+str(self.exp[x])+'+'
        return s

    def exponents(self):
        return self.exp
    def coefficients(self):
        return self.co
d=poly('q1.txt')
print d
print d.exponents()
print d.coefficients()


