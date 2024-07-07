"""Homework:
Tub sonlarni , Ham iterator ham generator orqali yozib kelinglar
"""
# from colorama import Fore
# from math import sqrt
#
#
# # =======================================================> Check one number to prime with iterator
# class CheckPrimeNumbers:
#     def __init__(self, number: int):
#         self.number = number
#         self.count = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count > self.number:
#             raise StopIteration
#         else:
#             sqrt_number: int = int(sqrt(number))
#             count = 0
#             for i in range(1, sqrt_number + 1, 1):
#                 if number % i == 0:
#                     count += 1
#
#             if number == 1:
#                 return Fore.GREEN + f'{sqrt_number} soni tub ham murakkab ham emas' + Fore.RESET
#             elif count > 1:
#                 return Fore.GREEN + f'{number} is`t prime number.' + Fore.RESET
#             else:
#                 return Fore.GREEN + f'{number} is a prime number' + Fore.RESET
#
#         self.count += 1
#
#
# try:
#     number: int = int(input(Fore.MAGENTA + 'Enter a number: ' + Fore.RESET))
#     result = CheckPrimeNumbers(number)
#     print(result)
#     # for i in result:
#     #     print(i)
# except ValueError as err:
#     print(Fore.RED + 'Error: ' + Fore.RESET + str(err))

# =========================================================> Check number to prime with generation

# def prime_check_with_gen(num: int):
#     k = 1
#     while k <= num:
#         def check_prime_one_numbers(number: int) -> str:
#             sqrt_number: int = int(sqrt(number))
#             count = 0
#             for i in range(1, sqrt_number + 1, 1):
#                 if number % i == 0:
#                     count += 1
#
#             if number == 1:
#                 return Fore.GREEN + f'{sqrt_number} soni tub ham murakkab ham emas' + Fore.RESET
#             elif count > 1:
#                 return Fore.GREEN + f'{number} is`t prime number.' + Fore.RESET
#             else:
#                 return Fore.GREEN + f'{number} is a prime number' + Fore.RESET
#
#         yield check_prime_one_numbers(k)
#         k += 1
#
#
# try:
#     number: int = int(input(Fore.MAGENTA + 'Enter a number: ' + Fore.RESET))
# except ValueError as err:
#     print(Fore.RED + 'Error: ' + Fore.RESET + str(err))
#
# prime_gen = prime_check_with_gen(number)
# for num in prime_gen:
#     print(num)
