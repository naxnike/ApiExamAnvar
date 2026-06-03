from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Transaction
from .serializers import TransactionSerializer, TopTransactionSerializer


class TransactionView(APIView):

    @swagger_auto_schema(request_body=TransactionSerializer)
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Получена транзакция",
                    "task_id": serializer.data['transaction_id']
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: openapi.Response('Успешно')})
    def delete(self, request):
        Transaction.objects.all().delete()
        return Response(
            {"message": "Транзакции были удалены."},
            status=status.HTTP_200_OK
        )


class StatisticsView(APIView):

    @swagger_auto_schema(responses={200: openapi.Response('Статистика')})
    def get(self, request):
        transactions = Transaction.objects.all()
        total = transactions.count()
        avg = transactions.aggregate(Avg('amount'))['amount__avg'] or 0
        top3 = Transaction.objects.order_by('-amount')[:3]

        return Response({
            "total_transactions": total,
            "average_transaction_amount": round(float(avg), 2),
            "top_transactions": TopTransactionSerializer(top3, many=True).data
        })