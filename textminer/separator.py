import re

#     ("hello", ['hello']),
#     ("hello world", ['hello', 'world']),
#     ("raggggg hammer dog", ['raggggg', 'hammer', 'dog']),
#     ("18-wheeler tarbox", ['18-wheeler', 'tarbox']),
#     ("12", None),
# ])


def words(text):
    match = re.match(r'(\b(?:\w*\-)?[A-Za-z]+\b)', text)
    if match:
        return re.findall(r'(\b(?:\w*\-)?[A-Za-z]+\b)', text)

def phone_number(text):
    match = re.search(r"""
                     \(?(?P<area_code>\d{3})\)?
                     [ \-\.]?
                     (?P<number>\d{3}
                     [ \-\.]?
                     \d{4})
                     """, text, re.VERBOSE)
    if match:
        gd = match.groupdict()
        digits = gd['number']
        if len(digits) == 7:
            gd['number'] = digits[:3] + '-' + digits[3:]
        elif len(digits) == 8:
            gd['number'] = digits[:3] + '-' + digits[4:]
        return gd
        # TODO: Find a cleaner way to clean up the phone numbers
