def search_for_vowels(word):
    """Возврашает булево значение в зависимости от
    присутствия любых гласных."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    if bool(found):
        print('True')
    else:
        print('False')
    return bool(found)    

search_for_vowels('pendulum')
