#principal
def main():
  notas = {}
  usuario = input('Olá! Qual o seu nome?').title()
  while True:
    escolha = menu()
    if escolha == 1:
      cadastro_alunos(notas)
    elif escolha == 2:
      estatistica(notas)
    elif escolha == 3:
      ordenar_alunos(notas)
    elif escolha == 4:
      printar_notas(notas)
    elif escolha == 0:
      print(f'Fim do programa, obrigado {usuario}!')
      break
    else:
      print('Opção inválida!')


#menu
def menu():
  print('''
1.Cadastrar alunos e suas notas
2.Calcular estatísticas(média, maior e menor nota)
3.Ordenar alunos por nome ou nota
4.Carregar os dados salvos
0.Sair
''')
  try:
    return int(input('Insira uma das opções acima:'))
  except ValueError:
    print('Insira um número válido')
    return None

#Cadastro notas
def cadastro_alunos(notas):
  while True:
      nome = input('Insira o nome do aluno: ').title()
      if not nome:
        print('Insira um nome válido')
        continue
      valido = True
      for letra in nome.split():
        if not letra.isalpha():
          print('Insira um nome válido')
          valido = False
          break
      if not valido:
        continue
      try:
        nota = float(input('Insira a nota do aluno'))
      except ValueError:
        print(f'Insira a nota do aluno {nome}')
        continue
      notas[nome] = nota
      while True:
        continua = input('Deseja continuar? Y/N').upper()
        if continua not in ('Y','N'):
          print('Insira Y ou N')
        else:
          break
      if continua == 'Y':
        continue
      else:
        while True:
          salvar = input('Deseja salvar os dados? Y/N').upper()
          if salvar not in ('Y','N'):
            print('Insira Y ou N')
          else:
            break
      if salvar == 'Y':
        guardar_notas(notas)
        print('Dados salvos com sucesso')
        print('Voltando ao menu')
        break
      else:
        print('Voltando ao menu')
        break

#estatisticas
def estatistica(notas):
  print('''
  1. Calcular média
  2. Maior nota
  3. Menor nota
  0. Voltar ao menu
  ''')
  while True:
    try:
      escolha = int(input('Insira uma das opções acima.'))
    except ValueError:
      print('Insira um número válido')
      continue
    if escolha == 1:
      media = sum(notas.values())/len(notas.values())
      print(f'A média das notas é {media:.2f}')
    elif escolha == 2:
      maior_nota = max(notas.values())
      alunos_maior_nota = [nome for nome,nota in notas.items() if nota == maior_nota]
      print(f'A maior nota da turma é {maior_nota:.2f} e os alunos {alunos_maior_nota} a tiraram')
    elif escolha == 3:
      menor_nota = min(notas.values())
      alunos_menor_nota = [nome for nome, nota in notas.items() if nota == menor_nota]
      print(f'A menor nota da turma é {menor_nota:.2f} e os alunos {alunos_menor_nota} a tiraram')
    elif escolha == 0:
      print('Voltando ao menu')
      break
    else:
      print('Escolha um número válido')

#ordenação
def ordenar_alunos(notas):
  print('''
  1. Ordenar por nome
  2. Ordenar por nota
  0. Voltar ao menu
  ''')
  while True:
    try:
        escolha = int(input('Insira uma das opções acima.'))
        if escolha == 1:
          for nome, nota in sorted(notas.items()):
            print(f'{nome}: {nota}')
        elif escolha == 2:
          for nome, nota in sorted(notas.items(), key=lambda i:i[1], reverse = True):
            print(f'{nome}: {nota}')
        elif escolha == 0:
          print('Voltando ao menu')
          break
        else:
          print('Escolha um número válido')
    except ValueError:
      print('Insira um número válido')

#guardando arquivos
def guardar_notas(notas):
  import json
  with open('notas.json','w') as arquivo:
    arquivo.write(json.dumps(notas))


#lendo arquivos
def ler_notas(notas):
  import json
  with open('notas.json','r') as leitura_arquivo:
    texto = leitura_arquivo.read()
    dados = json.loads(texto)

#printando arquivos
def printar_notas(notas):
  import json
  with open('notas.json','r') as leitura_arquivo:
    texto = leitura_arquivo.read()
    dados = json.loads(texto)
  print('Dados salvos no arquivo:')
  print(dados)


#Chamando o programa
main()

