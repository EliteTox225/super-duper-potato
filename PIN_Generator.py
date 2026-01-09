import random

wanted_pin_len = int(input("Enter your PIN's length: "))
pin_len = 0
pin = ""

while pin_len < wanted_pin_len:
	   pin_digit = random.randint(0,9)
	   pin += str(pin_digit)
	   pin_len += 1

print(f"Your generated PIN is {pin}")
