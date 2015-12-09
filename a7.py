import math

#p280
def taylororder2(f,fpt,fpy,a,b,h,alpha):
    t = a
    w = alpha
    print "ti  wi: "
    n = int((b-a)/h)
    for i in range(1,n+1):
        w = w + h*f(t,w)+ (h**2)*0.5*(fpt(t,w)+fpy(t,w)*f(t,w))
        t = a+ i*h
        print t,w

def p2801d():
    taylororder2(lambda t,y: math.cos(2*t)+math.sin(3*t),lambda t,y:-2*math.sin(2*t)+3*math.cos(3*t),lambda t,y: 0, 0,1.0,0.25,1.0)

def trial():
    taylororder4(lambda t,y: y-t**2+1,lambda t,y:y - t**2 +1 - 2* t, lambda t,y:y - t**2-2*t-1, lambda t,y:y-t**2-2*t-1, 0,2,.2,.5)

def p2802b():
    taylororder2(lambda t,y:(1+t)/(1+y), lambda t,y: (1+y)**(-1), lambda t,y: -(1+t)*(1+y)**(-2),1.0,2.0,0.25,2.0)

def taylororder4(f,fp,fpp,fppp,a,b,h,alpha):
    t = a
    w = alpha
    print "ti wi: "
    n = int((b-a)/h)
    for i in range(1,n+1):
        w = w + h*(f(t,w)+0.5*h*fp(t,w)+h**2*fpp(t,w)/6+h**3*fppp(t,w)/24)
        t = a+ i*h
        print t,w

def p2803c():
    taylororder4(lambda t,y:1+y/t,lambda t,y:1/t, lambda t,y:-1/t**2, lambda t,y:2/t**3, 1,2,.25,2)

#p291
def modifiedeuler(f,factual,a,b,h,alpha):
    t =a
    w = alpha
    print "t w y: " 
    n = int((b-a)/h)
    for i in range(1,n+1):
        tnext = a + i*h
        w = w + 0.5 * h * (f(t,w) + f(tnext,w+ h* f(t,w)))
        t = tnext
        print t,w,factual(t)

def p2911b():
    modifiedeuler(lambda t,y: 1+ (t-y)**2,lambda t:t + 1/(1-t), 2,3,.5,1)

def p2913a():
    modifiedeuler(lambda t,y: y/t - (y/t)**2, lambda t: t/(1+math.log(t)), 1,2,.1,1)

def rkorder4(f,factual,a,b,h,alpha):
    t = a
    w = alpha
    print "t w y: "
    n = int((b-a)/h)
    for i in range(1,n+1):
        k1 = h*f(t,w)
        k2 = h*f(t+h/2, w+k1/2)
        k3 = h*f(t+h/2, w+k2/2)
        k4 = h*f(t+h, w+k3)
        w = w + (k1+2*k2+2*k3+k4)/6
        t = a+i*h
        print t,w,factual(t)

def p29113b():
    rkorder4(lambda t,y: 1+ (t-y)**2,lambda t:t + 1/(1-t),2,3,.5,1)
