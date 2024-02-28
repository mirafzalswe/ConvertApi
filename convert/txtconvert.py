import re
CONVERSION_LETTERS = {
    'Sh': 'Ш',
    'Ch': 'Ч',
    "G'": 'Ғ',
    'Gʻ': 'Ғ',
    'Yo': 'Ё',
    'Ya': 'Я',
    'Yu': 'Ю',
    'Ts': 'Ц',
    'Shch': 'Щ',
    'A': 'А',
    'B': 'Б',
    'C': 'С',
    'D': 'Д',
    'E': 'Е',
    'F': 'Ф',
    'G': 'Г',
    'H': 'Ҳ',
    'I': 'И',
    'J': 'Ж',
    'K': 'К',
    'L': 'Л',
    'M': 'М',
    'N': 'Н',
    'O': 'О',
    'P': 'П',
    'Q': 'Қ',
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
    'h': 'ҳ',
    'i': 'и',
    'j': 'ж',
    'k': 'к',
    'l': 'л',
    'm': 'м',
    'n': 'н',
    'o': 'о',
    'p': 'п',
    'q': 'қ',
    'r': 'р',
    's': 'с',
    't': 'т',
    'u': 'у',
    'v': 'в',
    'w': 'в',
    'x': 'х',
    'y': 'й',
    'z': 'з',
    'sh': 'ш',
    'ch': 'ч',
    "g'": 'ғ',
    "gʻ": 'ғ',
    'yo': 'ё',
    'ya': 'я',
    'yu': 'ю',
    'zh': 'ж',
    'kh': 'х',
    'ts': 'ц',
    'sch': 'щ',
    # 'aʼ': 'аъ',
    'Oʻ': 'ў',
    "O'": 'ў',
    'oʻ': 'ў',
    "o'": 'ў',
    '’': 'ъ',
    'ʼ':'ъ'
}



REVERSE_CONVERSION_LETTERS = {v: k for k, v in CONVERSION_LETTERS.items()}

def convert_latin(txt:str, to_type:str):
    """
    Convert text between Latin and Cyrillic alphabets.

    :param txt: Text to be converted.
    :param to_type: Target type of conversion ('latin' or 'cyrillic').
    :return: Converted text.
    """
    result = ""

    if to_type == "latin":
        for char in txt:
            result += REVERSE_CONVERSION_LETTERS.get(char, char)
    elif to_type == "cyrillic":
        txt_modified = re.sub(r"Sh|SH|CH|Ch|ch|sh|o'|O'|G'|g'|gʻ|Gʻ|oʻ|Oʻ|kh|Kh|KH|ʻ|zh|Zh|ZH|Ts|ts|sch|SCh|SCH|Sch|Yo|Yu|Ya|yo|yo|ya",
                              lambda x: CONVERSION_LETTERS[x.group()], txt)
        for char in txt_modified:
            result += CONVERSION_LETTERS.get(char, char)
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
        return f"Error : {str(e)}"