import math
def fun1(x):
	num1= 5.0/(x**2) + 2
	return num1

def bisec(a,b,error):
	a=a+0.0
	b=b+0.0
	error = error+0.0
	p = (a+b)/2.0
	n = math.ceil(math.log((b-a)/error)/math.log(2))
	print n, math.log((b-a)/error)/math.log(2)
	for i in range(1,int(n)+1):
		res = fun1(p) 
		print i, p, res
		i+=1
		if res == 0: return p
		elif res>0: b=p
		else : a=p
		p = (a+b)/2.0

def fixedpt(pi,error):
	pi = pi+0.0
	error = error+0.0
	i=1
	p = fun1(pi)
	while abs(p-pi) > error:
		
		pi=p
		p = fun1(pi)
		print i,p, abs(p-pi)
		i +=1
	
	
