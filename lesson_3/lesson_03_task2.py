from smartphone import Smartphone
catalog = [
Smartphone("Huawei", "P20 Lite", "+79121212121"),
Smartphone("Samsung", "Galaxy A17", "+79232323232"),
Smartphone("Apple", "Iphone17", "+79123123123"),
Smartphone("Xiaomi", "Redmi Note 15 pro", "+79435678912"),
Smartphone("Honor", "Honor 600", "+79677689123")
]

for phone in catalog:

    print(f"{phone.brand} - {phone.model}. {phone.number}")