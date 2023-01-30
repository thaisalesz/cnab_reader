from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    transaction = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = '__all__'

    def get_transaction(self, obj):
        return obj.get_tipo_display()

