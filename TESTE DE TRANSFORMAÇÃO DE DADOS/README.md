# Teste de Transformação de Dados

## Desafio
Avaliar a habilidade em processar e transformar dados extraídos de um arquivo PDF em um formato estruturado.

## Objetivo
Extrair informações de tabelas dentro de um PDFs (Anexo I), converter os dados para um formato estruturado (CSV) e compactá-los.

## Dependências
* Linguagem Python
* Biblioteca pandas
* Biblioteca pdfplumber

## Resultado Esperado
Após a execução do script, espera-se:
* A extração dos dados do **Anexo I** para um arquivo CSV na pasta **result**
* Substituição das abreviações "OD" e "AMB" por suas descrições completas na tabela
* Um arquivo ZIP contendo o Anexo I compactados na pasta **"results"**

## Executar o Teste
1. Clone o repositório:
   ```bash
   git clone https://github.com/IvyssonUchoa/Testes-de-Nivelamento.git
   cd 'Testes de Nivelamento/TESTE DE TRANSFORMAÇÃO DE DADOS'
   ```

2. Instale as dependências necessárias através do arquivo "requirements.txt":
    ```
    pip install -r requirements.txt
    ```

3. Execute o arquivo main.py:
    ```
    python3 main.py
    ```