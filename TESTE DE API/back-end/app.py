from flask import Flask
from flask_cors import CORS

from src.routes import app_routes

###################################################################

def create_app():
    # Instancia o flask
    app = Flask(__name__)
    
    # Importa as rotas de app_routes
    app.register_blueprint(app_routes)
    
    # Uso do Cors para permitir requisições do front-end
    CORS(app)
    
    return app

if __name__ == '__main__':
    # Inicia a instancia do app
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)