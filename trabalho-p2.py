import json #Importando o JSON

#Colocar verificação no nome do usuário
#Colocar verificação de nota entre 0 e 10


#principal
def main(): #Definindo a função principal
  notas = {} #Definindo a variável notas como um dicionário vazio
  print("\n******************* Sistema de notas - UERJ *******************") #Mensagem de boas vindas
  print('Olá, professor(a) seja bem vindo(a) ao sistema de gerenciamento de notas da UERJ') #Mensagem de boas vindas
  usuario = input('Qual o seu nome?').title() #Para personalizar o uso do sistema pelo usuário
  if not usuario:
    return 'Insira um nome válido.'
  while True: #Loop da fuñção principal
    escolha = menu() #Chamando a função 'menu()'
    if escolha == 1:
      cadastro_alunos(notas) #Chamando a função de cadastro de alunos
    elif escolha == 2:
      estatistica(notas) #Chamando a função de estatística
    elif escolha == 3:
      ordenar_alunos(notas) #Chamando a função de ordenação de alunos
    elif escolha == 4:
      dados_carregados = ler_notas() #Chamando a função para printar os dados do arquivo json
      if dados_carregados: #Verificando se o arquivo possui dados
        notas.update(dados_carregados) #Se possui, adicionando esses dados ao dicionário 'notas'
        print("Dados carregados com sucesso!")
        printar_notas(notas)
      else:
        print("Nenhum dado para carregar ou arquivo não encontrado/vazio.")
    elif escolha == 0:
      print(f'Fim do programa, obrigado {usuario}!') #Finalizando o programa
      break
    else:
      print('Opção inválida!') #Opção inválida, fora do que foi pedido


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
  if not notas:
    print('O dicionário atual está vazio. Tentando carregar dados do arquivo JSON')
    dados_arquivo = ler_notas()
    if dados_arquivo:
        notas.update(dados_arquivo)
        print('Dados do arquivo encontrados para a operação.')
    else:
        print('Não há dados disponíveis para calcular as estatísticas')
        return


  while True:
    try:
      escolha = int(input('Insira uma das opções acima.'))
    except ValueError:
      print('Insira um número válido')
      continue
    if escolha == 1:
        if notas:
          media = sum(notas.values())/len(notas.values())
          print(f'A média das notas é {media:.2f}')
        else:
            print('Não há notas para calcular a média.')
    elif escolha == 2:
        if notas:
          maior_nota = max(notas.values())
          alunos_maior_nota = [nome for nome,nota in notas.items() if nota == maior_nota]
          print(f'A maior nota da turma é {maior_nota:.2f} e os alunos {alunos_maior_nota} a tiraram')
        else:
            print('Não há notas para verificar.')
    elif escolha == 3:
        if notas:
          menor_nota = min(notas.values())
          alunos_menor_nota = [nome for nome, nota in notas.items() if nota == menor_nota]
          print(f'A menor nota da turma é {menor_nota:.2f} e os alunos {alunos_menor_nota} a tiraram')
        else:
            print('Não há notas para verificar.')
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
  if not notas:
        dados_arquivo = ler_notas()
        if dados_arquivo:
            notas.update(dados_arquivo)
        else:
            print('Não há dados disponíveis para ordenação')
            return

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
  with open('notas.json','w') as arquivo:
    arquivo.write(json.dumps(notas))


#lendo arquivos
def ler_notas():
  try:
    with open('notas.json','r') as leitura_arquivo:
      texto = leitura_arquivo.read()
      if not texto.strip():
        return {}
      dados = json.loads(texto)
      return dados
  except (FileNotFoundError, json.JSONDecodeError):
    return {}

#printando arquivos
def printar_notas(notas):
  print('Dados salvos no arquivo:')
  for nome, nota in notas.items():
    print(f'{nome}: {nota}')

main()