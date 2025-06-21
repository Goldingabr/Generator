"""
Вспомогательные функции для работы с файлами с правильной кодировкой
"""

def write_utf8_file_with_bom(filename, content):
    """
    Запись файла с кодировкой UTF-8 и маркером BOM, который помогает Windows правильно распознавать кириллицу
    
    Аргументы:
        filename (str): Путь к файлу
        content (str): Содержимое для записи в файл
    """
    with open(filename, 'wb') as f:
        # Записываем UTF-8 BOM
        f.write(b'\xef\xbb\xbf')
        # Записываем содержимое как UTF-8
        f.write(content.encode('utf-8'))
    
    print(f"Файл сохранен с кодировкой UTF-8 BOM: {filename}")

def fix_file_encoding(input_file, output_file=None):
    """
    Исправление кодировки файла путем его чтения и записи с правильной кодировкой UTF-8 BOM
    
    Аргументы:
        input_file (str): Путь к входному файлу
        output_file (str, optional): Путь к выходному файлу. Если None, перезаписывает входной файл.
    """
    if output_file is None:
        output_file = input_file
    
    try:
        # Пробуем разные кодировки
        encodings = ['utf-8', 'cp1251', 'latin-1']
        content = None
        
        for encoding in encodings:
            try:
                with open(input_file, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        
        if content is None:
            print(f"Не удалось декодировать файл {input_file} ни с одной из поддерживаемых кодировок")
            return False
        
        # Записываем с UTF-8 BOM
        write_utf8_file_with_bom(output_file, content)
        return True
    except Exception as e:
        print(f"Ошибка при исправлении кодировки файла: {e}")
        return False 