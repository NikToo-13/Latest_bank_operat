def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    В случаи ошибки возвращает ошибку"""

    card_number1 = str(card_number)
    if len(card_number1) == 16:
        card_mask = card_number1[0:4] + " " + card_number1[4:6] + "** **** " + card_number1[12:16]
    else:
        card_mask = "Проверти, правильность ввода номера карты!"
    return card_mask


def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    В случаи ошибки возвращает ошибку"""

    account1 = str(account)
    if len(account1) == 20:
        account_mask = "**" + account1[-4:]
    else:
        account_mask = "Проверти, правильность ввода счета!"
    return account_mask
