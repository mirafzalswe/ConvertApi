import re

CONVERSION_MAP = {
    'A': 'А',
    'B': 'Б',
    'C': 'С',
    'D': 'Д',
    'E': 'Е',
    'F': 'Ф',
    'G': 'Г',
    'H': 'Х',
    'I': 'И',
    'J': 'Ж',
    'K': 'К',
    'L': 'Л',
    'M': 'М',
    'N': 'Н',
    'O': 'О',
    'P': 'П',
    'Q': 'К',
    'R': 'Р',
    'S': 'С',
    'T': 'Т',
    'U': 'У',
    'V': 'В',
    'W': 'В',
    'X': 'Х',
    'Y': 'Й',
    'Z': 'З',
    'a': 'а',
    'b': 'б',
    'c': 'с',
    'd': 'д',
    'e': 'е',
    'f': 'ф',
    'g': 'г',
    'h': 'х',
    'i': 'и',
    'j': 'ж',
    'k': 'к',
    'l': 'л',
    'm': 'м',
    'n': 'н',
    'o': 'о',
    'p': 'п',
    'q': 'к',
    'r': 'р',
    's': 'с',
    't': 'т',
    'u': 'у',
    'v': 'в',
    'w': 'в',
    'x': 'x',
    'y': 'й',
    'z': 'з',
}

REVERSE_CONVERSION_MAP = {v: k for k, v in CONVERSION_MAP.items()}

def convert_latin(txt, to_type):
    """
    Convert text between Latin and Cyrillic alphabets.

    :param txt: Text to be converted.
    :param to_type: Target type of conversion ('latin' or 'cyrillic').
    :return: Converted text.
    """
    result = ""

    if to_type == "latin":
        for char in txt:
            result += REVERSE_CONVERSION_MAP.get(char, char)
    elif to_type == "cyrillic":
        txt_modified = re.sub(r'sh|ch|Oʻ|oʻ|gʻ|Gʻ|Sh|Ch|yo|ya|Yo|Ya|yu|Yu|aʼ', lambda x: CONVERSION_MAP[x.group()], txt)
        result = ''.join(CONVERSION_MAP.get(char, char) for char in txt_modified)
    else:
        result = txt

    return result

def convert_file(language, file_path):
    """
    Convert the content of a file between Latin and Cyrillic alphabets.

    :param language: Target type of conversion ('latin' or 'cyrillic').
    :param file_path: Path to the file.
    :return: Converted text or error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            result = convert_latin(file_content, language)
        return result
    except Exception as e:
        return f"Error reading file: {str(e)}"
