
class functionObjects:
    """ Класс для представления функции """
    # Все поддерживаемые функции
    # BASIC_FUNCTIONS = {"x", "const"}
    # POWER_FUNCTIONS = {"x^n", "a^x", "e^x"}
    # LOG_FUNCTIONS = {"lnx"}
    # TRIG_FUNCTIONS = {"sinx", "cosx", "tgx", "ctgx", "arcsinx", "arccosx", "arctgx", "arcctgx"}
    # HYPERBOLIC_FUNCTIONS = {"shx", "chx", "thx"}

    def __init__(self, a=1, x=1, n=1, func="const"):
        self.a = a  # Коэффициент перед функцией (если есть)
        self.x = x  # Переменная или вложенная функция
        self.n = n  # Степень (если применимо)
        self.func = func  # Тип функции (например, "sinx", "x^n")

    def differentiate(self):

        """ Прямой вызов метода для дифференциирования обычной функции
        (при умножении,делении,суммировании и разнице функции дифференциируются автоматически)"""

        # Производная константы
        if self.func == "const":
            return "0"

        # Производная x
        if self.func == "x":
            if isinstance(self.x, functionObjects):
                return f"{self.a}({self.x.differentiate()})" 
            return f"{self.a}" 

        # Производная x^n
        if self.func == "x^n":
            if isinstance(self.x, functionObjects):
                if self.n == 2:
                    return f"({self.n*self.a}({self.x})) * ({self.x.differentiate()})"
                return f"({self.n*self.a}({self.x})^{self.n - 1}) * ({self.x.differentiate()})"
            else:
                if self.n == 2:
                    return f"({self.n*self.a}({self.x}))"
                return f"({self.n*self.a}({self.x})^{self.n - 1})"

        # Производная a^x
        if self.func == "a^x":
            if isinstance(self.x, functionObjects):
                return f"({self.a}^({self.x})) * ln({self.a}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}^{self.x} * ln({self.a}))"

        # Производная e^x
        if self.func == "e^x":
            if isinstance(self.x, functionObjects):
                if self.a == 1:
                    return f"e^({self.x}) * ({self.x.differentiate()})"
                return f"({self.a}*e^{self.x}) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"(e^{self.x})"
                return f"({self.a}e^{self.x})"

        # Производная ln(x)
        if self.func == "lnx":
            if isinstance(self.x, functionObjects):
                return f"({self.a}/{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}/{self.x})"

        # Производная sin(x)
        if self.func == "sinx":
            if isinstance(self.x, functionObjects):
                if self.a == 1:
                    return f"cos({self.x}) * ({self.x.differentiate()})"
                return f"{self.a}cos({self.x}) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"cos({self.x})"
                return f"{self.a}cos({self.x})"

        # Производная cos(x)
        if self.func == "cosx":

            variations_flag = {
                "neg":"-",
                "pos":""
            }
            if self.a < 0:
                flag = "pos"
            elif self.a > 0:
                flag = "neg"
            if isinstance(self.x, functionObjects):
                if self.a == 1:
                    return f"({variations_flag[flag]}sin({self.x}) * ({self.x.differentiate()})"
                return f"({variations_flag[flag]}{self.a}sin({self.x})) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"({variations_flag[flag]}sin({self.x}))"
                return f"{variations_flag[flag]}{self.a}sin({self.x})"

        # Производная tg(x)
        if self.func == "tgx":
            if isinstance(self.x, functionObjects):
                return f"({self.a} / cos^2({self.x})) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / cos^2({self.x}))"

        # Производная ctg(x)
        if self.func == "ctgx":
            if isinstance(self.x, functionObjects):
                return f"({-self.a} / sin^2({self.x})) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sin^2({self.x}))"

        # Производная arcsin(x)
        if self.func == "arcsinx":
            if isinstance(self.x, functionObjects):
                return f"({self.a} / sqrt(1 - ({self.x})^2) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / sqrt(1 - ({self.x})^2)"

        # Производная arccos(x)
        if self.func == "arccosx":
            if isinstance(self.x, functionObjects):
                return f"({-self.a} / sqrt(1 - ({self.x})^2) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sqrt(1 - ({self.x})^2)"

        # Производная arctg(x)
        if self.func == "arctgx":
            if isinstance(self.x, functionObjects):
                return f"({self.a} / sqrt(1 - {self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / sqrt(1 - {self.x})"

        # Производная arcctg(x)
        if self.func == "arcctgx":
            if isinstance(self.x, functionObjects):
                return f"({-self.a} / sqrt(1 - {self.x}) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sqrt(1 - {self.x})"

        # Производная sh(x)
        if self.func == "shx":
            if isinstance(self.x, functionObjects):
                return f"({self.a}ch{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}ch{self.x})"

        # Производная ch(x)
        if self.func == "chx":
            if isinstance(self.x, functionObjects):
                return f"({self.a}sh{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}sh{self.x})"

        # Производная th(x)
        if self.func == "thx":
            if isinstance(self.x, functionObjects):
                return f"({self.a} / ch^2({self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / ch^2({self.x})"

        else:
            return "Неизвестная функция"

    def __str__(self):
        """Корректное строковое представление"""
        FUNCTIONS_ALL = {
            "x":"x",
            "x^n":f"({self.x})",
            "e^x":f"e^({self.x})",
            "lnx":f"ln({self.x})",
            "sinx":f"sin({self.x})",
            "cosx":f"cos({self.x})",
            "tgx":f"tg({self.x})",
            "ctgx":f"ctg({self.x})",
            "arcsinx":f"arcsin({self.x})",
            "arccosx":f"arccos({self.x})",
            "arctgx":f"arctg({self.x})",
            "arcctgx":f"arcctg({self.x})",
            "shx":f"sh({self.x})",
            "chx":f"ch({self.x})",
            "thx":f"th({self.x})",
        }

        a_str = f"({self.a})" if self.a < 0 else str(self.a)
        n_str = f"({self.n})" if self.n < 0 else str(self.n)

        if self.func in FUNCTIONS_ALL:


            if self.a != 1 and self.n != 1:
                return f"{a_str}{FUNCTIONS_ALL[self.func]}^{n_str}"
            if self.a != 1 and self.n == 1:
                return f"{a_str}{FUNCTIONS_ALL[self.func]}"
            if self.a == 1 and self.n != 1:
                return f"{FUNCTIONS_ALL[self.func]}^{n_str}"
            if self.a == 1 and self.n == 1:
                return f"{FUNCTIONS_ALL[self.func]}"

        elif self.func == "a^x":
            return f"{a_str}^({self.x})"
        
        elif self.a != 0:
            return f"{a_str}"

        return "Некорректное выражение"