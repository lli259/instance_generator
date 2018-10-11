'''
#parameters:
n: node
a,b:lower_bound and upper_bound of distances of edges between nodes
d: number of deleted edges
s: samples


'''
import sys


def write_nodes(n,f):
	for i in range(1,n+1):
		f.write("node("+str(i)+").\n")

def generate_edges(dic,n,a,b):
	for i in range(1,n+1):
		for j in range(1,n+1):
			if (abs(j-i)>=a and abs(j-i)<=b) or (n-abs(j-i)>=a and n-abs(j-i)<=b):
				dic[str(i)+','+str(j)]=1
				dic[str(j)+','+str(i)]=1

def delete_edges(dic,e) :
	e_del=0
	while True:
		if e_del==e:
			break
		if len(dic)==0:
			break
		sample=random.sample(range(1,n+1),2)
		startE=sample[0]
		endE=sample[1]
		value=str(startE)+','+str(endE) 
		if value in dic.keys():
			del dic[value]
			e_del+=1

def write_edges(dic,f):
	for i in dic.keys():
		edgestring="link("+i+").\n"
		f.write(edgestring)	

_,n,a,b,d,s=sys.argv
n=int(n)
a=int(a)
b=int(b)
d=int(d)
s=int(s)


f=open("instDis"+str(n)+str(a)+str(b)+"_"+str(d)+"_"+str(s)+".csv","w")
write_nodes(n,f)
dic={}
generate_edges(dic,n,a,b)
delete_edges(dic,d)
write_edges(dic,f)
f.close()

