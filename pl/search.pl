go(X,Y):-(\+(X=Y)),write(X),write(":e:\n"),rel(X,Z,_),write(Z),write(":r:\n"),rel(Y,Z,_),write(Y),write(":e:\n"),!.
go(X,Y):-write(X),write(":e:\n"),rel(X,Z,V),write(Z),write(":r:\n"),write(V),write(":v:\n"),rel(Y,W,V),write(W),write(":r:\n"),write(Y),write(":e:\n"),\+(X=Y),!.
go(X,Y):-write(X),write(":e:\n"),rel(X,Z,K),write(Z),write(":r:\n"),write(K),write(":v:\n"),rel(W,M,K),write(M),write(":r:\n"),write(W),write(":e:\n"),go(W,Y).
