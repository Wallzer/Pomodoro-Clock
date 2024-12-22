import sympy as sp
error = "неверное значение"
error = error.upper()
error += " + даун"
x = sp.symbols('x')
a = 0

function_input = input("Введите функцию от x (например, sin(x), x2, e): ")


function_input = function_input.replace('e^x', 'exp(x)')
function_input = function_input.replace('^', '**')

f = sp.sympify(function_input)


is_definite = input("Вы хотите вычислить определенный интеграл? (да/нет): ").lower()

if is_definite == 'да':
    # Ввод пределов интегрирования
    lower_limit = float(input("Введите нижний предел интегрирования: "))
    upper_limit = float(input("Введите верхний предел интегрирования: "))
    # Вычисление определенного интеграла
    definite_integral = sp.integrate(f, (x, lower_limit, upper_limit))
    print(f"Определенный интеграл от {lower_limit} до {upper_limit}: {definite_integral}")
elif is_definite == 'нет':
    # Вычисление неопределенного интеграла
    indefinite_integral = sp.integrate(f, x)
    count=str(indefinite_integral)
    print(f"Неопределенный интеграл: {indefinite_integral} + C")
else:
     print(error)