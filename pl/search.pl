go(X,Y):-write(X),write(":1e: "),rel(X,Z,_),write(Z),write(":1r: "),rel(Y,Z,_),write(Y),write(":1e: "),!.
go(X,Y):-write(X),write(":2e: "),rel(X,Z,V),write(Z),write(":2r: "),write(V),write(":2v: "),rel(Y,W,V),write(W),write(":2r: "),write(Y),write(":2e: "),!.
go(X,Y):-write(X),write(":e: "),rel(X,Z,K),write(Z),write(":r: "),write(K),write(":v: "),rel(W,M,K),write(M),write(":r: "),write(W),write(":e: "),go(W,Y).
