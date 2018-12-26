def clean_text(txt):
    """ takes a string of text txt as a parameter and returns a
    list containing the words in txt after it has been “cleaned”."""
    for i in txt:
        if i in ['.', '!', '?', ',', "'", '-', '_', '[]', '(', ')', ';', ':']:
            txt.replace(i, '')
    return txt.lower()
