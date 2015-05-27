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


# if __name__ == '__main__':
#     pass
