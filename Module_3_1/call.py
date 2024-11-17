calls = 0
def count_calls():
    global calls
    calls += 1
    return calls




def string_info(string : str) -> tuple:
    count_calls()
    if type(string) != str:
        return tuple(['Тип текста - не строка!'])
    if not string.strip:
        return tuple(['Текст пуст, бро!'])
    lower_case = 0
    upper_case = 0
    for char in string:
        if char.isalpha() and char.islower():
            lower_case += 1
        elif char.isalpha() and char.isupper():
            upper_case += 1
    return "lower", lower_case, "upper", upper_case

def is_contains(string, list_to_search):
    count_calls()
    is_contained = False
    for substring in list_to_search:
        if substring in string:
            is_contained = True
    return is_contained


print(string_info('Привет'))

print(string_info('HaliUuja'))

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)












