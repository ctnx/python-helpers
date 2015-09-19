def to_str(bytes_or_str):
    """ (bytes/str) -> str
    convert from bytes (raw 8 bit) to string (Unicode) using UTF-8
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    """ (str/bytes) -> bytes
    convert from string (Unicode) to bytes (raw 8 bit) using UTF-8
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf8')
    else:
        value = bytes_or_str
    return value

