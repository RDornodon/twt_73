for I in[I:=input]*int(I()):L=int(I());A=abs;G=L//2;X={'L':(0,L-1),'R':(G-1,G),'U':(0,G-1),'D':(G,L-1)}[I()];D=I()+I()[::-1];U=D.index('2');Q=[(B:=-A(A(i-U)-G)+G,B-A(A(i-x)-G)+G)[::-1]for i in range(L)for x in X if'1'==D[i]];print(min(Q)[1])