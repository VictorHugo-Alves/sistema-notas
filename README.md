# Sistema de Gerenciamento de Notas

## Descrição do Projeto

Este projeto implementa um Sistema de Gerenciamento de Notas desenvolvido em Python. Ele demonstra conceitos fundamentais de programação, como modularização com funções, estrutura de dados (dicionários) e persistência de dados em arquivo (JSON). O sistema permite o cadastro, alteração, cálculo de estatísticas e ordenação de alunos e suas notas.

## Como Executar o Projeto

Para testar e rodar este sistema em sua máquina local, siga os passos abaixo:

1.  **Pré-requisitos:**
    * **Python 3.x** (preferencialmente Python 3.8 ou superior)

2.  **Obter o Código:**
    Você tem duas opções para obter o código:
    * **Clonar o repositório (recomendado - se você tiver Git instalado):**
        Abra seu terminal (Git Bash, Prompt de Comando ou PowerShell) e execute o comando:
        ```bash
        git clone https://github.com/VictorHugo-Alves/sistema-notas.git
        cd sistema-notas
        ```
    * **Baixar o ZIP do projeto:**


4.  **Executar o Programa:**
    Com o terminal posicionado na pasta correta, execute o script Python principal:
    ```bash
    python trabalho-p2.py
    ```


5.  **Interagindo com o Sistema:**
    * O sistema irá iniciar com uma mensagem de boas-vindas e pedirá seu nome de usuário.
    * Em seguida, um menu de opções será exibido. Você poderá cadastrar alunos, alterar notas, ver estatísticas, ordenar alunos e salvar/carregar dados.
    * Os dados serão salvos e carregados do arquivo `notas.json` na mesma pasta do script principal.


## Funcionalidades

O sistema oferece as seguintes funcionalidades principais:

* **Cadastro de Alunos e Notas**: Permite registrar novos alunos e associar notas a eles. Inclui validação para garantir nomes e notas válidos (notas entre 0 e 10).
* **Cálculo de Estatísticas**: Calcula e exibe estatísticas importantes para as notas dos alunos, como média, maior e menor nota[cite: 18].
* **Ordenação de Alunos**: Possibilita ordenar a lista de alunos por nome ou por nota, facilitando a visualização e análise dos dados.
* **Persistência de Dados**: Salva os dados dos alunos e suas notas em um arquivo JSON (`notas.json`) e permite o carregamento posterior, garantindo que as informações não se percam após o encerramento do programa.
* **Tratamento de Exceções**: Implementa mecanismos robustos para lidar com entradas inválidas (e.g., texto onde se espera número) e cenários de arquivo (e.g., arquivo `notas.json` não encontrado ou vazio).
* **Modularização do Código**: O código é dividido em funções bem definidas para cada tarefa (menu, cadastro, estatísticas, ordenação, manipulação de arquivos), promovendo organização e legibilidade.
* **Função Recursiva**: Contém uma implementação de uma função recursiva (`soma_notas`) utilizada no cálculo da média das notas, demonstrando o uso de recursão.


## Autor

* **Victor Hugo Alves**
    * [Seu perfil do LinkedIn](https://www.linkedin.com/in/victorhugo-data/)

## Licença
Este projeto é **open-source** e sua colaboração é bem-vinda! Sinta-se livre para explorar, aprender e contribuir com o código.
