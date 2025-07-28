from address import Address
from mailing import Mailing

from_address = Address(109109, "Moscow", "Pushkinskaya", 25, 12)
to_address = Address(109209, "Moscow", "Tverskaya", "15", "22")
track = 12909
cost = 1


mailing = Mailing(track, from_address, to_address, cost)

print(mailing)
