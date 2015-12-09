import math

#p208
def crs(fx,n,a,b):
#composite trapezoid rule 
    h = (b-a)/n
    sums =0.0
    for x in range(1,n):
        sums+= fx((x*h+a))
    return (2*sums+ fx(a) + fx(a+n*h))*h/2

def p1c():
    return crs(lambda x: 2.0/(x*x+4.0),6,0.0,2.0)

def p2a():
    return crs(lambda x: math.cos(x)**2, 4,-.5,.5)

def css(fx,n,a,b):
#comp. simpson's rule
    h = (b-a)/n
    sums =0.0
    for j in range(1,n/2):
        sums += 2 * fx(a+2*j*h)
    for j in range(1,n/2+1):
        sums += 4 * fx(a+(2*j-1)*h)
    return (fx(a)+fx(b)+sums)*h/3

def p3c():
    return css(lambda x: 2.0/(x*x+4.0),6,0.0,2.0)

def p4a():
    return css(lambda x: math.cos(x)**2, 4,-.5,.5)

def p13a():
    return crs(lambda x: 1.0/(x+4.0), 46,0.0,2.0) 

#p217
def romberg33(f,a,b):
    hs = [ (b-a)/(2**(k-1)) for k in range(1,12)]
    print hs[1]
    r11 = hs[0]*(f(a)+f(b))/2.0
    print r11
    rk1s = [ r11 for i in range(5)]
    for k in range(1,5):
        prevr = rk1s[k-1]
        prevh = hs[k-1]
        sum1 = [f(a+(2*i-1)*hs[k]) for i in range(1, 2**(k-1)+1)]
        summation = sum(sum1)
        #print "when k = ", k, "\n previous r =", prevr, " \n previous h =" ,prevh,"h = ", hs[k], "sum = ", summation, "\n list is", sum1, '\n'
        rk1s[k]=0.5*(prevr+prevh* summation)
    rk2s = [(rk1s[k+1]*4 - rk1s[k])/3.0 for k in range(4)]
    rk3s = [(rk2s[k+1]*16- rk2s[k])/15.0 for k in range(3)]
    print rk1s,'\n',rk2s,'\n',rk3s

def p1a1():
    romberg33(lambda x: x**2 * math.log(x),1.0,1.5)

def p1c1():
    romberg33(lambda x: 2/(x**2 -4), 0.0,0.35)

#p273
def euler(f,a,b,n,alpha):
    output = []
    h = (b-a)/n
    t=a
    w=alpha
    print "for t0  = ", t, ", w1  = ", w
    for i in range(1,n+1):
        w = w+ h*f(t,w)
        t = a + i*h
        print "for t"+str(i)," = ", t, ", w  = ", w

def eulerwithy(f,y,a,b,n,alpha):
    output = []
    h = (b-a)/n
    t=a
    w=alpha
    print "for t0  = ", t, ", w1  = ", w, ", y  = ", y(t,w), ", error  = ", abs(w-y(t,w))

    for i in range(1,n+1):
        w = w+ h*f(t,w)
        t = a + i*h
        print "for t"+str(i)," = ", t, ", w  = ", w, ", y  = ", y(t,w), ", error  = ", abs(w-y(t,w))


def p5d():
    euler(lambda t,y: -5*y+5*(t**2)+2*t, 0.0,1.0,10,1.0/3)

def p6d():
    euler(lambda t,y:-t*y + 4*t*(y**(-1)), 0.0,1.0,10,1.0) 

def p10a():
    eulerwithy(lambda t,y:1.0/(t**2) - y/t-y**2,lambda t,y:-1/t,1.0,2.0,20,-1.0)
