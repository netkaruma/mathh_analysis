
from typing import Tuple, List

# Дискретная производная по точкам
def discrete_derivative(y,y_0,x,x_0):
    """Дискретный дифференциал по точкам где первая точка (y,x)
    а вторая точка (y_0,x_0)"""
    return (y-y_0)/(x-x_0)

# Дискретная производная с функцией
def derivative_func(func,x,x_0):
    """Определенный дифференциал для дискретных значений функции
        ('x' и 'x_0') - Область дифференциирования на оси ординат"""

    return (func(x)-func(x_0))/(x-x_0)


# Дискретный интеграл методом трапеций по точкам.
def discrete_integral(func: Tuple[List[float], List[float]]):
    sum = 0
    for i in range(len(func[0]) - 1):
        sum += ((func[1][i] + func[1][i + 1])/2)*(func[0][i + 1] - func[0][i])
    return sum



# Определенный интеграл
def definite_integral(func,positive_axis,negative_axis=0,accuracy=1):
    massive_x = []
    massive_y = []
    for i in range(negative_axis*accuracy,accuracy*(positive_axis+1)-(accuracy-1)):

        massive_x.append(i/accuracy)
        massive_y.append(func(i/accuracy))

    return discrete_integral([massive_x, massive_y])


class derivative_Base:
    """ Класс для представления функции для дифференциирования/интегрирования """
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
            if isinstance(self.x, derivative_Base):
                return f"{self.a}({self.x.differentiate()})" 
            return f"{self.a}" 

        # Производная x^n
        if self.func == "x^n":
            if isinstance(self.x, derivative_Base):
                if self.n == 2:
                    return f"({self.n*self.a}{self.x}) * ({self.x.differentiate()})"
                return f"({self.n*self.a}{self.x}^{self.n - 1}) * ({self.x.differentiate()})"
            else:
                if self.n == 2:
                    return f"({self.n*self.a}{self.x})"
                return f"({self.n*self.a}{self.x}^{self.n - 1})"

        # Производная a^x
        if self.func == "a^x":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}^({self.x})) * ln({self.a}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}^{self.x} * ln({self.a}))"

        # Производная e^x
        if self.func == "e^x":
            if isinstance(self.x, derivative_Base):
                if self.a == 1:
                    return f"e^({self.x}) * ({self.x.differentiate()})"
                return f"({self.a}*e^{self.x}) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"(e^{self.x})"
                return f"({self.a}e^{self.x})"

        # Производная ln(x)
        if self.func == "lnx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}/{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}/{self.x})"

        # Производная sin(x)
        if self.func == "sinx":
            if isinstance(self.x, derivative_Base):
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
            if isinstance(self.x, derivative_Base):
                if self.a == 1:
                    return f"({variations_flag[flag]}sin({self.x}) * ({self.x.differentiate()})"
                return f"({variations_flag[flag]}{self.a}sin({self.x})) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"({variations_flag[flag]}sin({self.x}))"
                return f"{variations_flag[flag]}{self.a}sin({self.x})"

        # Производная tg(x)
        if self.func == "tgx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a} / cos^2({self.x})) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / cos^2({self.x}))"

        # Производная ctg(x)
        if self.func == "ctgx":
            if isinstance(self.x, derivative_Base):
                return f"({-self.a} / sin^2({self.x})) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sin^2({self.x}))"

        # Производная arcsin(x)
        if self.func == "arcsinx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a} / sqrt(1 - ({self.x})^2) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / sqrt(1 - ({self.x})^2)"

        # Производная arccos(x)
        if self.func == "arccosx":
            if isinstance(self.x, derivative_Base):
                return f"({-self.a} / sqrt(1 - ({self.x})^2) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sqrt(1 - ({self.x})^2)"

        # Производная arctg(x)
        if self.func == "arctgx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a} / sqrt(1 - {self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / sqrt(1 - {self.x})"

        # Производная arcctg(x)
        if self.func == "arcctgx":
            if isinstance(self.x, derivative_Base):
                return f"({-self.a} / sqrt(1 - {self.x}) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sqrt(1 - {self.x})"

        # Производная sh(x)
        if self.func == "shx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}ch{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}ch{self.x})"

        # Производная ch(x)
        if self.func == "chx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}sh{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}sh{self.x})"

        # Производная th(x)
        if self.func == "thx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a} / ch^2({self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / ch^2({self.x})"

        else:
            return "Неизвестная функция"

    def integrate(self):
        """ Прямой вызов метода для интегрирования обычной функции
        (при умножении,делении,суммировании и разнице функции интегрируются автоматически)"""

        if self.func == "0dx":
            return "C"
        # Интеграл константы
        if self.func == "dx":
            return "x"

        # Интеграл 
        if self.func == "const":
            if isinstance(self.x, derivative_Base):
                return f"{self.a}*({self.x.differentiate()})" 
            return f"{self.a}" 

        # Производная x^n
        if self.func == "x^n":
            if isinstance(self.x, derivative_Base):
                if self.n == 2:
                    return f"({self.n*self.a}*{self.x}) * ({self.x.differentiate()})"
                return f"({self.n*self.a}*{self.x}^{self.n - 1}) * ({self.x.differentiate()})"
            else:
                if self.n == 2:
                    return f"({self.n*self.a}*{self.x})"
                return f"({self.n*self.a}*{self.x}^{self.n - 1})"

        # Производная a^x
        if self.func == "a^x":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}^({self.x})) * ln({self.a}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}^{self.x} * ln({self.a}))"

        # Производная e^x
        if self.func == "e^x":
            if isinstance(self.x, derivative_Base):
                if self.a == 1:
                    return f"e^({self.x}) * ({self.x.differentiate()})"
                return f"({self.a}*e^{self.x}) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"(e^{self.x})"
                return f"({self.a}*e^{self.x})"

        # Производная ln(x)
        if self.func == "lnx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}/{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}/{self.x})"

        # Производная sin(x)
        if self.func == "sinx":
            if isinstance(self.x, derivative_Base):
                if self.a == 1:
                    return f"cos({self.x}) * ({self.x.differentiate()})"
                return f"{self.a}*cos({self.x}) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"cos({self.x})"
                return f"{self.a}*cos({self.x})"

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
            if isinstance(self.x, derivative_Base):
                if self.a == 1:
                    return f"({variations_flag[flag]}sin({self.x}) * ({self.x.differentiate()})"
                return f"({variations_flag[flag]}{self.a}*sin({self.x})) * ({self.x.differentiate()})"
            else:
                if self.a == 1:
                    return f"({variations_flag[flag]}sin({self.x}))"
                return f"{variations_flag[flag]}{self.a}*sin({self.x})"

        # Производная tg(x)
        if self.func == "tgx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a} / cos^2({self.x})) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / cos^2({self.x}))"

        # Производная ctg(x)
        if self.func == "ctgx":
            if isinstance(self.x, derivative_Base):
                return f"({-self.a} / sin^2({self.x})) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sin^2({self.x}))"

        # Производная arcsin(x)
        if self.func == "arcsinx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a} / sqrt(1 - ({self.x})^2) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / sqrt(1 - ({self.x})^2)"

        # Производная arccos(x)
        if self.func == "arccosx":
            if isinstance(self.x, derivative_Base):
                return f"({-self.a} / sqrt(1 - ({self.x})^2) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sqrt(1 - ({self.x})^2)"

        # Производная arctg(x)
        if self.func == "arctgx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a} / sqrt(1 - {self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a} / sqrt(1 - {self.x})"

        # Производная arcctg(x)
        if self.func == "arcctgx":
            if isinstance(self.x, derivative_Base):
                return f"({-self.a} / sqrt(1 - {self.x}) * ({self.x.differentiate()})"
            else:
                return f"({-self.a} / sqrt(1 - {self.x})"

        # Производная sh(x)
        if self.func == "shx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}*ch{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}*ch{self.x})"

        # Производная ch(x)
        if self.func == "chx":
            if isinstance(self.x, derivative_Base):
                return f"({self.a}*sh{self.x}) * ({self.x.differentiate()})"
            else:
                return f"({self.a}*sh{self.x})"

        # Производная th(x)
        if self.func == "thx":
            if isinstance(self.x, derivative_Base):
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
        if self.func in FUNCTIONS_ALL:

            a_str = f"({self.a})" if self.a < 0 else str(self.a)
            n_str = f"({self.n})" if self.n < 0 else str(self.n)

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

        return "Некорректное выражение"


    # def __truediv__(self,other):
    #     return f"({self.differentiate()} * {other} - {self} * {other.differentiate()})/({other})^2"

    # def __mul__(self,other):
    #     return f"{self.differentiate()} * {other} + {self} * {other.differentiate()}"

    # def __add__(self,other):
    #     return f"{self.differentiate()} + {other.differentiate()}"

    # def __sub__(self,other):
    #     return f"{self.differentiate()} - {other.differentiate()}"



# Тестирование с простыми и сложными функциями

        
# f1 = derivative_Base(3, "x", None, "a^x")  # 3^x
# f2 = derivative_Base(2, f1, None, "sinx")  # 2sin(3^x)
# f3 = derivative_Base(4, f2, None, "a^x")  # 4^(2sin(3x^3))

# ff1 = derivative_Base(3, "x", 3, "x^n")  # 3x^3
# ff2 = derivative_Base(2, ff1, None, "sinx")  # 2sin(3x^3)
# ff3 = derivative_Base(4, ff2, None, "lnx")  # 4ln(2sin(3x^3))
# f12 = derivative_Base(3, "x", 3, "a^x")  # 3x^3
# ----

# answer = f3 + ff3 * f12

# print(ff3)
# print(ff3.differentiate())
# print(f3)
# print(f3.differentiate())
# # print(answer)
# import sympy as sp

# Определяем переменную
# x = sp.Symbol('x')

# Определяем функцию
# f = ((4*sp.log(2*sp.sin(3*x**3)**3)**2)*sp.log(3))

# Вычисляем производную
# dfdx = sp.diff(f, x)

# Выводим результат
# print(dfdx)

# # print(f3)


# import sympy as sp
# # Определение переменной
# x = sp.symbols('x')

# # Определение функции
# f = sp.sin(x**2)

# # Вычисление неопределенного интеграла
# integral = sp.integrate(f, x)
# print(integral)
