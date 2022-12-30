from random import randint, choice
from time import sleep
import os

nomes = ['Lucas', 'Jose', 'Maria', 'Bernado', 'Souza'];
emails = ['lucas@gmail.com', 'ronaldo@gmail.com', 'sidinei@gmail.com', 'roberto@gmail.com', 'timas@gmail.com'];
telefones = ['5599984324146', '5599987895141', '5599984321237', '5599984374312', '5599983325166'];
cidades = ['Olinda', 'Salvador', 'Belo Horizonte', 'Jundiai', 'Campinas'];
estados = ['São Paulo', 'Rio de janeiro', 'Pernambuco', 'Minas Gerais', 'Brasilia'];
statusLoop = '';



print('Bem-vindo ao Gerador de Dados de teste - Para finalizar, digite "parar"');
print('-------------------------------------------');



while statusLoop != 'parar':
    print("----------------------------");
    print('Escolha uma ou mais opções abaixo a serem geradas aleatóriamente');
    print('[1] - Nome');
    print('[2] - E-mail');
    print('[3] - Telefone');
    print('[4] - Cidades');
    print('[5] - Estados');
    
    opcoes = input('Digte um(as) opções separada por virgulas / sem espaços: ');
    print('')

    if opcoes != 'parar':
        listaOpcoes = opcoes.split(',');
    else:
        break
    
    for opcao in listaOpcoes:
        indice = randint(0, 4)
        
        if opcao == '1':   
            print(nomes[indice]);
            with open('dados.txt', 'a', newline='',) as dados:
                dados.write(nomes[indice] + os.linesep);
            
        
        if opcao == '2':
            print(emails[indice]);
            with open('dados.txt', 'a', newline='') as dados:
                dados.write(emails[indice] + os.linesep);

        if opcao == '3':
            print(telefones[indice]);
            with open('dados.txt', 'a', newline='') as dados:
                dados.write(telefones[indice] + os.linesep);

        if opcao == '4':
            print(cidades[indice]);
            with open('dados.txt', 'a', newline='') as dados:
                dados.write(cidades[indice] + os.linesep);

        if opcao == '5':
            print(estados[indice]);
            with open('dados.txt', 'a', newline='') as dados:
                dados.write(estados[indice] + os.linesep);


    print('ALERTA - CONFIRME NO ARQUIVO');
    sleep(5)
    os.system("cls");