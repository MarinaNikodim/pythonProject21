import pandas as pd
import numpy as np


try:
    file_path = 'realisation_report.xlsx'
    selected_columns = ['Товар', 'Кол-во', 'Реализовано на сумму, руб.', 'Доплата за счет Ozon, руб.']
    datafile = pd.read_excel(file_path, sheet_name='Лист 1', header=12, usecols=selected_columns)
    print(datafile.head()) # проверка, вывод пяти первых строк
    # суммирование выручки и доплаты от озон, создание сводного файла
    pivot_table = pd.pivot_table(datafile, values=['Кол-во', 'Реализовано на сумму, руб.', 'Доплата за счет Ozon, руб.'],
                                 index=['Товар'], aggfunc=np.sum)
    print(pivot_table)
    pivot_table.to_excel('Pivot_report.xlsx') # выгрузка сводного файла
except FileNotFoundError:
    print('Файл не найден')



