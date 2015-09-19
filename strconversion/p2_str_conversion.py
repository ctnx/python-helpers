# python 2
def to_unicode(unicode_or_str):
    """ (unicode/ str) -> unicode
    Convert to Unicode using UTF-8
    """
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value


def to_str(unicode_or_str):
    """ (unicode/ str) -> str
    Convert to String using UTF-8
    """
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value
