import os

from project_sys import PATH_HOME


def log(filename=""):
    """Декоратор который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def wrapper(func):
        def inner(*args, **kwargs):
            current_directory = os.path.join(PATH_HOME, "logs.txt")
            data_ = ""
            function_str = str(func)
            funcs = function_str.split()
            start_ = f"{data_}--> Function: {funcs[1]} started"
            try:
                if not filename.endswith(".txt") and filename != "":
                    raise Exception("Неверное расширение файла")
                result = func(*args, **kwargs)
                out = f"{start_} OK!; result: ({result})\n"
            except Exception as err:
                if err == "Неверное расширение файла":
                    out = err
                else:
                    print(args)
                    out = f"{start_}-> ERROR!: {err}  при входных данных: {str(args)}, {str(kwargs)}\n"
            finally:
                if filename == "":
                    print(out)
                else:
                    with open(current_directory, "a", encoding="utf-8") as file:
                        file.write(out)
                    print(out)

        return inner

    return wrapper
