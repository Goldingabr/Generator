import task_generator
import sys

# Пытаемся импортировать модуль утилит для лучшей работы с файлами
try:
    from utils import write_utf8_file_with_bom
    has_utils = True
except ImportError:
    has_utils = False

def main():
    try:
        if len(sys.argv) > 1:
            num_variants = int(sys.argv[1])
            if num_variants < 1:
                print("Количество вариантов должно быть не менее 1.")
                return
        else:
            num_variants = int(input("Введите количество вариантов для генерации: "))
            if num_variants < 1:
                print("Количество вариантов должно быть не менее 1.")
                return
        
        print(f"Генерация {num_variants} вариантов...")
        variants = task_generator.generate_variants(num_variants)
        
        content = "\n\n" + "="*50 + "\n\n".join(variants)
        
        if has_utils:
            # Используем UTF-8 с BOM для лучшей совместимости с Windows
            write_utf8_file_with_bom("task_variants.txt", content)
        else:
            # Запасной вариант - стандартная кодировка UTF-8
            with open("task_variants.txt", "w", encoding="utf-8") as f:
                f.write(content)
        
        print(f"Сгенерировано {num_variants} вариантов и сохранено в файл task_variants.txt")
        
    except ValueError:
        print("Пожалуйста, введите корректное число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main() 