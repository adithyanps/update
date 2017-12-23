
import sys
def poly(x):
 c = [tuple(line.split(',')) for line in open(x) if line != '\n']
 d=[(int(x),int(y.strip(' \n'))) for x,y in c]
 d=sorted(d,key=lambda y: y[1],reverse=True)
 print d
 z=dict()
 for (i,j) in d:
  if j in z.keys():
   z[j]=z[j]+i
  else:
   z[j]=i
 new=sorted(z.items(),reverse=True)
 print new
 print '+'.join([(str(j)+'X^'+str(i)) for i,j in new])
if __name__ == "__main__":
 poly('q2.txt')
