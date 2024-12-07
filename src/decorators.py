import re

from project_sys import PATH_HOME
import datetime
import os


def log(filename):
    """Декоратор который автоматически логирует начало и конец выполнения функции,
        а также ее результаты или возникшие ошибки."""
    def wrapper(func):
        def inner(*args, **kwargs):
            current_directory = os.path.join(PATH_HOME, "logs.txt")
            data_ = datetime.datetime.now()
            start_ = f'{data_}--> Function: {func} started'
            result = None
            try:
                if not filename.endswith(".txt") and filename != '':
                    raise Exception("Неверное расширение файла")
                result = func(*args, **kwargs)
                out = f'{start_} OK!; result: ({result})\n'
            except Exception as err:
                if err == "Неверное расширение файла" :
                    out = err
                else:
                    out = f'{start_}-> ERROR!: {err} \n при входных данных: {args}, {kwargs}\n'
            finally:
                if filename == '':
                    out = out.replace("\n", "")
                    return out, result
                else:
                    with open(current_directory, "a", encoding="utf-8") as file:
                        file.write(out)
                    out = out.replace("\n", "")
                    return out, result
        return inner
    return wrapper
