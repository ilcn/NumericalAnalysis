import math

def p5c():
	xs = [2.9,3.0,3.1,3.2]
	fxs = [-4.827866, -4.240058, -3.496909, -2.596792]
	n1 = 4
	ret = [0 for x in range(n1)]
	h = xs[1]-xs[0]
	for i in range(n1):
# Use the first formula for the first point
		if i == 0: ret[i] = threepoint(fxs,i,h,1) 
# Use the third formula for the last point
		elif i ==n1-1: ret[i] = threepoint(fxs,i,-h,3)
# and the second formula for the rest
		else: ret[i] = threepoint(fxs,i,h,2)
	print ret


def threepoint(fxs,i,h,whichformula):
# whichformula indicates which formula to use
	if whichformula==1: return (1.0/(2*h))* (-3*(fxs[i])+ 4*(fxs[i+1])-fxs[i+2])
	elif whichformula ==2: return (1.0/(2*h))*(-fxs[i-1]+fxs[i+1])
	elif whichformula ==3: return (1.0/(2*h))*(-3*fxs[i]+ 4*fxs[i-1]-fxs[i-2])
	else:
		print "wrong input"
		return 0

def p5d():
#same logic, different data
	xs = [2.0,2.1,2.2,2.3]
	fxs = [3.6887983,3.6905701,3.6688192,3.6245909]
	n1 = 4
	ret = [0 for x in range(n1)]
	h = xs[1]-xs[0]
	for i in range(n1):
		if i == 0: ret[i] = threepoint(fxs,i,h,1)
		elif i ==n1-1: ret[i] = threepoint(fxs,i,-h,3)
		else: ret[i] = threepoint(fxs,i,h,2)
	print ret

def p1a():
#using the forward difference formula
	n = 3
	h = 0.4
	x0 = 1.0
	n1s = [(math.log(x0+h/(2**x))-math.log(x0))/(h/(2**x)) for x in range(n)]
	n2s = [2.0*n1s[x+1] - n1s[x] for x in range(n-1)]
	n3s = [(4*n2s[x+1]-n2s[x])/3.0 for x in range(n-2)]
	print n1s,'\n', n2s,'\n', n3s

def p1b():
#using the forward difference formula
	n=3
	h = 0.4
	x0 = 0
	n1s = [(fx(x0+h/(2**x))-fx(x0))/(h/(2**x)) for x in range(n)]
	n2s = [2.0*n1s[x+1] - n1s[x] for x in range(n-1)]
	n3s = [(4*n2s[x+1]-n2s[x])/3.0 for x in range(n-2)]
	print n1s,'\n', n2s,'\n', n3s
	
def fx(x):
	return x+math.exp(x)
