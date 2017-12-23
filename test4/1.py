import sys
def asc(x):
 c=[]
 open(x).readlines()
 for line in open(x):
  if line != '\n':
    line=line.strip('\'"\n')
    c.append(line)
 c=[int(x) for x in c]
 print sorted(c)
if __name__ == "__main__":
 asc('q1.txt')
