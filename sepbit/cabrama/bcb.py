'''
Cabrama - Câmbio no Brasil para Mastodon
Copyright (C) 2020 Vitor Guia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import datetime
import csv
from urllib.request import Request, urlopen


def mask_money(value):
    '''
    Money format
    '''
    value = value.replace(',', '.')
    value = '{:.2f}'.format(float(value))
    return str(value.replace('.', ','))


def cotacao():
    '''
    Cotação BCB
    See https://www.bcb.gov.br/estabilidadefinanceira/cotacoestodas
    '''
    timestamp = datetime.datetime.now()

    request = Request(
        'https://www4.bcb.gov.br/Download/fechamento/' + timestamp.strftime('%Y%m%d') + '.csv',
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )
    with urlopen(request) as response:
        response = response.read()

    response = response.decode('utf-8')
    response = response.splitlines()

    message = 'Cotação: ' + timestamp.strftime('%d/%m/%Y') + ' 13:00'

    file = csv.reader(response, delimiter=';')
    for row in file :
        if row[3] == 'USD':
            message += '\n#Dolar R$:' + mask_money(row[5])

        if row[3] == 'EUR':
            message += '\n#Euro R$:' + mask_money(row[5])

        if row[3] == 'GBP':
            message += '\n#LibraEsterlina R$:' + mask_money(row[5])

        if row[3] == 'XAU':
            message += '\n#Ouro R$:' + mask_money(row[5])

    message += '\n\n#bot #cambio #PTAX #BCB #Brasil'
    return message
