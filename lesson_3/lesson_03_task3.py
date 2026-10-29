from adress import Address
from Mailing import Mailing


from_address = Address("453445", "Тверь", "Ленина", "35", "124")
to_address = Address("747476", "Челябинск", "Ленинский проспект", "34", "54")


mail = Mailing(to_address=to_address, from_address=from_address, cost=1000, track="TR54365RU")

track_info = f"Отправить {mail.track} из адреса "
from_info = f"{from_address.formatted()}"
to_info = f" по адресу {mail.to_address.formatted()}"
cost_info=f". Стоимость {mail.cost} рублей."
print(track_info + from_info + to_info + cost_info)
