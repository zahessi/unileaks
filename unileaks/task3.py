# Задача: Напишите метод, заменяющий все пробелы в строке символами '%20'.
# Можно предположить, что длина строки позволяет сохранить 
# дополнительные символы и «истинная» длина строки известна. 

import re

# regular expressions
def replace_spaces(s):
    return re.sub(' ', '%20', s)

# without them
def replace_spaces2(s):
    return ''.join(map(lambda i: '%20' if i == ' ' else i, list(s)))

assert replace_spaces2('Mr John Smith ') == 'Mr%20John%20Smith%20'