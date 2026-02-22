def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()  # прибираємо перенос рядка

                if line:  # перевіряємо, що рядок не пустий
                    cat_id, name, age = line.split(",")

                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }

                    cats.append(cat_dict)

        return cats

    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    except Exception as e:
        print("Сталася помилка:", e)
        return []
    

cats_info = get_cats_info("cats.txt")
print(cats_info)
