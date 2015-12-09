import math

def rkforsystems(flist,a,b,alphalist,h):
    m = len(flist)
    n = int((b-a)/h)
    t = a
    ws = list(alphalist)
    ws.insert(0,t)
    print m,n
    print ws
    for i in range(1,n+1):
#note that the functions should take in a list as the single parameter. 
#kxtransforms are for modifing the input
        k1s = [h*flist[j](ws) for j in range(m)]
        k2s = [h*flist[j](ktransform(ws,k1s,h,2)) for j in range(m)]
        k3s = [h*flist[j](ktransform(ws,k2s,h,3)) for j in range(m)]
        k4s = [h*flist[j](ktransform(ws,k3s,h,4)) for j in range(m)]
        ws = [ws[j]+(k1s[j]+2*k2s[j]+2*k3s[j]+k4s[j])/6 for j in range(m)]  
        ws.insert(0, a + i*h)
        print ws

def ktransform(ws,ks,h,num):
    ws = list(ws)
    ks = list(ks)
    ks.insert(0,h)
    for i in range(len(ws)):
        if num==4: ws[i] = ws[i]+ks[i]
        else: ws[i] = ws[i] + 0.5*ks[i]
    return ws

def p3371a():
    flist=[lambda fl: 3*fl[1] + 2*fl[2] - (2*(fl[0])**2 + 1)*math.exp(2*fl[0])]
    flist.append(lambda fl: 4*fl[1] + fl[2]+(fl[0]**2 + 2* fl[0] - 4)*math.exp(2*fl[0]))
    rkforsystems(flist,0,1,[1,1],0.2)

def trial():
    u1 = lambda fl: -4 * fl[1] + 3* fl[2] + 6
    u2 = lambda fl:-2.4 * fl[1] + 1.6*fl[2]+3.6
    rkforsystems([u1,u2],0,0.5,[0,0],0.1)
