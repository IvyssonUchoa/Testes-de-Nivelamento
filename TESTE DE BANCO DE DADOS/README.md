# Teste de Banco de Dados

## Desafio
Avalia a capacidade de manipular e analisar grandes conjuntos de dados utilizando um banco de dados.

## Objetivo
Criar e estruturar um banco de dados utilizando PostgreSQL, importando dados públicos sobre operadoras de saúde, além de escrever queries para realizar análises sobre as despesas das operadoras.

## Dependências
* Servidor PostgreSQL 

## Resultado Esperado
Após a execução do script, espera-se:
* A criação das tabelas de dados **cadop** e **demo_contabeis**
* A importação dos dados presentes nos arquivos CSV para suas respectivas tabelas
* A execução correta das queries de análise dos dados das tabelas

## Executar o Teste
1. Baixe os arquivos dos últimos 2 anos do repositório da ANS:
    https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

2. Baixe os Dados cadastrais das Operadoras Ativas na ANS:
    https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/

3. No arquivo **load_csvs.sql**, substitua "caminho para o relatorio X" pelo respectivo caminho do arquivo baixado nas etapas 1 e 2 para alimentar suas respectivas tabelas:
    ```
    -- Exemplo

    \COPY cadop FROM /caminho/para/Relatorio_de_Dados_cadastrais_das_Operadoras.csv' DELIMITER ';' CSV HEADER;
    \COPY demo_contabeis FROM '/caminho/para/Relatorio_de_Demonstracao_Contabel_1T2023.csv' DELIMITER ';' CSV HEADER;
    ```

4. Acesse o Banco de Dados PostgreSQL:
    ```
    psql -U seu_usuario
    ```

5. Crie um novo Banco de Dados, caso não exista um, e o acesse:
    ```
    CREATE DATABASE teste_banco_de_dados;
    \c teste_banco_de_dados;
    ```

6. Execute os comandos presentes no arquivo **create_tables.sql**

7. Execute os comandos presentes no arquivo **load_csvs.sql**

8. Execute os comandos presentes no arquivo **analysis_query.sql**