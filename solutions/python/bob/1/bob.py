def response(hey_bob):
    stripped_string = hey_bob.strip()
    if stripped_string == '':
        return "Fine. Be that way!"
    elif(stripped_string[len(stripped_string)-1] == '?' and  not(stripped_string.isupper())):
        return 'Sure.'
    elif (stripped_string.isupper() and stripped_string[len(stripped_string)-1] != '?'):
        return 'Whoa, chill out!'
    elif (stripped_string.isupper() and stripped_string[len(stripped_string)-1] == '?'):
        return "Calm down, I know what I'm doing!"
    return 'Whatever.'
    pass
