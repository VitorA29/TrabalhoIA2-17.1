rel(jude_the_obscure,bookwriter,thomas_hardy).
rel(animal_farm,bookwriter,orwell).
rel(animal_farm,bookwriter,george_orwell).
rel(nineteen_eighty_four,bookwriter,orwell).
rel(nineteen_eighty_four,bookwriter,george_orwell).
rel(tess_of_the_d_urbervilles,bookwriter,thomas_hardy).
rel(dune,bookwriter,frank_herbert).
rel(a_farewell_to_arms,bookwriter,ernest_hemingway).
rel(alice_in_wonderland,bookwriter,lewis_carrol).
rel(artemis_fowl,bookwriter,eoin_colfer).
rel(world_cup,sportsgameteam,brazil).
rel(skiing,sportusesequipment,orwell).
rel(skiing,sportusesequipment,equipment).
rel(sports,sportusesequipment,skis).
rel(ski,sportusesequipment,skis).

go(X,Y):-(\+(X=Y)),write(X),write(":e: "),rel(X,Z,_),write(Z),write(":r: "),rel(Y,Z,_),write(Y),write(":e: "),!.
go(X,Y):-write(X),write(":e: "),rel(X,Z,V),write(Z),write(":r: "),write(V),write(":v: "),rel(Y,W,V),write(W),write(":r: "),write(Y),write(":e: "),\+(X=Y),!.
go(X,Y):-write(X),write(":e: "),rel(X,Z,K),write(Z),write(":r: "),write(K),write(":v: "),rel(W,M,K),write(M),write(":r: "),write(W),write(":e: "),go(W,Y).
