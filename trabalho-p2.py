import json #Importando o JSON

#principal
def main(): #Definindo a função principal
  notas = {} #Definindo a variável notas como um dicionário vazio
  print("\n******************* Sistema de notas - UERJ *******************") #Mensagem de boas vindas
  print('Olá, professor(a) seja bem vindo(a) ao sistema de gerenciamento de notas da UERJ') #Mensagem de boas vindas
  usuario = input('Qual o seu nome?').title() #Para personalizar o uso do sistema pelo usuário
  if not usuario:
    return 'Campo vazio, insira um nome.'
  elif not usuario.replace(' ','').isalpha():
    return 'Insira um nome válido! Use apenas letras e espaços'
  while True: #Loop da fuñção principal
    escolha = menu() #Chamando a função 'menu()'
    if escolha == 1:
      cadastro_alunos(notas) #Chamando a função de cadastro de alunos
    elif escolha == 2:
        alterar_notas(notas) #Chamando a função para alterar notas
    elif escolha == 3:
      estatistica(notas) #Chamando a função de estatística
    elif escolha == 4:
      ordenar_alunos(notas) #Chamando a função de ordenação de alunos
    elif escolha == 5:
      dados_carregados = ler_notas() #Chamando a função para printar os dados do arquivo json
      if dados_carregados: #Verificando se o arquivo possui dados
        notas.update(dados_carregados) #Se possui, adicionando esses dados ao dicionário 'notas'
        print("Dados carregados com sucesso!")
        printar_notas(notas) #Chamando a função printar_notas(), com o dicionario 'notas' como parâmetro
      else:
        print("Nenhum dado para carregar ou arquivo não encontrado/vazio.")

    elif escolha == 0:
      print(f'Fim do programa, obrigado {usuario}!') #Finalizando o programa
      break
    else:
      print('Opção inválida!') #Opção inválida, fora do que foi pedido


#menu
def menu(): #Definindo a função menu, que é chamada na função main()
  print('''
1.Cadastrar alunos e suas notas
2.Alterar notas
3.Calcular estatísticas(média, maior e menor nota)
4.Ordenar alunos por nome ou nota
5.Carregar os dados salvos
0.Sair
''')
  try: #tratamento de erros para o input abaixo
    return int(input('Insira uma das opções acima:')) #Retorna um input para o usuário selecionar a opção desejada
  except ValueError:
    print('Insira um número válido')
    return None


#Cadastro notas
def cadastro_alunos(notas): #Criando a função para cadastro de notas
  while True: #loop para o cadastro de notas até que o usuário queira parar
      nome = input('Insira o nome do aluno: ').title()
      if not nome: #Verificando se o nome não é vazio
        print('Insira um nome válido')
        continue #Retornando ao início do loop
      elif not nome.replace(' ','').isalpha(): #Verificando se não há caracteres além de letras e espaços
        print('Nome inválido! Insira apenas letras e espaços')
        continue #Retornando ao início do loop
      try:
        nota = float(input('Insira a nota do aluno'))
      except ValueError: #Tratamento de erros para a nota do aluno
        print(f'Nota inválida')
        continue
      if 0 <= nota <=10:
        notas[nome] = nota #Se passar por todas as verificações de nome e nota, adiciona o aluno e a nota no dicionário de notas (nome como chave e nota como valor)
      else:
        print('A nota deve estar entre 0 e 10.')
        continue
      while True: #loop para verificar se o usuário deseja continuar com o processo
        continua = input('Deseja continuar? Y/N').upper()
        if continua not in ('Y','N'):
          print('Insira Y ou N')
        else:
          break
      if continua == 'Y':
        continue
      else:
        while True: #Caso ele não queira continuar, outro loop para saber se ele quer salvar as notas no arquivo
          salvar = input('Deseja salvar os dados? Y/N').upper()
          if salvar not in ('Y','N'):
            print('Insira Y ou N')
          else:
            break
      if salvar == 'Y':
        guardar_notas(notas) #Se for salvar, chama a função guardar_notas() com o dicionário 'notas' como parâmetro
        print('Dados salvos com sucesso')
        print('Voltando ao menu')
        break
      else:
        print('Voltando ao menu')
        break

#Função para alterar notas
def alterar_notas(notas):
    while True: #Loop para escolha do usuário
        try: #Tratamento de erros pra escolha do usuário
            escolha = int(input('Escolha: alterar nome(1), alterar nota(2), excluir aluno(3), sair(0)'))
        except:
            print('Insira um número válido.')

        if escolha == 1:
            aluno = input('Insira o nome que deseja modificar').title()
            if aluno in notas: #Verificando se o aluno está no sistema
                novo_nome = input('Insira o novo nome').title() #Definindo o novo nome
                if novo_nome and novo_nome.replace(' ','').isalpha(): #Verificando se o novo nome não está vazio e se possui apenas letras
                    notas[novo_nome] = notas[aluno] #Alterando o nome do aluno
                    del notas[aluno] #Deletando o nome antigo
                    print('Alteração realizada com sucesso!')
                else:
                    print('Insira um nome válido')
            else:
                print('O aluno informado não está cadastrado no sistema')

        elif escolha == 2:
            aluno = input('Insira o nome do aluno que deseja alterar a nota').title()
            if aluno in notas: #Verificando se o aluno está no sistema
                try:
                  nova_nota = float(input(f'Insira a nova nota para {aluno}: '))
                  if 0 <= nova_nota <= 10: #Verificando a nota
                      notas[aluno] = nova_nota #Alterando a nota
                      print('Nota alterada com sucesso!')
                  else:
                      print('A nota deve estar entre 0 e 10.')
                except ValueError:
                  print('Nota inválida. Insira um número.')
            else:
                print('O aluno informado não está cadastrado no sistema')

        elif escolha == 3:
          aluno = input('Insira o nome do aluno que deseja remover').title()
          if aluno in notas and aluno and aluno.replace(' ','').isalpha(): #Verificando o nome
            del notas[aluno] #Deletando o aluno
            print('Aluno removido com sucesso!')
          else:
            print('O aluno não está no sistema')

        elif escolha == 0:
            while True: #Caso ele não queira continuar, outro loop para saber se ele quer salvar as notas no arquivo
                salvar = input('Deseja salvar os dados? Y/N').upper()
                if salvar not in ('Y','N'):
                    print('Insira Y ou N')
                else:
                    break
            if salvar == 'Y':
                guardar_notas(notas) #Se for salvar, chama a função guardar_notas() com o dicionário 'notas' como parâmetro
                print('Dados salvos com sucesso')
                print('Voltando ao menu...')
                break
            else:
                print('Dados descartados.')
                print('Voltando ao menu...')
                break
        else:
            print('Insira uma opção válida: alterar nome(1), alterar nota(2), sair(0)')

#estatisticas
def estatistica(notas):
  
  if not notas: #verifica se o dicionário está vazio, para evitar divisão por zero
    print('O dicionário atual está vazio. Tentando carregar dados do arquivo JSON')
    dados_arquivo = ler_notas() #Caso esteja vazio, define uma nova variavel chamada 'dados_arquivo' como função ler_notas()
    if dados_arquivo: #Verifica se a nova variável possui dados
        notas.update(dados_arquivo) #Caso possua, adiciona todos os dados no dicionário de notas
        print('Dados do arquivo encontrados para a operação.')
    else:
        print('Não há dados disponíveis para calcular as estatísticas')
        return


  while True:
    print('''
  1. Calcular média
  2. Maior nota
  3. Menor nota
  0. Voltar ao menu
  ''')
    try:
      escolha = int(input('Insira uma das opções acima.'))
    except ValueError:
      print('Insira um número válido')
      continue
    if escolha == 1:
        if notas:
          valores_notas = list(notas.values())
          soma_total = soma_notas(valores_notas, 0) # Chama a função recursiva
          media = soma_total / len(valores_notas) # Calcula a média com a soma recursiva
          print(f'A média das notas é {media:.2f}')
        else:
            print('Não há notas para calcular a média.')
    elif escolha == 2:
        if notas: #Verifica se o dicionário de notas não está vazio
          maior_nota = max(notas.values()) #Cria a variável da maior nota
          alunos_maior_nota = [nome for nome,nota in notas.items() if nota == maior_nota] #Cria uma lista usando list compreehnsion, adicionando todos os alunos que possuem a tal da maior nota
          print(f'A maior nota da turma é {maior_nota:.2f} e os alunos {alunos_maior_nota} a tiraram')
        else:
            print('Não há notas para verificar.')
    elif escolha == 3:
        if notas:
          menor_nota = min(notas.values()) #Cria a variável da menor nota
          alunos_menor_nota = [nome for nome, nota in notas.items() if nota == menor_nota] #Cria uma lista usando list compreehnsion, adicionando todos os alunos que possuem a tal da menor nota
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
  if not notas: #Verifica se o dicionário de notas está vazio
        dados_arquivo = ler_notas() #Caso esteja vazio, define a variavel dados_arquivo chamando a função ler_notas()
        if dados_arquivo: #Verifica se a variável possui dados
            notas.update(dados_arquivo) #Caso possua, atualiza o dicionário de notas com esses dados
        else:
            print('Não há dados disponíveis para ordenação')
            return

  while True:
    print('''
  1. Ordenar por nome
  2. Ordenar por nota
  0. Voltar ao menu
  ''')
    try:
        escolha = int(input('Insira uma das opções acima.'))
        if escolha == 1:
          for nome, nota in sorted(notas.items()): #Ordena os alunos por nome
            print(f'{nome}: {nota}')
        elif escolha == 2:
          for nome, nota in sorted(notas.items(), key=lambda i:i[1], reverse = True): #Ordena por nota, utilizando key=lambda e reverse = True para mostrar da maior para a menor nota
            print(f'{nome}: {nota}')
        elif escolha == 0:
          print('Voltando ao menu')
          break
        else:
          print('Escolha um número válido')
    except ValueError:
      print('Insira um número válido')


#Função recursiva de soma de notas
def soma_notas(notas_list, indice):
#notas_list: Uma lista contendo os valores das notas
#indice: O índice atual na lista que está sendo processado

  # Caso Base: Se o índice for igual ao tamanho da lista, não há mais notas para somar
  if indice >= len(notas_list):
      return 0
  else:
      # Recursiva: Soma a nota atual com a soma do restante da lista
      return notas_list[indice] + soma_notas(notas_list, indice + 1)



#guardando arquivos
def guardar_notas(notas):
  with open('notas.json','w') as arquivo: #Utilizando o metodo with, cria a variavel arquivo no modo escrita no arquivo 'notas.json'
    arquivo.write(json.dumps(notas)) #Utilizando o metodo json.dumps, guarda as notas do dicionário no arquivo


#lendo arquivos
def ler_notas():
  try:
    with open('notas.json','r') as leitura_arquivo: #Utilizando o metodo with, cria a variavel leitura_arquivo no modo modo de leitura no arquivo 'notas.json'
      texto = leitura_arquivo.read() #Define a variavel texto como o leitor dessa variavel
      if not texto.strip(): #Caso não possua nada na variavel texto, retorna um dicionário vazio
        return {}
      dados = json.loads(texto) #Caso possua dados, cria uma nova variavel chamada 'dados' e carrega nela todos os dados da variavel 'texto' atraves do metodo json.loads
      return dados
  except (FileNotFoundError, json.JSONDecodeError): #Tratamento de erros de arquivos json
    return {}

#printando arquivos
def printar_notas(notas):
  print('Dados salvos no arquivo:')
  for nome, nota in notas.items():
    print(f'{nome}: {nota}')

main()