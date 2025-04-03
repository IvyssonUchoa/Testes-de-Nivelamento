# Teste de API

## Desafio
Avaliar a capacidade de criar uma API para buscar informações sobre operadoras de saúde.

## Objetivo
Construir uma API utilizando Python e Vue.js que permita pesquisar operadoras de saúde cadastradas. A API deve fornecer resultados relevantes e ser demonstrada com uma coleção no Postman.

## Dependências
* Linguagem Python e JavaScript
* Biblioteca pandas
* Framework Flask
* Ferramenta Postman

## Resultado Esperado
Após a execução do script, espera-se:
* A implementação de uma API em python que permita a busca textual na lista de operadoras.
* O desenvolvimento de uma interface simples para consulta dos dados.
* A criação de uma coleção no Postman para demonstrar a funcionalidade da API.

## Executar o Teste
1. Clone o repositório:
   ```bash
   git clone https://github.com/IvyssonUchoa/Testes-de-Nivelamento.git
   cd 'Testes de Nivelamento/TESTE DE API/back-end'
   ```

2. Instale as dependências necessárias através do arquivo "requirements.txt":
    ```
    pip install -r requirements.txt
    ```

3. Execute o arquivo app.py para iniciar o servidor:
    ```
    python3 app.py
    ```

4. Para experimentar o interface web,
    * Abra o arquivo 'TESTE DE API/front-end/index.html' no navegador 
    * Selecione um filtro no seletor e insira um valor de pesquisa
    * Clique no Botão **Buscar**

5. Para testar a coleção Postman,
    * Abra o Postman e clique em **File > Import**
    * Selecione o arquivo **"Colecao_Teste_API.postman_collection.json"**
    * Clique em Open