

def search_vowels(phrase: str) -> set:
    """Возврашает гласные, найденные в указанной фразе."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_letters(phrase: str, letters:str='aeiou') -> set:
    """Возврашает множество букв из 'letters', найденных в указанной фразе."""
    return set(letters).intersection(set(phrase)) 


