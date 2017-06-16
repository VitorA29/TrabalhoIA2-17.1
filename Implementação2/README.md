<<<<<<< HEAD
# Tabelas
Todas as bases de conhecimento que extraímos em Prolog, e que as consultas serão feitas.

## Compilador
[YAP COMPILER](https://www.dcc.fc.up.pt/~vsc/Yap/)

### questions
Consultas que serão realizadas na base de dados.

### rneg
Negações das relações.

### fneg
Negações dos fatos.

### fpos
Fatos.

### rpos
Relações.
=======
# Segunda implementação.

A segunda implementação, foi elaborada uma query de busca de relação entre entidades. Foi feita uma ferramente que formaliza a knowledge base, onde a partir do .csv de entrada foi gerado o arquivo rpos.pl, formalizando a knowledge base em uma tupla de 3 informações. Tais informações foram definidas como (entidade, relação, valor). A busca foi elaborada baseada na ideia do caso base, que são entidades ligadas pela mesma relação ou elas estarem ligadas pelo mesmo valor. A busca então olha as ligações entre a primeira entidade e uma outra entidade que possuem uma relação em comum ou um valor em comum, fazendo a ligação da nova entidade com a entidade de destino.
>>>>>>> 77885854c78334f15e8254909aa44a8e7785a609
