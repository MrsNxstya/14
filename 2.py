import matplotlib.pyplot as plt

years = list(range(2005, 2025))
ukraine_data = [15000, 14000, 12000, 11000, 10000, 9500, 9000, 8500, 8000, 7500,
                7000, 6800, 6500, 6200, 6000, 5800, 5600, 5400, 5200, 5000]
usa_data = [350000, 340000, 330000, 320000, 310000, 300000, 290000, 280000, 270000, 260000,
            250000, 240000, 230000, 220000, 210000, 200000, 195000, 190000, 185000, 180000]

plt.figure(figsize=(10, 6))
plt.plot(years, ukraine_data, label='Ukraine', marker='o', color='blue')
plt.plot(years, usa_data, label='USA', marker='s', color='green')

plt.xlabel('Year')
plt.ylabel('Children out of school (primary)')
plt.title('Children out of school, primary (2005–2024)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

country = input("Введіть назву країни (Ukraine або USA): ").strip().lower()

plt.figure(figsize=(10, 6))

if country == "ukraine":
    plt.bar(years, ukraine_data, color='skyblue')
    plt.title("Діти поза школою (початкова освіта) – Україна")
elif country == "usa":
    plt.bar(years, usa_data, color='orange')
    plt.title("Діти поза школою (початкова освіта) – США")
else:
    print("Вибрано невірну назву країни. Спробуйте ще раз.")
    exit()

plt.xlabel("Рік")
plt.ylabel("Кількість дітей, які не відвідують початкову школу")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, axis='y')
plt.show()
