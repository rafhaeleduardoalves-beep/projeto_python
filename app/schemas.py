from app import ma
from app.models.produto_model import Produto

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto
        load_instance = True

produto_schema = ProdutoSchema()
produtos_schema = ProdutoSchema(many=True)