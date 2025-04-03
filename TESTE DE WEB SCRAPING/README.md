# Teste de Web Scraping

## Desafio
Avaliar a capacidade de coletar e manipular dados da web por meio de web scraping.

## Objetivo
Criar um script em Python que automatize a extração de arquivos PDF do site da ANS, compactando-os em um único arquivo ZIP.

**Link para o site:** https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos

**Importante:** Certifique-se de possuir um navegador Chrome instalado na máquina que executar o código

## Dependências
* Linguagem Python
* Framework Selenium
* Biblioteca Pandas

## Resultado Esperado
Após a execução do script, espera-se:
* Os arquivos PDF referentes aos Anexo I e Anexo II estejam baixados na pasta **"donwload"**
* Um arquivo ZIP contendo os Anexo I e Anexo II compactados na pasta **"results"**

## Executar o Teste
1. Clone o repositório:
   ```bash
   git clone https://github.com/IvyssonUchoa/Testes-de-Nivelamento.git
   cd 'Testes de Nivelamento/TESTE DE WEB SCRAPING'
   ```

2. Instale as dependências necessárias através do arquivo "requirements.txt"
    ```
    pip install -r requirements.txt
    ```

3. Execute o arquivo main.py
    ```
    python3 main.py
    ```