from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ver_tela(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    if request.method == "POST":
        cnab_file = request.FILES['cnabFile'].read()
        print(cnab_file)

        return render(request, 'cnabInfo.html', {'file_data': cnab_file})