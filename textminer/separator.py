import re
import calendar

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

def phone_number(text, return_match=False):
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
        if return_match:
            return gd, match
        return gd
        # TODO: Find a cleaner way to clean up the phone numbers


def money(text):
    match = re.match(r"""^(?P<currency>\$)   # currency group
                          (?P<amount>
                           ((\d{1,3}  # $ and at least 1 digit, 3 max
                           (,\d{3})+)   # commas require 3 trailing digits (opt)
                           |            # unless there are no commas, in
                           (\d+))       # which case we just want 1+ digits
                           (\.\d{2})?)$  # dec require 2 trailing digits (opt)
                           """, text, re.VERBOSE)
    if match:
        gd = match.groupdict()
        gd['amount'] = float(gd['amount'].replace(',',''))
        return gd

def zipcode(text):
    match = re.match(r"""
                        ^(?P<zip>\d{5})
                        (-(?P<plus4>\d{4}))?$
                    """, text, re.VERBOSE)
    if match:
        return match.groupdict()

def date(text):
        # ("9/4/1976", {"month": 9, "day": 4, "year": 1976}),
        # ("1976-09-04", {"month": 9, "day": 4, "year": 1976}),
        # ("2015-01-01", {"month": 1, "day": 1, "year": 2015}),
        # ("02/15/2004", {"month": 2, "day": 15, "year": 2004}),
        # ("9/4", None),
        # ("2015", None),

        # ("2014 Jan 01", {"month": 1, "day": 1, "year": 2014}),
        # ("2014 January 01", {"month": 1, "day": 1, "year": 2014}),
        # ("Jan. 1, 2015", {"month": 1, "day": 1, "year": 2014}),
        # ("07/40/2015", None),
        # ("02/30/2015", None),

    # match = re.match(r"""
    #                     (?P<month>[01]?[0-9])[/-]             # MM/DD/YYYY
    #                     (?P<day>[0-2]?[0-9])[/-]
    #                     (?P<year>\d{4})
    #                     |
    #                     (?P<year2>\d{4})[/-]                   # YYYY/MM/DD
    #                     (?P<month2>[0-2]?[0-9])[/-]
    #                     (?P<day2>[01]?[0-9])
    #                   """, text, re.VERBOSE)

    match = re.match(r"""
                        (^(?P<month>[01]?[0-9])[/-]             # MM/DD/YYYY
                        (?P<day>[0-2]?[0-9])[/-]
                        (?P<year>\d{4}))
                        |
                        (^(?P<year2>\d{4})[\s/-]                 # YYYY/MM/DD
                            ((((?P<month2>[0-2]?[0-9])[\s/-])
                            |
                            (?P<month_word>(\w)+)\s))           # YYYY month DD
                        (?P<day2>[01]?[0-9]))
                        |
                        (^(?P<month_word2>\w+)\.?\s
                        (?P<day3>[0-3]?\d),\s
                        (?P<year3>[\d]{4}))
                      """,
                      text, re.VERBOSE)

    if match:
        gd = match.groupdict()
        if gd.get('year2',False):
            gd['day'] = gd['day2']
            gd['year'] = gd['year2']
            if gd.get('month_word',False):
                gd['month'] = month_to_int(gd['month_word'])
            else:
                gd['month'] = gd['month2']
        elif gd.get('year3'):
            gd['month'] = month_to_int(gd['month_word2'])
            gd['day'] = gd['day3']
            gd['year'] = gd['year3']
        del(gd['day2'])
        del(gd['month2'])
        del(gd['year2'])
        del(gd['month_word'])
        del(gd['month_word2'])
        del(gd['day3'])
        del(gd['year3'])


        gd['day'] = int(gd['day'])
        gd['month'] = int(gd['month'])
        gd['year'] = int(gd['year'])
        return gd

def month_to_int(text):
    months =  {i[1]: i[0] for i in enumerate(calendar.month_name)}
    month_abbrs = {v: k for k,v in enumerate(calendar.month_abbr)}
    if text in months:
        return months[text]
    elif text in month_abbrs:
        return month_abbrs[text]

def email(text):
    match = re.match(r"""
                        (?P<local>[\d\w\.]+)@
                        (?P<domain>\w+\.(com|org|net|us))
                      """,
                      text, re.VERBOSE)
    if match:
        gd = match.groupdict()
        return gd
