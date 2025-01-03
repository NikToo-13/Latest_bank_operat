import logging
import os

from project_sys import PATH_HOME
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csvexcel import read_csv, read_excels
from src.utils import json_to_dictionary, convert_date_to_general, transaction_search
from src.widget import get_date, mask_account_card

path_ = f"{PATH_HOME}/logs/main.log"
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(path_, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def main():
    """основная логика проекта"""
    legend_s = " Функция: main -> "
    logger.info(f"{legend_s}Запуск функции, приветствие пользователя.")
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    # Вывод осногного меню
    while True:
        print()
        print('Выберите необходимый пункт меню:')
        print('___________________________________________________')
        print('1. Получить информацию о транзакциях из JSON-файла')
        print('2. Получить информацию о транзакциях из CSV-файла')
        print('3. Получить информацию о транзакциях из XLSX-файла')
        entrance = input('-> ')
        logger.info(f"{legend_s}Получение варианта выбора файла: {entrance}")
        if entrance == '1':
            print('Для обработки выбран JSON-файл.')
            data_file_transaction = json_to_dictionary(PATCH_FILE_JSON)
            break
        if entrance == '2':
            print('Для обработки выбран CSV-файл.')
            data_file = read_csv(PATCH_FILE_CSV)
            data_file_transaction = convert_date_to_general(data_file)
            break
        if entrance == '3':
            print('Для обработки выбран XLSX-файл.')
            data_file = read_excels(PATCH_FILE_EXCEL)
            data_file_transaction = convert_date_to_general(data_file)
            break
        print(f'Введено значение несоответствующее не одному пункту меню( {entrance} )')
        entrance = ''
        print('Повторите попытку')
        logger.warning(f"{legend_s}Неверный ввод данных: {entrance}")
    # Запрос на фильтрацию списка
    while True:
        print()
        print('Введите статус, по которому необходимо выполнить фильтрацию. \n'
              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        status_in = str(input('-> '))
        logger.info(f"{legend_s}Получение варианта выбора статуса: {status_in}")
        status = status_in.upper()
        if status == 'EXECUTED' or status == 'CANCELED' or status == 'PENDING':
            data_file_filter = filter_by_state(data_file_transaction, status)
            if type(data_file_filter) == list:
                print(f'Операции отфильтрованы по статусу "{status}"')
                break
            elif type(data_file_filter) == str:
                print(data_file_filter)
        else:
            print(f'Статус операции "{status_in}" недоступен.')
            logger.warning(f"{legend_s}Неверный ввод статуса: {status_in}")
    filtr = True
    while filtr:
        data_file_filter_dat = []
        print()
        print('Отсортировать операции по дате? Да/Нет')
        date_filtr_statuss = str(input('-> '))
        logger.info(f"{legend_s}Запрос на сортировку даты. Введено: {date_filtr_statuss}")
        date_filtr_status = date_filtr_statuss.upper()
        if date_filtr_status == 'ДА':
            while True:
                print('Отсортировать по возрастанию или по убыванию?')
                date_filtr_up_downs = str(input('-> '))
                logger.info(f"{legend_s}Запрос тип сортировки даты. Введено: {date_filtr_up_downs}")
                date_filtr_up_down = date_filtr_up_downs.upper()
                if date_filtr_up_down == 'ПО ВОЗРАСТАНИЮ':
                    data_file_filter_dat = sort_by_date(data_file_filter)
                    filtr = False
                    print('Операции отсортированы по возрастанию')
                    break
                elif date_filtr_up_down == 'ПО УБЫВАНИЮ':
                    data_file_filter_dat = sort_by_date(data_file_filter, False)
                    filtr = False
                    print('Операции отсортированы по убыванию')
                    break
                else:
                    print('Некоректный ввод!!!')
                    logger.warning(f"{legend_s}Неверный ввод типа сортировки даты: {status_in}")
        elif date_filtr_status == 'НЕТ':
            data_file_filter_dat = data_file_filter
            break
        else:
            print('Некорктный ввод!')
            logger.warning(f"{legend_s}Неверный ввод (ДА/НЕТ): {date_filtr_status}")
    cicl = True
    while cicl:
        print()
        print('Выводить только рублевые тразакции? Да/Нет')
        transac_rubl = str(input('-> '))
        logger.info(f"{legend_s}Запрос на рублевые тразакции. Введено: {transac_rubl}")
        transac_rub = transac_rubl.upper()
        if transac_rub == 'ДА':
            filter_by_curr = filter_by_currency(data_file_filter_dat, "RUB")
            s = 1
            data_file_filter_curr = []
            while s == 1:
                try:
                    by_currency = next(filter_by_curr)
                except:
                    s = 0
                    cicl = False
                else:
                    data_file_filter_curr.append(by_currency)
                    s = 1
            print('Отфильтровано по рублевым тразакциям.')
            logger.info(f"{legend_s}Отфильтровано по рублевым тразакциям.")
        elif transac_rub == 'НЕТ':
            data_file_filter_curr = data_file_filter_dat
            cicl = False
            break
        else:
            print('Некорктный ввод!')
            logger.warning(f"{legend_s}Неверный ввод (ДА/НЕТ) для фильтра по рублевым транзакциям: {transac_rubl}")
    while True:
        print()
        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        filter_words = str(input('-> '))
        logger.info(f"{legend_s}Запрос на фильтрацию по описанию(Да/Нет): {filter_words}")
        filter_word = filter_words.upper()
        if filter_word == 'ДА':
            print('Введите слово по которому нужно отфильтровать список.')
            words = str(input('-> '))
            date_search = transaction_search(data_file_filter_curr, words)
            print(f'Отфильтровано по слову {words} в описании.')
            logger.info(f"{legend_s}Отфильтровано по слову {words} в описании.")
            break
        elif filter_word == 'НЕТ':
            date_search = data_file_filter_curr
            break
        else:
            print('Введен некоректный ответ!')
            logger.warning(f"{legend_s}Неверный ввод (ДА/НЕТ) на запрос фильтрацию по описанию: {filter_word}")
    # Итоговая логика вывода результата
    print('________________________РЕЗУЛЬТАТ ФИЛЬТРАЦИИ_______________________________')
    if date_search == []:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print()
        print('Распечатываю итоговый список транзакций...')
        print()
        print(f'Всего банковских операций в выборке: {len(date_search)}')
        for date_sample in date_search:
            print()
            #print(date_sample)
            print(f'{get_date(date_sample['date'])} {date_sample['description']}')
            if 'from' in date_sample:
                if str(date_sample['from']) == 'nan' or date_sample['from'] == '':  #!= nan
                    print(mask_account_card(date_sample['to']))
                else:
                    print(f'{mask_account_card(date_sample['from'])} -> {mask_account_card(date_sample['to'])}')
            else:
                print(mask_account_card(date_sample['to']))
            if date_sample['operationAmount']['currency']['code'] == 'RUB':
                print(f'Сумма: {date_sample['operationAmount']['amount']} руб.')
            else:
                print(f'Сумма: {date_sample['operationAmount']['amount']} {date_sample['operationAmount']['currency']['code']}')
    logger.info(f"{legend_s}Вывод результатов")


if __name__ == "__main__":
    PATCH_FILE_JSON = os.path.join(PATH_HOME, "data", "operations.json")
    PATCH_FILE_CSV = os.path.join(PATH_HOME, "data", "transactions.csv")
    PATCH_FILE_EXCEL = os.path.join(PATH_HOME, "data", "transactions_excel.xlsx")
    main()