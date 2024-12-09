# import random
# from decimal import Decimal
# from datetime import datetime, timedelta
# class Tekshiruvchi:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __set__(self, instance, value:str):
#         temp = Decimal(value)
#         if not (-50 <= temp <= 50):
#             raise ValueError("Xato!!!!")
#         instance.__dict__[self.name] = temp
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     day_offset = random.randint(-30, 30)
#     conversion_date = datetime.now() + timedelta(days=day_offset)
#     print("Vaqti", conversion_date.strftime("%Y-%m-%d"))
#
# class Harorat:
#     harorat = Tekshiruvchi()
#     def __init__(self , harorat):
#         self.harorat = harorat
#
#
#
#     def harorat_chiqarish(self):
#         return f"Bizda harorat {self.harorat}"
#
# harortda1 = Harorat('hh')
# print(harortda1.harorat_chiqarish())
#
#
# import random
# import decimal
# from datetime import datetime, timedelta
#
# class Tekshiruvchi:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name)
#
#     def __set__(self, instance, value):
#         value = decimal.Decimal(value).quantize(decimal.Decimal('0.00'))
#         if not (-50 <= value <= 50):
#             raise ValueError("Belgilanganida tashqarida -50°C  50°C")
#         instance.__dict__[self.name] = value
#
# class Harorat:
#     temperatura = Tekshiruvchi('temperatura')
#
#     def __init__(self):
#         self.temperatura = random.uniform(-10, 40)
#         self.mudat = datetime.now() - timedelta(days=random.randint(0, 30))
#
#     def __str__(self):
#         return f"{self.temperatura}C  {self.mudat:%Y-%m-%d}"
#
# temp1 = Harorat()
# print(temp1)

# #2 msiol
# import decimal
# import random
# from datetime import datetime, timedelta
#
# class InsufficientFundsError(Exception):
#     pass
#
# class BankAccount:
#     def __init__(self, initial_balance):
#         self.balance = decimal.Decimal(initial_balance)
#
#     def depozit(self, amount):
#         self.balance += decimal.Decimal(amount)
#         self.transaction_date = datetime.now() - timedelta(days=random.randint(0, 30))
#         print(f"{amount}  qo'shildi. Hisobingiz: {self.balance} ")
#
#     def olish (self, amount):
#         amount = decimal.Decimal(amount)
#         if self.balance - amount < 0:
#             raise InsufficientFundsError("Xatolik: Balans yetarli emas!")
#         self.balance -= amount
#         self.transaction_date = datetime.now() - timedelta(days=random.randint(0, 30))
#         print(f"{amount}  yechildi. Hisobingiz: {self.balance} ")
#
#     def __str__(self):
#         return f"Hisobingiz: {self.balance} "
#
# hisob = BankAccount('500000')
# print(hisob)
# hisob.depozit('200000')
#
# 3 misol
# import decimal
# import random
# from datetime import datetime, timedelta
#
# class Chipta:
#     def __init__(self, narx):
#         try:
#             self.narx = decimal.Decimal(narx)
#         except decimal.InvalidOperation:
#             raise ValueError("Narx Decimal formatda bo'lishi kerak")
#         self.data = datetime.now() - timedelta(days=random.randint(0, 30))
#
#     def __str__(self):
#         return f"chipta narxi: {self.narx} sanasi: {self.data:%Y-%m-%d}"
#
#
# chipta = Chipta('150000')
# print(chipta)
#

# 4 msiol
# import decimal
# import random
# from datetime import datetime, timedelta
#
# class Maosh:
#     def __init__(self, narx):
#         try:
#             self.narx = decimal.Decimal(narx)
#         except decimal.InvalidOperation:
#             raise ValueError(" notogiri kiritlgan!!!")
#         self.data = datetime.now() - timedelta(days=random.randint(0, 30))
#
#     def __str__(self):
#         return f"ishchi oyligi: {self.narx} tolov sanasi: {self.data:%Y-%m-%d}"
#
#
# maosh = Maosh('320000000')
# print(maosh)
#
#
