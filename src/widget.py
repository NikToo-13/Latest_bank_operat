from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Возвращать строку с замаскированным номером.
    Для карт и счетов используйте разные типы маскировки."""

    card_attributes = account_card.split()
    if len(card_attributes) != 0:
        # определяем card_attributes это номер карты или счет, и выполняем соответствующею логику
        if len(card_attributes[-1]) == 16:
            card_attribut = " ".join(card_attributes[0:-1])
            card_attributs = card_attribut + " " + get_mask_card_number(int(card_attributes[-1]))
        elif len(card_attributes[-1]) == 20:
            card_attribut = " ".join(card_attributes[0:-1])
            card_attributs = card_attribut + " " + get_mask_account(int(card_attributes[-1]))
        else:
            card_attributs = "Проверти, правильность ввода данных!"
        return card_attributs
    return "Проверти, правильность ввода данных!"


def get_date(date_line: str) -> str:
    """Возвращает из строки дату в формате: День.Месяц.Год"""

    try:
        if len(date_line) == 26:
            if date_line.find("T") == 10:
                if date_line[4] == "-" and date_line[7] == "-":
                    date_e = date_line[0 : date_line.find("T")]
                    date_es = date_e.split("-")
                    if 0 < int(date_es[2]) < 32 and 0 < int(date_es[1]) < 13:
                        if date_es[2].isdigit() and date_es[1].isdigit() and date_es[0].isdigit():
                            dates = date_es[2] + "." + date_es[1] + "." + date_es[0]
                            return dates
        return "Проверти, правильность ввода данных!"
    except Exception:
        return "Проверти, правильность ввода данных!"
