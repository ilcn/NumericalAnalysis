def p5a():
  xs = [-.75, -0.5,-0.25,0]
  fxs = [-.0718125, -.02475, .3349375, 1.101]
  getdd123(xs,fxs,3)
 
def getdd123(xs,fxs,n):  
#derivatives
  l1stdd = []
  l2nddd = []
  l3rddd = []
  for i in range(0,n):
    l1stdd.append((fxs[i+1]-fxs[i])/(xs[i+1]-xs[i]))
  for i in range(0,n-1):
    l2nddd.append((l1stdd[i+1]-l1stdd[i])/(xs[i+2]-xs[i]))
  for i in range(0,n-2):
    l3rddd.append((l2nddd[i+1]-l2nddd[i])/(xs[i+3]-xs[i]))
  #print [l1stdd,l2nddd,l3rddd] 
  return [l1stdd,l2nddd,l3rddd] 

def p7a():
  xs = [-.1, 0,.2,.3]
  fxs = [5.3, 2, 3.19, 1]
  getdd123(xs,fxs,3)

def p14():
  xs = [0, .25,.5,.75]
  fxs = [1, 2, 3.5, 6]
  getdd123(xs,fxs,3)
