# Sistema de Gerenciamento de Notas

## Descrição do Projeto

Este projeto implementa um Sistema de Gerenciamento de Notas desenvolvido em Python. Ele demonstra conceitos fundamentais de programação, como modularização com funções, estrutura de dados (dicionários) e persistência de dados em arquivo (JSON). O sistema permite o cadastro, alteração, cálculo de estatísticas e ordenação de alunos e suas notas.

## Funcionalidades

O sistema oferece as seguintes funcionalidades principais:

* **Cadastro de Alunos e Notas**: Permite registrar novos alunos e associar notas a eles. Inclui validação para garantir nomes e notas válidos (notas entre 0 e 10).
* **Cálculo de Estatísticas**: Calcula e exibe estatísticas importantes para as notas dos alunos, como média, maior e menor nota[cite: 18].
* **Ordenação de Alunos**: Possibilita ordenar a lista de alunos por nome ou por nota, facilitando a visualização e análise dos dados.
* **Persistência de Dados**: Salva os dados dos alunos e suas notas em um arquivo JSON (`notas.json`) e permite o carregamento posterior, garantindo que as informações não se percam após o encerramento do programa.
* **Tratamento de Exceções**: Implementa mecanismos robustos para lidar com entradas inválidas (e.g., texto onde se espera número) e cenários de arquivo (e.g., arquivo `notas.json` não encontrado ou vazio).
* **Modularização do Código**: O código é dividido em funções bem definidas para cada tarefa (menu, cadastro, estatísticas, ordenação, manipulação de arquivos), promovendo organização e legibilidade.
* **Função Recursiva**: Contém uma implementação de uma função recursiva (`soma_notas`) utilizada no cálculo da média das notas, demonstrando o uso de recursão.

### Gerenciamento Avançado de Alunos e Notas

* **Gerenciamento de Alunos e Notas**: Além das funcionalidades básicas, o sistema permite ao usuário:
    * Alterar o nome de um aluno já cadastrado.
    * Alterar a nota de um aluno existente.
    * Excluir um aluno do sistema.
    Essa funcionalidade extra aprimora a usabilidade e a flexibilidade do sistema, mostrando um controle mais completo sobre os dados.

## Desafios e Aprendizados

O desenvolvimento deste projeto me proporcionou um grande aprendizado em:

* **Estruturação do Código**: O principal desafio foi a modularização interna do código, dividindo as funcionalidades em funções bem encapsuladas (main, menu, cadastro_alunos, etc.). Isso foi crucial para garantir a clareza, organização e manutenibilidade de um projeto mais complexo.
* **Tratamento de Exceções Robustas**: Aprender a prever e tratar diferentes tipos de erros (entrada de usuário inválida, problemas com arquivos JSON) foi crucial para tornar o sistema mais resiliente.
* **Persistência de Dados**: A implementação de salvamento e carregamento de dados em JSON foi um ponto chave para garantir a continuidade do sistema entre as execuções, exigindo cuidado na serialização e desserialização dos dados.
* **Lógica de Ordenação e Filtragem**: Desenvolver a lógica para ordenar alunos por diferentes critérios e extrair estatísticas demandou o uso eficaz de estruturas de dados e funções como `lambda`.
* **Gerenciamento de Versões com Git**: Utilizar o Git desde o início foi fundamental para controlar as alterações, revisar o histórico do código e garantir a segurança do trabalho, especialmente em um projeto em constante evolução.

## Autor

* **Victor Hugo Alves**
    * [Seu perfil do LinkedIn](https://www.linkedin.com/in/victorhugo-data/)
