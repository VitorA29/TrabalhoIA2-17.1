%1. Os escritores que escreveram pelo menos um livro e também são professores.
writer(X), professor(X), bookwriter(Y,X).

%2. Os escritores que escreveram pelo menos um livro que possui página na Wikipedia.
writer(X), bookwriter(Y,X), haswikipediaurl(Y,Z).

%3. As construções localizadas na capital da França.
citycapitalofcountry(X,france), city(X), buildinglocatedincity(Y,X).

%4. Os modelos de carro produzidos pelas montadoras que fazem negócios no paises cujas capitais são Berlim ou Tóquio.
country(X), (citycapitalofcountry(berlin,X); citycapitalofcountry(tokyo,X)), automobilemakerdealersincountry(Y,X), automakerproducesmodel(Y,Z).

%5. As capitais dos paises que possuem escola de futebol.
country(X), sportschoolincountry(football, X), citycapitalofcountry(Y, X).

%6. Os nomes das pessoas que possuem pelo menos um filho que fizeram algum comentário sobre bombas em um evento de bombas.
commentatorofbombing(X,Y), bombingevent(Y), person(X), fatherofperson(X,Z), person(Z).

%7. As plantas que representam alguma emoção.
emotion(X), plant(Y), plantrepresentemotion(Y,X).

%8. As pessoas que são menores de idade.
person(X), personhasage(X, Y), Y < 21.

%9. As bebidas que possuem proteínas que causam alguma doença.
beverage(X), beveragecontainsprotein(X,proteins), foodcancausedisease(X,Y).

%10. Os criminosos presos em países de língua portuguesa.
criminal(X), country(Y), languageofcountry(portuguese,Y), criminalarrestedincountry(X,Y).
