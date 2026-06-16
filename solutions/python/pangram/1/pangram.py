def is_pangram(sentence):
    map = {}
    for char in sentence:
        if not char.isalpha():
            continue
        map[char.lower()] = char
    return len(map) == 26
