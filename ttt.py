# Импортируем модуль os
import os
from dotenv import load_dotenv

load_dotenv()

# Создаём цикл, чтобы вывести все переменные среды
# print('The keys and values of all environment variables:')
# os.environ['LVI'] = '1111111111111111111111111'

# for key in os.environ:
#  print(key, '=>', os.environ[key])

# Выводим значение одной переменной
print('The value of LVI is: ', os.environ.get('LVI'))

print('The value of LVI is: ', os.getenv("LVI"))

print('Привет')
