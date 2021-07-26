# Gerador_de_Senhas
Projeto: Gerador de Senhas

Este programa serve para usuários que querem senhas fortes, dificeis de serem quebradas, para usar em seus sites e redes sociais, com mais segurança.

O programa irá criar oito senhas aleatórias com oito dígitos cada, toda vez que for rodado. Nelas irá conter números de 0 a 9, sinais de pontuação e letras de A a Z maiúscula e minúsculas.

Sua estrutura:  Foi necessário a importação da biblioteca random para gerar números pseudoaleatórios, depois houve a criação das variáveis carac e compr e definiu-se os itens contidos nela.
               O uso da estrutura de repetição for i in range, para que a repetição sequencial da senha esteja de acordo com o número de vezes que foi informado.
               No final do código a variável "senha" é definida. E houve também a utilização de .join que serve para unir as variáveis carac e compr, e random.sample para que retorne dessas variáveis uma lista de certo tamanho contendo itens escolhidos da sequência. 
               Então quando roda o código, é imprimido na tela oito senhas com oito caracteres. As senhas são diferentes a cada vez que o programa é rodado.
