import pandas as pd
from pathlib import Path

# Obtém o caminho do diretório atual
current_path = Path(__file__).parent.resolve()

# Carrega os daddos do relatório CSV apenas uma vez
data_path = current_path / "Relatorio_cadop.csv"

df_cadop = pd.read_csv(data_path, sep=';', encoding='utf-8', dtype=str)
df_cadop.fillna('', inplace=True)

###################################################################

def search_data(filter):
    try:
        df_filtered = df_cadop.copy()
        
        # lista com as colunas presentes no CSV
        authorized_col = list(df_cadop.columns)
        
        for arg, value in filter.items():
            
            # Caso o filtro não exista
            if arg not in authorized_col:
                return None
            
            # Filtra os dadso pelos valores passados nos filtros
            df_filtered = df_filtered.loc[
                df_filtered[arg].str.contains(value, case=False)
            ]
            
        filtered_json = df_filtered.to_dict(orient='records')
        
        return filtered_json
    
    except Exception as e:
        print(f"Erro durante pesquisa: {e}")
        return None