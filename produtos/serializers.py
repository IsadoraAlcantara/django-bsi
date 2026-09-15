from decimal import Decimal

from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ("id", "nome", "preco")

    def validate_nome(self, value):
        nome_limpo = value.strip()
        if len(nome_limpo) < 2:
            raise ValidationError(
                "O nome deve possuir pelo menos 2 caracteres."
            )
        return nome_limpo

    def validate_preco(self, value):
        if value <= Decimal("0"):
            raise ValidationError("O preço deve ser maior que zero.")
        return value