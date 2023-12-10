import os
import sys

while True:

    command = input("$ ")

    if command.lower() == "exit":
        break

    try:

        result = os.system(command)

        if result != 0:
            print(f"Xatolik: Buyruqni bajarishda xatolik ro'y berdi. Xatolik kodi: {result}")
    except Exception as e:
        print(f"Xatolik: {e}")
