import textminer.separator as s

def phone_numbers(text):
    numbers = []
    start = 0
    for _ in range(2):
        gd, match = s.phone_number(text[start:], return_match=True)
        numbers.append(format_phone(gd))
        start = match.end()
    return numbers

def format_phone(groupdict):
    return '({area_code}) {number}'.format(**groupdict)

def emails(text):
    matches = []
    start = 0
    for _ in range(2):
        print('start: ', start)
        gd, match = s.email(text[start:], return_match=True)
        matches.append(format_email(gd))
        start = match.end()
    return matches

def format_email(groupdict):
    return '1'


def palindromes(text):
    return s.palindromes(text)

def format_email(groupdict):
    return '1'
