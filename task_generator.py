import random

def generate_task1():
    """Генерация случайной строки для задачи 1 (суффиксы, префиксы, подстроки)"""
    # Ensure length is always 7 or 8 digits
    length = random.randint(7, 8)
    
    # Generate a string without limitation first
    result = ''.join(random.choice('0123') for _ in range(length))
    
    # Check for more than 2 consecutive zeros and fix if needed
    while '000' in result:
        # Find the position of three consecutive zeros
        pos = result.find('000')
        # Replace the third zero with a random non-zero digit
        replacement = random.choice('123')
        # Replace in the string
        result = result[:pos+2] + replacement + result[pos+3:]
    
    # Ensure first digit is not 0
    if result[0] == '0':
        result = random.choice('123') + result[1:]
    
    return result

def generate_task2():
    """Генерация задачи на формальные языки"""
    # Определяем возможные элементы языка
    symbols = ['0', '1', '2', '3', 'a', 'b', 'c', 'є']
    
    # Генерация L1
    l1_size = random.randint(2, 4)
    l1 = [random.choice(symbols[:6]) for _ in range(l1_size-1)]
    
    # Добавляем один составной элемент
    if random.random() > 0.5:
        l1.append(random.choice(symbols[:6]) + random.choice(symbols[:6]))
    else:
        l1.append(random.choice(symbols[:6]))
    
    # Генерация L2
    l2_size = random.randint(2, 4)
    l2 = ['є']  # Пустая строка часто встречается в примерах
    l2.extend([random.choice(symbols[:6]) for _ in range(l2_size-1)])
    
    # Определяем возможные операции
    operations = [
        (f"L2UL1", "объединение L2 и L1"),
        (f"L1^2", "L1 в квадрате"),
        (f"L2^2\\L1^2", "L2 в квадрате минус L1 в квадрате"),
        (f"L2L1", "конкатенация L2 и L1"),
        (f"L1L2", "конкатенация L1 и L2"),
        (f"L1\\L2", "L1 минус L2"),
        (f"L2^2UL1^2", "объединение L2 в квадрате и L1 в квадрате"),
        (f"L1^2\\L2^2", "L1 в квадрате минус L2 в квадрате")
    ]
    
    # Выбираем 3 операции
    chosen_ops = random.sample(operations, 3)
    
    return {
        "L1": set(l1),
        "L2": set(l2),
        "operations": chosen_ops
    }

def generate_task3():
    """Генерация задачи на вывод в контекстно-свободной грамматике"""
    # Выбираем одну из грамматик из примеров
    grammars = [
        {
            "rules": "S-> bA|aB, A-> a|aS|bAA, B-> b|bS|aBB",
            "samples": ["aabbab", "baaabbab"]
        },
        {
            "rules": "S-> bA|aB, A-> a|aS|bAa, B-> b|bS|aBb",
            "samples": ["bbaaba"]
        },
        {
            "rules": "S-> bA|aBC, A-> a|aS|bAC, B-> b|bS|aCB, C-> a|Bb",
            "samples": ["aaabbb"]
        }
    ]
    
    chosen_grammar = random.choice(grammars)
    
    # Выбираем из существующих примеров или генерируем новый (упрощенно)
    if random.random() > 0.7 and chosen_grammar["samples"]:
        sentence = random.choice(chosen_grammar["samples"])
    else:
        length = random.randint(5, 8)
        sentence = ''.join(random.choice('ab') for _ in range(length))
    
    return {
        "grammar": chosen_grammar["rules"],
        "sentence": sentence
    }

def generate_task4():
    """Генерация задачи на создание контекстно-свободной грамматики для языка"""
    # Определяем возможные шаблоны языков
    language_patterns = [
        "{a^k b^m c^m|m,k,>=0}",
        "{a^m b^m c^k|m>=0, k>=1}",
        "{a b^k c^m|m,k>=1}",
        "{a^k b c^k|k>=1}U{a b^k c|k>=1}"
    ]
    
    # Выбираем один или создаем вариацию
    if random.random() > 0.3:
        chosen_pattern = random.choice(language_patterns)
    else:
        # Создаем вариации
        symbols = ['a', 'b', 'c']
        random.shuffle(symbols)
        x, y, z = symbols
        
        k_condition = random.choice([">=0", ">=1"])
        m_condition = random.choice([">=0", ">=1"])
        
        pattern = f"{{{x}^k {y}^m {z}^m|m{m_condition}, k{k_condition}}}"
        chosen_pattern = pattern
    
    return chosen_pattern

def generate_task5():
    """Генерация задачи на построение є-свободной грамматики"""
    # Определяем возможные грамматики с є-продукциями
    grammars = [
        "S-> AC|BA, A-> a|BAB|bCb, B-> bC|aAc|є, C-> a|ACb|c",
        "S-> AAb|BA, A-> a|BAB|baC, B-> bC|aAc, C-> a|c|є",
        "S-> AB|BA, A-> SA|BB|bB, B-> b|aA|є",
        "S-> bA|aBb, A-> a|aCC|bAa|є, B-> b|bC|aAc, C-> a|b|c"
    ]
    
    # Выбираем одну или создаем вариацию
    if random.random() > 0.3:
        chosen_grammar = random.choice(grammars)
    else:
        # Создаем вариацию, заменяя некоторые нетерминалы или терминалы
        base_grammar = random.choice(grammars)
        
        # Случайно решаем заменить некоторые нетерминалы
        if random.random() > 0.5:
            nt_swap = {'A': 'B', 'B': 'A'} if random.random() > 0.5 else {'B': 'C', 'C': 'B'}
            
            # Используем временные маркеры, которые точно не будут встречаться в грамматике
            temp_markers = {'A': '!A!', 'B': '!B!', 'C': '!C!'}
            
            # Сначала заменяем на временные маркеры
            for old, temp in temp_markers.items():
                if old in nt_swap:
                    base_grammar = base_grammar.replace(old, temp)
            
            # Затем заменяем временные маркеры на целевые нетерминалы
            for old, new in nt_swap.items():
                base_grammar = base_grammar.replace(temp_markers[old], new)
        
        chosen_grammar = base_grammar
    
    return chosen_grammar

def generate_variant():
    """Генерация полного варианта со всеми 5 задачами"""
    return {
        "task1": generate_task1(),
        "task2": generate_task2(),
        "task3": generate_task3(),
        "task4": generate_task4(),
        "task5": generate_task5()
    }

def format_variant(variant, variant_num):
    """Форматирование варианта в текстовом виде"""
    result = f"Вариант {variant_num}\n\n"
    
    # Задача 1
    result += "1. Найдите все суффиксы, префиксы и подстроки строки: " + variant["task1"] + "\n\n"
    
    # Задача 2
    task2 = variant["task2"]
    l1_str = "{" + ", ".join(sorted(task2["L1"])) + "}"
    l2_str = "{" + ", ".join(sorted(task2["L2"])) + "}"
    result += f"2. Пусть L1 и L2 два формальных языка. L1={l1_str}, L2={l2_str}. Вычислить:\n"
    result += ", ".join([op[0] for op in task2["operations"]]) + ".\n\n"
    
    # Задача 3
    task3 = variant["task3"]
    result += "3. Задана контекстно свободная грамматика G = (N, T, P, S), N = {S, A, B}, T= {a, b},\n"
    result += f"P: {task3['grammar']}.\n"
    result += f"Построить схему вывода сентенции: {task3['sentence']}, дерево разбора и все сечения дерева.\n\n"
    
    # Задача 4
    result += "4. Постройте контекстно свободную грамматику, которая порождает следующий язык:\n"
    result += f"L={variant['task4']}.\n\n"
    
    # Задача 5
    result += "5. Задана грамматика G=(N, T, P, S), построить є - свободную грамматику.\n"
    result += f"{variant['task5']}.\n"
    
    return result

def generate_variants(num_variants=10):
    """Генерация нескольких вариантов"""
    variants = []
    for i in range(1, num_variants+1):
        variants.append(format_variant(generate_variant(), i))
    return variants

if __name__ == "__main__":
    try:
        # Пытаемся импортировать модуль утилит для лучшей работы с файлами
        from utils import write_utf8_file_with_bom
        
        num_variants = 10  # Измените это значение, чтобы сгенерировать больше или меньше вариантов
        variants = generate_variants(num_variants)
        
        # Записываем в файл с кодировкой UTF-8 BOM для лучшей совместимости с Windows
        content = "\n\n" + "="*50 + "\n\n".join(variants)
        write_utf8_file_with_bom("task_variants.txt", content)
        
    except ImportError:
        # Запасной вариант, если модуль utils недоступен
        num_variants = 10
        variants = generate_variants(num_variants)
        
        # Записываем в файл с кодировкой UTF-8
        with open("task_variants.txt", "w", encoding="utf-8") as f:
            f.write("\n\n" + "="*50 + "\n\n".join(variants))
        
    print(f"Generated {num_variants} variants and saved to task_variants.txt") 