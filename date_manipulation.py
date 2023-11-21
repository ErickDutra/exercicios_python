from datetime import datetime

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y'
date_start = datetime.strptime('20/12/2020', fmt)
data_fim = datetime.strptime('20/12/2025', fmt)

delta = relativedelta(data_fim, date_start)
diferennt_month = delta.years * 12
loan = 1000000

for i in range(diferennt_month):
    print(f'{date_start + relativedelta(months=+i)}, {(loan / diferennt_month):.2f}')

