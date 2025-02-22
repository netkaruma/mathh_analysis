
import re
from derivatives import functionObjects


# model = a * (funcX) ^ n
# expression = "50/((2/((sin(e^(2x)))^2)) ^ 3)"

def function_parser(express,a = 1,x = "x",n = 1, func = "x^n"):

    """ Парсер математических выражений
    (без умножения/деления/вычитания/сложения  функций)
    """

    express = express.replace(" ", "")

    functions_all = {
        "e\\^": "e^x",
        "\\^": "a^x",
        "ln": "lnx",
        "sin": "sinx",
        "cos": "cosx",
        "tg": "tgx",
        "ctg": "ctgx",
        "arcsin": "arcsinx",
        "arccos": "arccosx",
        "arctg": "arctgx",
        "arcctg": "arcctgx",
        "sh": "shx",
        "ch": "chx",
        "th": "thx",
    }
    if express == "x":
        return functionObjects(a, "x", n, "x")

    # Ищем коэффициент перед функцией, если он отрицательный, он будет в скобочках ()
    match = re.search(r"^\((\-\d+)\)\*?|^(\d+)\*?", express)
    if match:  
        a = int(match.group(1) or match.group(2))*a

    # Если перед функцией стоит только знак минуса, принимает значение коэффициента как "-1"
    if re.search(r"^\(\-[a-z]\)", express):
        a = -1

    # Удаляем знак коэффициента, чтобы было легче анализировать функцию в дальнейшем
    express = re.sub(r"^\((\-\d+)\)\*?|^(\d+)\*?", "", express)  

    # Ищем степенное число
    match = re.search(r"\^([\d]+)$|\^\((\-[\d]+)\)$|\^([\d]+)\)$", express)
    if match:
        n = int(match.group(1) or match.group(2) or match.group(3))

    match = re.fullmatch(r"\/\(([a-z0-9^*/()]+)\^[\d]+\)", express)
    if match:
        n = -n
    # Удаляем степенное число,чтобы было легче анализировать функцию в дальнейшем
        express = match.group(1)
    else:
    # Удаляем степенное число,чтобы было легче анализировать функцию в дальнейшем
        express = re.sub(r"\^[\d]+$|\^\(\-[\d]+\)$", "", express)  

    # Если после всех махинаций остался только "х" и n = 1, то возвращаем фукнцию вида ах
    if re.fullmatch(r"\(?x\)?", express) and n == 1:
        return functionObjects(a, "x", n, "x")

    # Проверяем оставшуюся функцию на константу
    if re.fullmatch(r"\(?\d+\)?", express) and n == 1: 
        return functionObjects(a, f"{a}", n, "const")

    # Ищем функцию и аргумент функции
    match = re.fullmatch(r"[a-z]+\([a-z0-9^*/()]+\)", express)

    # Если есть функция и степень не равняется 1, то это степенная функция
    if match and n != 1:
        return functionObjects(a, function_parser(match.group()), n, func)


    match = re.fullmatch(r"\(([a-z0-9^*/()-]+)\)", express)
    if match and n != 1:
        inner_expr = match.group(1)
        return functionObjects(a, function_parser(inner_expr), n, func)


    match = re.fullmatch(r"\(([a-z0-9^*/()]+)\)", express)
    if match and n == 1:                      # Убираем скобки ->(выражение)<-, если функция не степенная
        inner_expr = match.group(1)
        return function_parser(inner_expr, a = a)


    for i, p in functions_all.items():

        # Если выражение строго равно `имя_функции(x)`
        if re.fullmatch(fr"{i}\(?x\)?", express):
            return functionObjects(a, "x", n, p)

        # Если выражение — `имя_функции(что-то сложное)`
        match = re.fullmatch(fr"{i}\(([a-z0-9^*/()]+)\)", express)
        if match:
            inner_expr = match.group(1)  # Вытаскиваем аргумент функции
            return functionObjects(a, function_parser(inner_expr), n, p)
        
    return functionObjects(a, x, n, func)
