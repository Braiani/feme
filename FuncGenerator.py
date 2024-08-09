import string
import random as r

class FuncGenerator():
  def __init__(self, width, choice_num, choice_letters, choice_special) -> None:
    self.width = width
    self.choice_num = choice_num
    self.choice_letters = choice_letters
    self.choice_special = choice_special

  def generatePass(self):
    random = []
    password = []
    passwordstr = ''

    if self.choice_letters == 'Y':
      random += string.ascii_lowercase + string.ascii_uppercase

    if self.choice_num == 'Y':
      random += string.digits

    if self.choice_special == 'Y':
      random += string.punctuation

    randomcharacter = ''
    for i in range(self.width):
      r.shuffle(randomcharacter)
      randomcharacter = r.choice(random)

      if randomcharacter in password:
        randomcharacter = r.choice(random)
        password.append(randomcharacter)
      else:
        password.append(randomcharacter)

    for i in password:
      passwordstr += i

    print(f"- Your password: {passwordstr}")