from .serializers import TransactionSerializer
from datetime import datetime, date
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

def handle_uploaded_cnab_file(file):
    cnab_entries = []
    for line in file:
        cnab_entries.append(line.decode("utf-8").rstrip())

    negative_entries = ['2','3','9']

    for line in cnab_entries:
        entry = dict(
            tipo=line[0],
            data = line[1:9],
            valor = int(line[9:19]) if line[0] not in negative_entries else -abs(int(line[9:19])),
            cpf = line[19:30],
            cartao = line[30:42],
            hora = line[42:48],
            dono_loja=line[48:62].rstrip(),
            nome_loja=line[62:]
        )
        serializer = TransactionSerializer(data=entry)
        serializer.is_valid(raise_exception=True)
        serializer.save()

def handle_db_data(data):
    db_data = {}
    for entry in data:
        entry['valor'] = entry['valor']/100
        entry_date = datetime.strptime(entry['data'], f'%Y-%m-%d').date()
        entry['data'] = entry_date.strftime(f'%d de %B, %Y')

        if entry['nome_loja'] not in db_data:
            db_data[entry['nome_loja']] = []
            db_data[entry['nome_loja']].append(entry)
        else:
            db_data[entry['nome_loja']].append(entry)

    for i, loja in db_data.items():
        balance = []
        for item in loja:
            balance.append(item['valor'])
            item['valor'] = locale.currency(item['valor'], grouping=True)
        db_data[i].append('%.2f' %sum(balance))

    return db_data