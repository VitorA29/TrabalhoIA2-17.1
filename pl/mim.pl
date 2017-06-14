%modelos produzidos pela montadora que faz comercio no pais cuja capital e tokyo.
citycapitalofcountry(tokyo,X),automobilemakerdealersincountry(Y,X),automakerproducesmodel(Y,Z).

%artistas cujo genero musical não e thrash_metal.
musicartistgenre(Y,X),musicgenre(X),\+musicgenressuchasmusicgenres(thrash_metal,X).

%Nome da filha da pessoa que fez comentario de bomba de um evento de bomba.
commentatorofbombing(X,Y),person(X),bombingevent(Y),fatherofperson(X,Z).
