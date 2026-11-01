from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app import db
from app.models.produto_model import Produto
from app.schemas import produto_schema, produtos_schema

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

# Endpoint: Cadastro de Produto
@produtos_bp.route('/cadastrar', methods=['POST'])
def criar_produto():
    data = request.get_json()
    try:
        produto = produto_schema.load(data)
        db.session.add(produto)
        db.session.commit()
        return produto_schema.jsonify(produto), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Endpoint: Listagem de Produtos
@produtos_bp.route('/', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return produtos_schema.jsonify(produtos), 200