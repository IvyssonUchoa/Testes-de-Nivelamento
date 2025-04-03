import zipfile
import pdfplumber
import pandas as pd

from pathlib import Path

#########################################################################################

# Obtém o caminho do diretório atual
current_path = Path(__file__).parent.resolve()

data = []
columns = None

#########################################################################################

try:
    pdf_path = current_path / "data/Anexo_1.pdf"

    # Extrai as tabelas do arquivo PDF
    with pdfplumber.open(pdf_path) as pdf: 
        print("Iniciado extração de dados")
        
        for page in pdf.pages:
            table = page.extract_table()
            
            if table:
                
                # Obtem o nome as colunas das tabelas
                if columns is None:
                    columns = table[0]
                
                # Guarda o conteúdo das tabelas
                contents = table[1:]
                for row in contents:
                    data.append(row)
        
    # Converte os dados obtidos em um DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Substitue as abreviacoes das colunas OD e AMB conforme a legenda do PDF
    df['OD'] = df['OD'].str.replace('OD', 'Seg. Odontologica')
    df['AMB'] = df['AMB'].str.replace('AMB', 'Seg. Ambulatorial')

    # Converte o DataFrame em um arquivo CSV
    annex_1_path = current_path / "result/Anexo_1.csv"
    
    df.to_csv(annex_1_path, index=False, encoding='utf-8')

    # Compacta o arquivo CSV 
    zip_path = current_path / "result/Teste_Ivysson.zip"

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(annex_1_path, arcname=Path(annex_1_path).name)
        
    print("Operação concluida")
    print(f"Arquivo zip em: {zip_path}")
    
except Exception as e:
    print("Operação Interrompida") 
    print(f"Erro: {e}")