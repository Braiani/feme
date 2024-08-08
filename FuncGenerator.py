import string
import random as r

class Generator():
  def generatePass(width, choice_num, choice_letters, choice_special):
    random = []
    password = []
    passwordstr = ''

    if choice_letters == 'Y':
      random += string.ascii_lowercase + string.ascii_uppercase

    if choice_num == 'Y':
      random += string.digits

    if choice_special == 'Y':
      random += string.punctuation

    for i in range(width):
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