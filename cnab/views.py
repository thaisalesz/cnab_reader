from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
from .serializers import TransactionSerializer
from .utils import handle_uploaded_cnab_file, handle_db_data

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    if request.method == "POST":
        cnab_file = request.FILES['cnabFile']
        handle_uploaded_cnab_file(cnab_file)

        db_cnab_entries = Transaction.objects.all().order_by('nome_loja')
        serializer = TransactionSerializer(db_cnab_entries, many=True) 

        db_data = handle_db_data(serializer.data)

        return render(request, 'cnab.html', {'db_data': db_data})