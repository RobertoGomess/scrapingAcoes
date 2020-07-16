from services.scraping import get_all,get_by_name
from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/acao/<string:name>", methods=['GET'])
def by_name(name):
    """
    Get per name.
    """
    if not name:
        return "Não foi informado", 400
    return get_by_name(name)

@app.route("/acao/all", methods=['GET'])
def get_all_itens():
    """
    List all itens.
    """
    return get_all()

if __name__ == "__main__":
    app.run(debug=True)