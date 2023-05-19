print("Bem-vindo ao Jogo da Forca! \nTema: Escola")
from random import choice # o random pertence ao pacote do proprio python 

with open('palavras.txt') as arquivo:
  linhas = arquivo.read() #aqui usamos o 'read' para ele ler o arquivo
  lista_de_palavras = linhas.split('\n') #O 'spli' é usado para dividir uma string em pequenos pedaços.  
#criamos uma lista. Uma lista que está separada por quebras de linhas do arquivo palavras, fazendo com que essas linhas sejam elementos de uma lista.  
  
  
#'with' usamos para importar palavras.txt e chamamos ele de 'arquivo' , o que eu passo depois do 'as' é o nome da variavél que vai receber o valor


#Usamos o while para ficar pedindo ao usuário as letras - a condição para encerrar o programa é quando o usuário ganhar o jogo ou peder. 

#o for vai percorrer cada letra da 'palavra',  então para cada letra(item) dentro da palavra, ele vai comparar se letra está dentro da palavra. 

#mostramos na tela o underscore _ _ _ de acordo com o len

#Jogo da Forca com Python | Listas, strings, for e while

palavra = choice(lista_de_palavras).upper() #Upper deixa a letra maiúscula / para escolher a palavra de forma aleatoria usamos o metodo 'choice'

forca = """
|--|
|  |
|

"""
vazio = """

"""
cabeca = """
    O
"""
tronco = """
    O
    |
"""

braco_esquerdo = """
    O
   /|
"""

braco_direito = """
  O
 /|\\
 
"""

perna_direita = """
   O
  /|\\
  /
""" #usamos duas barras 

perna_esquerda = """
   O
  /|\\
  / \\

"""

#Colocamos as partes do corpo dentro de uma lista
chances_do_boneco = [vazio, cabeca, tronco, braco_esquerdo, braco_direito, perna_direita, perna_esquerda]

acertos = 0
erros = 0
letras_ok = '' #armazenar e mostrar ao us. as letras acertdas
letras_not = '' #armazenar letras errdas

while acertos != len(palavra) and erros != 7: #len mede o comprimento da string 
  mensg = '' #underscore
  for letra in palavra: 
    if letra in letras_ok: 
       mensg += letra + ' ' #espaço #mensg += f'{letra} ' - outra forma 
    else:
        mensg += '_ '   
  print(forca+chances_do_boneco[erros]) 
  print(mensg)#imprime o desenho da forca e a lista "chances", passando a posição[indice] com o número de erros.  "O programa pega a lsita 'chances', pega o valor da variável 'erros''
 
  
  letra = input("Digite a letra: ").upper() #recebendo e pedindo novamente a letra

  if letra in letras_ok+letras_not:#Aqui estamos somando duas strings para apenas uma string
    print("Você já tentou essa letra ")
    continue #'continue' usado para interromper a execução do while (No caso) e volta para o while. 
    
#Além da letra existir na palavra, precisamos verificar se essa letra já foi acertada e errada . Por isso usamos o if.
  
  if letra in palavra: 
       print("Você acertou a letra")
       letras_ok = letras_ok + letra 
       acertos += palavra.count(letra) #O count vai contar quantas vezes na vaqriavél palavra existe o caractere, então quando digitamos uma letra que existe mais de uma vezes, pontuamos essa letra mais de uma vez. 
  else:
   print("Você errou a letra")
   letras_not = letras_not + letra
   erros+=1
    