import re

def binary(text):
    return re.match(r'[01]+', text)

def binary_even(text):
    if binary(text):
        return re.match(r'.*0$', text)
    return False

def hex(text):
    return re.match(r'\b[0-9A-F]+\b', text)

def word(text):
    return re.match(r'^\b[0-9-]*[a-z-]+\b$', text)

def words(text, count=0):
    word_list = text.split(' ')
    if len(word_list) != count and count != 0:
        return False
    for a_word in word_list:
        if not word(a_word):
            return False
    return True

def phone_number(text):
    return re.match(r'\(?\d{3}\)?[ \-\.]?\d{3}[ \-\.]?\d{4}', text)

def money(text):
    return re.match(r"""^\$((\d{1,3}  # $ and at least 1 digit, 3 max
                           (,\d{3})+)   # commas require 3 trailing digits (opt)
                           |            # unless there are no commas, in
                           (\d+))       # which case we just want 1+ digits
                           (\.\d{2})?$  # dec require 2 trailing digits (opt)
                           """, text, re.VERBOSE)
    # return re.match(r'^\$(((\d{1,3})(,\d{3})+)|(\d+))(\.\d{2})?$', text)

def zipcode(text):
    return re.match(r'^\d{5}(-\d{4})?$', text)

def date(text):
    """
    assert v.date("9/4/1976")
    assert v.date("1976-09-04")
    assert v.date("2015-01-01")
    assert v.date("02/15/2004")
    assert not v.date("9/4")
    assert not v.date("2015")

    assert v.date("2014 Jan 01")
    assert v.date("2014 January 01")
    assert v.date("Jan. 1, 2015")
    assert not v.date("07/40/2015")
    assert not v.date("02/30/2015")

    """
    match = re.match(r"""
                        ((?P<month>[01]?[0-9])[/-]             # MM/DD/YYYY
                        (?P<day>[0-2]?[0-9])[/-]
                        (?P<year>\d{4}))
                        |
                        ((?P<year2>\d{4})[\s/-]                   # YYYY/MM/DD
                            ((((?P<month2>[0-2]?[0-9])[\s/-])
                            |
                            ((\w)+)\s))
                        (?P<day2>[01]?[0-9]))
                        |
                        \w+\.?\s[0-3]?\d,\s[\d]{4}
                      """,
                      text, re.VERBOSE)
    return match
    # re.match(r"""
    #                     [01]?[0-9][/-][0-2]?[0-9][/-]\d{4} |  # MM/DD/YYYY
    #                     \d{4}[/-][0-2]?[0-9][/-][01]?[0-9]    # YY/MM/DDDD
    #                  """, text, re.VERBOSE)

def email(text):
    """
        assert v.email("stroman.azariah@yahoo.com")
        assert v.email("viola91@gmail.com")
        assert v.email("eathel.west@example.org")
        assert v.email("dwehner@harley.us")
        assert v.email("malcolm.haley@hotmail.com")
        assert v.email("ezzard90@hotmail.com")
        assert v.email("legros.curley@gmail.com")
        assert v.email("leatha75@mertz.net")
        assert v.email("bonita43@yahoo.com")
        assert not v.email("")
        assert not v.email("legros.curley")
        assert not v.email("mertz.net")
        assert not v.email("bonita43@")
    """
    match = re.match(r"""
                        [\d\w\.]+@\w+\.(com|org|net|us)
                      """,
                      text, re.VERBOSE)
    return match

def address(text):
    '''
        """This must be a full address with street number, street, city, state,
        and ZIP code. Again, US-only."""
        assert v.address("""368 Agness Harbor
        Port Mariah, MS 63293""")
        assert v.address("""96762 Juluis Road Suite 392
        Lake Imogenemouth, AK 20211""")
        assert v.address("""671 Tawnya Island Apt. 526
        Clementeburgh, AK 82652""")
        assert v.address("""568 Eunice Shoals
        Parishaven, AK 09922-2288""")
        assert v.address("8264 Schamberger Spring, Jordanside, MT 98833-0997")

        assert not v.address("")
        assert not v.address("99132 Kaylah Union Suite 301")
        assert not v.address("Lake Joellville, NH")
        assert not v.address("35981")
    '''
    match = re.match(r"""
                        \d+\s                       # House # plus space
                        (\w+\b\s?)+(\.\s)?          # Words plus .
                        \d*                         # Apt/etc #
                        (\n|,)\s*                   # Newline or , +tabs/spaces
                        (\w+\b\s?)+,                # City,
                        \s[A-Z]{2}\s                # State
                        \d{5}                       # ZIP
                      """,
                      text, re.VERBOSE)
    return match

def palindrome(text):
    if len(text) == 0:
        return False
    text = text.lower().strip().replace(' ','')
    return text == text[::-1]
