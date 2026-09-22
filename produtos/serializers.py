from decimal import Decimal

from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ("id", "nome", "preco", "marca", "estoque")

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

    def validate_marca(self, value):
        marca_limpo = value.strip()
        if len(marca_limpo) < 2 or len(marca_limpo) > 50:
            raise ValidationError(
                "O nome deve possuir de 2 à 50 caracteres."
            )
        return marca_limpo

    def validate_estoque(self, value):
        if value <= Decimal("0"):
            raise ValidationError("O preço deve ser maior que zero.")
        return value
    # PAREI AQUI, CORRIGIR O "Decimal("0")"