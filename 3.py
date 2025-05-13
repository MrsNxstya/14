import json
import os
import matplotlib.pyplot as plt

JSON_FILE = "detali.json"
RESULT_FILE = "result.json"
PRICES = {
    "тип1": 50,
    "тип2": 40,
    "тип3": 30,
    "тип4": 60,
    "тип5": 70
}

def load_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def show_data():
    data = load_data()
    if not data:
        print("Файл порожній.")
        return
    for entry in data:
        print(f"{entry['день']}: {entry['деталі']}")

def add_entry():
    day = input("Введіть день тижня: ")
    details = {}
    for i in range(1, 6):
        count = int(input(f"Введіть кількість для тип{i}: "))
        details[f"тип{i}"] = count
    data = load_data()
    data.append({"день": day, "деталі": details})
    save_data(data)
    print("Запис додано.")

def delete_entry():
    day = input("Введіть день, запис якого потрібно видалити: ")
    data = load_data()
    data = [entry for entry in data if entry['день'].lower() != day.lower()]
    save_data(data)
    print("Запис видалено (якщо існував).")

def search_by_field():
    field = input("Введіть тип деталі (тип1-тип5): ")
    data = load_data()
    found = False
    for entry in data:
        if field in entry["деталі"]:
            print(f"{entry['день']}: {field} = {entry['деталі'][field]}")
            found = True
    if not found:
        print("Нічого не знайдено.")

def calculate_week_cost():
    data = load_data()
    total = 0
    for entry in data:
        for detail_type, quantity in entry['деталі'].items():
            total += quantity * PRICES.get(detail_type, 0)
    result = {"Загальна вартість за тиждень": total}
    with open(RESULT_FILE, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)
    print(f"Загальна вартість за тиждень: {total} грн (збережено у {RESULT_FILE})")

def plot_pie_chart():
    data = load_data()
    if not data:
        print("Немає даних для побудови діаграми.")
        return

    totals = {"тип1": 0, "тип2": 0, "тип3": 0, "тип4": 0, "тип5": 0}

    for entry in data:
        for detail_type, count in entry["деталі"].items():
            totals[detail_type] += count

    labels = list(totals.keys())
    sizes = list(totals.values())
    colors = plt.get_cmap('Set3').colors[:5]

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140,
        colors=colors,
        shadow=True
    )
    plt.title("Співвідношення кількості деталей за типами (за тиждень)")
    plt.axis('equal')
    plt.tight_layout()

    plt.savefig("diagram.png")
    print("Діаграма збережена у файл diagram.png")

def menu():
    while True:
        print("\nМеню:")
        print("1. Вивести дані")
        print("2. Додати запис")
        print("3. Видалити запис")
        print("4. Пошук за полем")
        print("5. Обчислити вартість за тиждень")
        print("6. Вийти")
        print("7. Побудувати кругову діаграму")
        choice = input("Ваш вибір: ")

        if choice == '1':
            show_data()
        elif choice == '2':
            add_entry()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            search_by_field()
        elif choice == '5':
            calculate_week_cost()
        elif choice == '6':
            break
        elif choice == '7':
            plot_pie_chart()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    menu()
