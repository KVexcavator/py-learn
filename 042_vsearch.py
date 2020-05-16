def search_for_vowels(word: str) -> set:
    """Возврашает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word)) 

search_for_vowels('pendulum')
