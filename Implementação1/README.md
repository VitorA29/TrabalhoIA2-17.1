# Primeira implementação.

Primeira implementação do trabalho. 
Foi a nossa primeira interpretação, talvez errônea, do enunciado do trabalho.
Basicamente, escrevemos consultas sobre a base de dados.

Para a execução das consultas, consulte o consult-me.pl, usando o YAP.
Em seguida, execute alguma das consultas a seguir.

## pl 
Possui os arquivos .pl com a nossa knowledge base.
O arquivo questions.pl possui as perguntas que serão realizadas sobre a KB.

## py-parser
Parser feito em python para gerar a KB a partir do arquivo ,csv.

## Consultas

1. Os escritores que escreveram pelo menos um livro e também são professores.
``` prolog
writer(X), professor(X), bookwriter(Y,X).
``` 

2. Os escritores que escreveram pelo menos um livro que possui página na Wikipedia.
``` prolog
writer(X), bookwriter(Y,X), haswikipediaurl(Y,Z).
``` 
3. As construções localizadas na capital da França.
``` prolog
citycapitalofcountry(X,france), city(X), buildinglocatedincity(Y,X).
``` 

4. Os modelos de carro produzidos pelas montadoras que fazem negócios no paises cujas capitais são Berlim ou Tóquio.
``` prolog
country(X), (citycapitalofcountry(berlin,X); citycapitalofcountry(tokyo,X)), automobilemakerdealersincountry(Y,X), automakerproducesmodel(Y,Z).
``` 

5. As capitais dos paises que possuem escola de futebol.
``` prolog
country(X), sportschoolincountry(football, X), citycapitalofcountry(Y, X).
``` 

6. Os nomes das pessoas que possuem pelo menos um filho que fizeram algum comentário sobre bombas em um evento de bombas.
``` prolog
commentatorofbombing(X,Y), bombingevent(Y), person(X), fatherofperson(X,Z), person(Z).
``` 

7. As plantas que representam alguma emoção.
``` prolog
emotion(X), plant(Y), plantrepresentemotion(Y,X).
``` 

8. As pessoas que são menores de idade.
``` prolog
person(X), personhasage(X, Y), Y < 21.
``` 

9. As bebidas que possuem proteínas que causam alguma doença.
``` prolog
beverage(X), beveragecontainsprotein(X,proteins), foodcancausedisease(X,Y).
``` 

10. Os criminosos presos em países de língua portuguesa.
``` prolog
criminal(X), country(Y), languageofcountry(portuguese,Y), criminalarrestedincountry(X,Y).
