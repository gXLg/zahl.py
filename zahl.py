*A,L,M,N,O,P,B,G,g,t,k="drei vier fünf sech sieb acht neun zehn elf zwölf sept quin ing okt qua nm non tre en quadr".split()
F,H,n,o,C,U,m,j="engo saz"
I,S="",10;Q=S*S;T=Q*S
l=*[H+U]*3,H,H,"mx",I,I
Y=["null","ein","zwei"]+A*S
Y[6]+=U;Y[7]+=t
def Z(q,r=I):
 a=abs(q);d,u=a//T,1;s=Y[b:=a%Q]*(a<S)or Z(d%T,"tausend")+Z(a//Q%S,"hundert")+[Z(a%S,"und")+["zwan",*A][x:=b//S-2]+"zß"[x==1]+"ig",Y[b]*(b>0)+Y[S]*(b>12)][x<0]
 while d:
  d//=T;u+=1;V,v=u//2,I
  while V:c,e,h=V//S%S,V//Q%S,[*"nmb","tr",k,M+"t","sext",L,O,G,I,"un","duo",g,P+"ttuor",M,U+F,L+F,O+o,"nove",I,I,I,U,I,I,"x",B,I,B][V%S::S];f,y=[[I,H,"ms",*l,"dezi","viginti","tri",k+m,M+P,"sexa",L+"ua",O+o,G+m],i:=[I,"nxs",H,*l,j,"duz",g+j,k+N,M+n,"sesz",L+N,O+N,G+n][e:]][c<1][c::S];v=h[y>I]+(I.join({*h[2]}&{*f})+y+"ginta"*(c>2)+i[S]*(c>0)+"enti"*(e>0))[:-1]+"illi"+v;V//=T
  s=Z(p:=d%T,F*(p<2)+C+v.title()+[o+H,"arde"][u%2]+t[u%2:]*(p>1)+C*(s>I))+s
 s="minus "*(q<0)+s+U[a==1!=r>I:b==1];x=r<C;return(s[:x].upper()+s[x:]+r)*(a>-x)
zahl=Z
