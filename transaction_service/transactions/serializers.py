from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'user_id', 'amount', 'currency', 'timestamp']
        ref_name = 'Transaction'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Сумма должна быть больше нуля")
        return value

    def validate_currency(self, value):
        allowed = ['USD', 'EUR', 'RUB', 'KGS']
        if value.upper() not in allowed:
            raise serializers.ValidationError(f"Валюта должна быть одной из: {allowed}")
        return value.upper()


class TopTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'amount']
        ref_name = 'TopTransaction'