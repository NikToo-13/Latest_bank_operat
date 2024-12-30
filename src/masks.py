import logging

from project_sys import PATH_HOME

path_ = f"{PATH_HOME}/logs/masks.log"
logger = logging.getLogger("masks")
file_handler = logging.FileHandler(path_, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    В случаи ошибки возвращает ошибку"""

    legend_s = " Функция: get_mask_card_number -> "
    card_number1 = str(card_number)
    logger.info(f"{legend_s}Принимаем номер карты: {card_number1}")
    try:
        if len(card_number1) == 16:
            card_mask = card_number1[0:4] + " " + card_number1[4:6] + "** **** " + card_number1[12:16]
            logger.info(f"{legend_s}Создаем маску для номера карты: {card_mask}")
        else:
            raise Exception(f"{legend_s}Проверти, правильность ввода номера карты!")
        return card_mask
    except Exception as er:
        logger.warning(f"{legend_s}Ошибка: {er}")
        return str(er)


def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    В случаи ошибки возвращает ошибку"""

    legend_s = " Функция: get_mask_account -> "
    try:
        account1 = str(account)
        logger.info(f"{legend_s}Принимаем номер счета: {account1}")
        if len(account1) == 20:
            account_mask = "**" + account1[-4:]
            logger.info(f"{legend_s}Создаем маску для номера счета: {account_mask}")
        else:
            raise Exception(f"{legend_s}Проверти, правильность ввода счета!")
        return account_mask
    except Exception as er:
        logger.warning(f"{legend_s}Ошибка: {er}")
        return str(er)
