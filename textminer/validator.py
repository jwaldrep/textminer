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
    return re.match(r"""^\$(\d{1,3})  # $ and at least 1 digit, 3 max

                           (,\d{3})*   # commas require 3 trailing digits (opt)
                           (.\d{2})?$  # dec require 2 trailing digits (opt)
                           """, text, re.VERBOSE)
