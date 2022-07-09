

print ("Programm by Filatov & Tkachenko")

# Список констант
P = 3.14159
R = 8.3144
e = 2.71828

# Введение молярной массы пользователем
import math
print ("Введите молярную массу в г/моль")
m = input("Молярная масса = ")
mm = "г/моль"
M = (int(m) / int(1000))
print(f"{M} кг/моль")

# Проверка значения молярной массы и ввод температуры
if int(m) > int(0):
 print ("Введите абсолютную температуру в кельвинах")
 t = input("Абсолютная температура = ")
 T = float(t)
 print (T)

# Заранее заданые параметры формулы для облегчения кода
o = 4.0 * P
h = (M / (2.0 * P * R * T)) ** 1.5
u = (2.0 * R * T) / M
n = 1.0 / e

z = o * h * u * n

# Анализ введенных данных и вывод на экран
print("1. Область визначення f(V) множина дійсних чисел D(f(V)) = R" )
print(f"2. Область значень ф-ії E(f(V)) = [0; {z}]")
print("3. Функція загального виду")
j = math.sqrt(u)
print(f"4. f(V)🠕, V є [0; {j}])")
print("5. Не періодична")
print(f"6. Найбільшого значення набуває при V = {j}")
print(f"7. Площа під графіком функції дорівнює 1")

# Запуск директории matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib import pylab
import matplotlib.ticker as ticker                               
import numpy as np

# Формула у и заданые параметры х
x = np.linspace(0, 35, 30)
y = 4 * P * ((M / 2.0 * P * R * T) ** 1.5) * (x ** 2.0) * (e ** (-M * (x ** 2.0)) / 2.0 * R * T)
fig, ax = plt.subplots(figsize=(12, 10))


# Линии основной сетки:
ax.grid(which='major',linewidth=1.0,
        color = 'k')

# Видимость вспомогательных делений:
ax.minorticks_on()

# Подписи абцисы, ординаты и заголовка графика
ax.set_title("График распределения молекул по скоростям", fontsize=16)
ax.set_xlabel("V", fontsize=16)        
ax.set_ylabel("f(V)", fontsize=16)

# Линии вспомогательной сетки
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

# Параметры основной линии
ax.plot(x, y, label="f(V)", color = 'r', linewidth = 3)

# Включение "легенды"
ax.legend()

frame = pylab.gca()
frame.axes.get_xaxis().set_ticklabels([])
frame.axes.get_yaxis().set_ticklabels([])

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

plt.show()
