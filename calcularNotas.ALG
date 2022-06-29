Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/06/2022
// aula be mesttra no Youtube youtu.be/kRL-iAjaqz8
Var
NomeAluno: caractere
prova1: real
prova2: real
trabalho1: real
trabalho2: real
diferenca: real
NotaFinal: real
// Seção de Declarações das variáveis 


Inicio
escreva("Digite o seu nome: ")
leia(NomeAluno)
escreva(" Digite a nota do trabalho 1: ")
leia(trabalho1)
escreva(" Digite a nota da prova 1: ")
leia(prova1)
escreva("Digite sua nota do trabalho 2: ")
leia(trabalho2)
escreva("Digite a nota da prova 2: ")
leia(prova2)

NotaFinal <- (trabalho1 + prova1 + trabalho2 + prova2)
diferenca <- (10 - NotaFinal)

escreva("Aluno ", (NomeAluno), " Sua nota é: ", (NotaFinal), " ")
se (NotaFinal >= 6) entao
    escreva(NomeAluno, " você foi aprovado! ")
senao
se (NotaFinal >= 3) e (NotaFinal < 6) entao
     escreva(NomeAluno, " você está de recuperação! ")
  senao
    escreva (NomeAluno, " você foi reprovado! ")
  fimse
 fimse

      

// Seção de Comandos, procedimento, funções, operadores, etc... 


Fimalgoritmo