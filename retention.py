KEYWORDS = ["AI", "NEW", "TODAY", "NOBODY", "BREAKING", "CHANGES"]

def is_keyword(word):
    return word.upper().strip(".,!?") in KEYWORDS
