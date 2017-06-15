rel(o1, p1, s2).
rel(o2, p2, s4).
rel(o3, p2, s1).
rel(o7, p5, s5).
rel(o9, p1, s4).
rel(o2, p6, s7).
rel(o3, p3, s2).
rel(o6, p6, s3).
rel(o5, p7, s2).
rel(o4, p2, s1).
rel(o3, p3, s1).

go(X,Y):-(\+(X=Y)),write(X),write(":e: "),rel(X,Z,_),write(Z),write(":r: "),rel(Y,Z,_),write(Y),write(":e: "),!.
go(X,Y):-write(X),write(":e: "),rel(X,Z,V),write(Z),write(":r: "),write(V),write(":v: "),rel(Y,W,V),write(W),write(":r: "),write(Y),write(":e: "),\+(X=Y),!.
go(X,Y):-write(X),write(":e: "),rel(X,Z,K),write(Z),write(":r: "),write(K),write(":v: "),rel(W,M,K),write(M),write(":r: "),write(W),write(":e: "),go(W,Y).
