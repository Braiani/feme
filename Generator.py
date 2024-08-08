from FuncGenerator import Generator

try:
  width = int(input("- Insert the width the password needs to have: "))
except ValueError:
  print("- Invalid value")

choice_special = input("- Does the password needs special characters? (Y/N) ").capitalize()

if choice_special not in ['Y', 'N']:
  print("\n- Invalid choice")

choice_num = input("- Does the password needs numbers? (Y/N) ").capitalize()

if choice_num not in ['Y', 'N']:
  print("\n- Invalid choice")

choice_letters = input("- Does the password needs letters? (Y/N) ").capitalize()

if choice_letters not in ['Y', 'N']:
  print("\n- Invalid choice")

Generator.generatePass(width, choice_num, choice_letters, choice_special)