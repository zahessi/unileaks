# Дана строка, слова в ней указаны через пробел. Вывести слова в порядке убывания длины.
# Пример: "My favorite music band is Rammstein",
# Вывод: 1. Rammstein 2. favorite 3. music 4. band 5. My 6. is


def length_of_words(s):
    return sorted(s.split(" "))

assert length_of_words("My favorite music band is Rammstein") == ['Rammstein','favorite','music','band','My', 'is'] \
or  ['Rammstein','favorite','music','band','is', 'My']