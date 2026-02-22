def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()  # прибираємо перенос рядка
                if line:  # перевірка, що рядок не пустий
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено")
        return (0, 0)

    except Exception as e:
        print("Сталася помилка:", e)
        return (0, 0)
    

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

