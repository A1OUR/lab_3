def calculate_commission(amount: int) -> float:
    """
    Рассчитывает комиссию для денежного перевода.
    
    Args:
        amount (int/float): Сумма перевода (от 100 до 50 000 руб.)
    
    Returns:
        float: Размер комиссии
    
    Raises:
        TypeError: Если передано нечисловое значение
        ValueError: Если сумма не входит в допустимый диапазон
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма перевода должна быть числовым значением.")
    
    if amount < 100 or amount > 50000:
        raise ValueError("Сумма перевода должна быть от 100 до 50 000 руб.")
    
    if amount <= 1000:
        return 50.0
    elif amount <= 20000:
        return 100.0
    elif amount <= 40000:
        return 200.0 + (amount * 0.01)
    else:
        return 500.0