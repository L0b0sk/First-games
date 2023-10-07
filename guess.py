import random


def jogar():
    print("*******************************************************************************************************************************************************************************")
    print ("*******************************************************************************************************************************************************************************")
    print ("************************************************************************ Welcome to guessing game *****************************************************************************")
    print ("*******************************************************************************************************************************************************************************")
    print("*******************************************************************************************************************************************************************************")
    ##
    ##
    ##  the entire project was done in Portuguese, with exception of the texts that will be shown on the terminal
    ##
    ##  2(##) inicio do raciocinio e 1(#) pular a linha para dixar mais organizado 3(###)para codigos que podem ser usados
    ##                                                                                   mas foram substituidos sintaxe melhores
    ##
    ##


    numero_secreto = random.randrange(1,101)                                     ##adicionei um valor numerico aleatorio para "Numero_secreto"
    total_de_tentativas = 0                                                                 ##adicionei um valor numerico para "total_de_tentativas"
    ###rodada = 1                                                                           ##adicionar um valor numerico para "rodada"
    pontos = 1000

    print ("What difficulty you want to play?")
    print ("(1) Easy (2) Medium (3) Hard")

    nivel = int(input("Chose the difficulty: "))                                            ##input para poder ecolher a dificuldade do jogo

    if (nivel == 1):                                                                        ##se o nivel selecionado for "X" o numero de tentativas e "Y"
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    ###while(rodada <= total_de_tentativas)                                                 ## a funcao while funciona para, enquanto a a variavel total de tentativas nao for
                                                                                            # menor ou igual a variavel rodadas
    for rodada in range (1, total_de_tentativas + 1):                                       ##literalmente falando, para rodada foi implementado um raio
                                                                                            # que vai de 1 ate o numero  de tentativas
        print("Guess {} of {}". format(rodada, total_de_tentativas))                  ## {} serve para colocar o valor inserido
                                                                                            # pela funcao format, que dentro dos parenr=teses tem o valor que vai ser colocado
                                                                                            # dentro dos colchetes
        chute_str = input("Enter a number between 1 to 100: ")                              ##coloquei o input para que, alem de escrever o texto,
                                                                                            # no console eu consiga digitar o valor que eu quiser
        print("You typed", chute_str)                                                       ##vai escrever o texto mais o valor colocado no item acima
        chute = int(chute_str)                                                              ##vaiatribuir o valor do imput acima a palavra "chute" e deixar em valor sem ser decimal

        if (chute < 1 or chute > 100):                                                      ##se o chute dfor menor que 0 ou maior que 100
            print ("You must type a number between 1 to 100!")                              ##vai ser impresso a mensagem
            continue                                                                        ##e o jogo vai continuar de onde parou


        acertou = chute == numero_secreto                                                   ## criei uma variavel onde ao invez de ter que ficar colocando o valor varias vezes
                                                                                            # posso simplemente colocar "acertou" que ja vai valer por essa linha inteira
        maior   = chute > numero_secreto                                                    ## o mesmo vale para esse valor que agora durante o codigo posso apenas substituir por "maior"
        menor   = chute < numero_secreto                                                    ## o mesmo vale para esse apenas trocando por "menor"

        if(acertou):                                                                        ##auto intuitivo, se acertou entao vai escrever a mensagem de acerto
            print("You got it right!!! you scored {} points".format(pontos))
            break                                                                           ##breake e usado para encerar o programa assim que o numero secreto for adivinhado

        else:                                                                               ##se nao vai para a variavel a baixo
            if(maior):                                                                      ## se o valor for maior ent vai escrever
                print("your guess was higher than the secret number")
            elif(menor):                                                                    ##ainda assim nao for o valor do if vai ler o "elif"
                print("your guess was lower than the secret number")
            pontos_perdidos = abs(numero_secreto - chute)                                   ##aqui a pontuacao vai aparecer com o calculo onde a pontuacao e
                                                                                            # o numero secreto - o valor chutado, e a funcao "abs" funciona para idependente se o numero
                                                                                            #for negativo ou positivo, ele apareca positivo
            pontos = pontos - pontos_perdidos

    ###rodada = rodada + 1                                                                  ## para cada rodada que caontecer, vai ser adicionado +1 para a
                                                                                            # contagem de rodadas

    print("End of the game")

if(__name__ == "__main__"):
    jogar()