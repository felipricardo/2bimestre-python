'''
Faça um único programa na linguagem Python para calcular 
o lucro que um salão de festas tem durante um mês de funcionamento. 
Considere que o salão de festas funciona apenas aos sábados e domingos, 
portanto abre apenas 8 vezes em um mês, e todas as noites sempre acontece um evento. 

Para cada evento (utilizando bloco(s) de repetição) solicite as seguintes informações: (2.0)
a. O dia no mês em que vai acontecer o evento;
b. O número de pessoas que estarão no evento;
 
Calcule e mostre:
a. Considerando a tabela abaixo, defina e mostre o valor da locação. (2.0)
+----------------------------------+--------------------+
| Número de pessoas                | Valor da locação   |
+----------------------------------+--------------------+
| Caso não ultrapasse 1000 pessoas |    R$ 4500,00      |
+----------------------------------+--------------------+
|  Caso ultrapasse 1000 pessoas    |  R$ 5,00 reis      |
|                                  |  por pessoa        |
+----------------------------------+--------------------+

b. Qual a média do valor da locação (considerando todas as locações). (2.0)

c. Quantos eventos não ultrapassaram 1000 pessoas? (2.0)

d. Qual o dia do mês onde ocorreu o evento com o maior número de pessoas, 
e qual o dia do mês onde ocorreu o evento com o menor número de pessoas.(2.0)
'''

vallocacaomenor = 0
vallocacaomaior = 0
valtotal = 0
eventosmenor1000 = 0
omaiorevento = 0
maiordiames = 0
omenorevento = 0
menordiames = 0

for i in range(8):
    print("Evento Nº", i+1)
    print("O dia do mês vai acontecer o evento: ")
    diames = int(input())
    print("Digite o número de pessoas que vão estar no evento: ")
    numpessoas = int(input())

    if numpessoas <= 1000:
        print("O valor da locação é de R$4500")
        vallocacaomenor += 4500
        eventosmenor1000 += 1
    else:
        vallocacaomaior = numpessoas * 5
        print("O valor da locação é de R$", vallocacaomaior)
    valtotal += vallocacaomenor + vallocacaomaior

    if numpessoas > omaiorevento:
        omaiorevento = numpessoas
        maiordiames = diames
    #separar omaior e omenor
    if i == 0:
        omenorevento = numpessoas
        menordiames = diames
    if numpessoas < omenorevento:
        omenorevento = numpessoas
        menordiames = diames

mediatotal = valtotal / 8
print("A média total das locações é de R$", mediatotal)
print("O número de eventos que não ultrapassaram 1000 pessoas foi:", eventosmenor1000, "eventos")
print("O dia do evento com o maior número de pessoas foi o dia", maiordiames)
print("O dia do evento com o menor número de pessoas foi o dia", menordiames)