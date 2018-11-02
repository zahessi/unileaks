#  Определить является ли одна строка перестановкой другой

def mutated_string(original, mutated):
    return sorted(original) == sorted(mutated)

assert mutated_string('asd', 'dsa') == True