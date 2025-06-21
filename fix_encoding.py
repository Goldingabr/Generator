"""
Вспомогательный скрипт для исправления проблем с кодировкой текстовых файлов
"""
import sys
from utils import fix_file_encoding

def main():
    if len(sys.argv) < 2:
        print("Использование: python fix_encoding.py <имя_файла> [выходной_файл]")
        print("Если выходной_файл не указан, входной файл будет перезаписан.")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"Пытаемся исправить кодировку для: {input_file}")
    
    if fix_file_encoding(input_file, output_file):
        print("Успех! Кодировка файла исправлена.")
    else:
        print("Не удалось исправить кодировку файла.")

if __name__ == "__main__":
    main() 