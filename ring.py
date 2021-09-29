class R:
    def __init__(s,u,x,b,r):s.u=u;s.x=x;s.b=b;s.r=r
for I in'*'*int(input()):
    L=int(input());X={'L':(0,L),'R':(l:=L//2,l+1),'U':(0,l),'D':(l+1,L)}[input()]
    Q=[R(c==2,i in X,c==1,(~-i%L,-~i%L))for i,c in enumerate(map(int,input()+input()[::-1]))]
def F(Q):
    pass
