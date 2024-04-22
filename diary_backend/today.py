from colorama import just_fix_windows_console
from termcolor import colored


just_fix_windows_console()
print(colored(f"Tell me about your day", "dark_grey" ,attrs=["underline"]))
toWrite = input()
with open("today.txt", "a") as f:
    f.write(toWrite)
    f.close()
