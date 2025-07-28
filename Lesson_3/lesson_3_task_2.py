from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13 Pro", "+79995556741"),
    Smartphone("Samsung", "Galaxy S25", "+79995556123"),
    Smartphone("Xiaomi", "Redmi 12", "+79995551123"),
    Smartphone("HUAWEI", "Nova 12", "+79995551423"),
    Smartphone("Infinix", "XX", "+79995551893")
]

# Печатаем библиотеку
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}, {smartphone.number}")
