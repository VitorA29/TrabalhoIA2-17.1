rel(o1,p1,s2).
rel(o2,p2,s4).
rel(o3,p2,s1).
rel(o7,p5,s5).
rel(o9,p1,s4).
rel(o2,p6,s7).
rel(o3,p3,s2).
rel(o6,p6,s3).
rel(o5,p7,s2).
rel(o4,p2,s1).
rel(o3,p3,s1).

go(X,Y):-(\+(X=Y)),write(X),write(":1e: "),rel(X,Z,_),write(Z),write(":1r: "),rel(Y,Z,_),write(Y),write(":1e: "),!.
go(X,Y):-write(X),write(":2e: "),rel(X,Z,V),write(Z),write(":2r: "),write(V),write(":2v: "),rel(Y,W,V),write(W),write(":2r: "),write(Y),write(":2e: "),!.
go(X,Y):-write(X),write(":3e: "),rel(X,Z,_),write(Z),write(":3r: "),rel(W,Z,_),write(W),write(":3e: "),go(W,Y),!.
go(X,Y):-write(X),write(":4e: "),rel(X,_,V),write(V),write(":4v: "),rel(W,_,V),write(W),write(":4e: "),go(W,Y).
