#2.1_NOMECLATURA:

message = "Hello World!"; #Em python variáveis podem possuir apenas letras, números e undescores.
message_1 = "Não podemons começar nomes de variáveis com números, como 1_message";
message_2 = "Evite utilizar nomes de funções reservadas para não gerar erros";
message = "Podemos alterar os valores das variáveis a qualquer momento";

#print(message);
message = "Porém será exibido apenas o último valor da variavel definido antes do print"
#print(message);

#As variáveis Python que você está usando no momento devem utilizar
#letras minúsculas. Você não terá erros se usar letras maiúsculas, mas é
#uma boa ideia evitá-las por enquanto.

#2.2 Strings

string_1 = "Isso é uma string";
string_2 = 'Isso é uma string';
#Strings definidas com aspas e apostrofos possuem o mesmo valor
#print(string_1 == string_2)

string_3 = "minha primeira letra é minúscula"
#print(string_3.title()); #mas a função title transforma todas as primeiras letras em maíusculas
#print(string_3.upper()); #A função upper transforma todas as letrar para maiusculas.
#print(string_3.lower()); #A função lower transforma todas as letras para minusculo

#Python usa símbolos de adição para concatenar string
linha_1 = "\n\t essa linha possui parágrafo"
linha_2 = "\n logo após pulamos uma linha"
linha_3 = "E aqui retiramos todos os espaços antes e depois da frase  ";

print(linha_1+linha_2+"\n"+linha_3.strip());