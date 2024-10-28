from masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: str) -> str:
    """Возвращать строку с замаскированным номером. Для карт и счетов используйте разные типы маскировки."""

    card_attributes = account_card.split()
    # определяем card_attributes это номер карты или счет, и выполняем соответствующею логику
    if len(card_attributes[-1]) == 16:
        card_attributs = card_attributes[0:-1]
        card_attribut = " ".join(card_attributs)
        card_attributs = card_attribut + " " + get_mask_card_number(int(card_attributes[-1]))
    elif len(card_attributes[-1]) == 20:
        card_attributs = card_attributes[0:-1]
        card_attribut = " ".join(card_attributs)
        card_attributs = card_attribut + " " + get_mask_account(int(card_attributes[-1]))
    else:
        card_attributs = "Проверти, правильность ввода данных!"

    return card_attributs


def get_date(date_line: str) -> str:
    """Возвращает из строки дату в формате: День.Месяц.Год"""

    date_e = date_line[0:date_line.find('T')]
    date_es = date_e.split("-")
    dates = date_es[2] + "." + date_es[1] + "." + date_es[0]
    return dates



print()
print(get_date("2024-03-11T02:26:18.671407"))
print()
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
