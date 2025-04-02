import json

from .data.data_loader import search_data
from flask import Blueprint, request, Response

###################################################################

app_routes = Blueprint('app_routes', __name__)

# Rota de pesquisa nos dados de cadastros de operadoras
@app_routes.route('/search_cadop', methods=['GET'])
def get_registration():
    # Obtem os parametros de pesquisa
    filter = request.args

    # Faz a busca nos dados usando os filtros passados
    data_result = search_data(filter)

    if not data_result:
        # Caso nada seja encontrado nos dados
        return Response(
            json.dumps({"error": "Nenhum dado encontrado"}, ensure_ascii=False),
            content_type="application/json; charset=utf-8",
            status=400)
        
    # Retorna os dados 
    return Response(
        json.dumps(data_result, ensure_ascii=False),
        content_type="application/json; charset=utf-8",
        status=200)