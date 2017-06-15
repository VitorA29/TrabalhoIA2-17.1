# Segundo trabalho da disciplina de Inteligência Artificial 2017.1.

## Realizar consultas em uma base de dados.
Base de dados usada: [NELL](https://pt.wikipedia.org/wiki/Minimax).

Compilador usado: [YAP COMPILER](https://www.dcc.fc.up.pt/~vsc/Yap/).

## Grupo
- Max Fratane.
- Erick Grilo.
- Vitor Araújo.
- Vitor Lourenço.

## Consultas

- Os escritores que escreveram pelo menos um livro e também são professores.
``` prolog
writer(X), professor(X), bookwriter(Y,X).
```

- Os escritores que escreveram pelo menos um livro que possui página na Wikipedia.
``` prolog
writer(X), bookwriter(Y,X), haswikipediaurl(Y,Z).
```

- As construções localizadas na capital da França.
``` prolog
citycapitalofcountry(X,france), city(X), buildinglocatedincity(Y,X).
```

- Os modelos de carro produzidos pelas montadoras que fazem negócios no paises cujas capitais são Berlim ou Tóquio.
``` prolog
country(X), (citycapitalofcountry(berlin,X); citycapitalofcountry(tokyo,X)), automobilemakerdealersincountry(Y,X), automakerproducesmodel(Y,Z).
```

- As capitais dos paises que possuem escola de futebol.
``` prolog
country(X), sportschoolincountry(football, X), citycapitalofcountry(Y, X).
```

- Os nomes das pessoas que possuem pelo menos um filho que fizeram algum comentário sobre bombas em um evento de bombas.
``` prolog
commentatorofbombing(X,Y), bombingevent(Y), person(X), fatherofperson(X,Z), person(Z).
```

- As plantas que representam alguma emoção.
``` prolog
emotion(X), plant(Y), plantrepresentemotion(Y,X).
```

- As pessoas que são menores de idade.
``` prolog
person(X), personhasage(X, Y), Y < 21.
```

- As bebidas que possuem proteínas que causam alguma doença.
``` prolog
beverage(X), beveragecontainsprotein(X,proteins), foodcancausedisease(X,Y).
```

- Os criminosos presos em países de língua portuguesa.
``` prolog
criminal(X), country(Y), languageofcountry(portuguese,Y), criminalarrestedincountry(X,Y).
```
