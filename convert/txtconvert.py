convert = {
    'A': 'А',
    'B': 'Б',
    'C': 'С',
    'D': 'Д',
    'E': 'Е',
    'F': 'Ф',
    'G': 'Г',
    'H': 'X',
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




def convert_latin(txt, to_type):
    '''
    (text) write to text which u going to convert
    (to_type) choose language which u going to convert
    '''
    result = ""
    conversion_dict = {v: k for k, v in convert.items()}  # Создаем словарь с обратным порядком ключей и значений


    if to_type == "latin":
        for char in txt:
            result += conversion_dict.get(char, char)  # Используем get() для поиска соответствующего значения
    elif to_type == "cyrillic":
        txt_modified = ((txt.replace('sh', 'ш').replace('ch', 'ч').replace('Oʻ','У')
                        .replace('oʻ','у').replace('gʻ', 'ғ')).replace('Gʻ','F').replace('Sh', 'Ш')
                        .replace('Ch', 'Ч').replace('yo','ё').replace('ya','я').replace('Yo','Ё').replace('Ya','Я')
                        .replace('yu', 'ю').replace('Yu','Ю').replace('aʼ', 'ъ'))

        for char in txt_modified:
            result += convert.get(char, char)
    else:
        for char in txt:
            result += char

    return result


#salom nima gap
def covnvert_file(language, file):
    '''
    (language) bu yerga til kiritasiz qaysi tilda
    (file) bu yerga failni nomini kiriting
    '''
    try:
        file_content = file.read().decode('utf-8')
        result = convert_latin(file_content, language)
        return result
    except Exception as e:

        return f'''Error reading file: {str(e)}" reading file: {str(e)}'''
