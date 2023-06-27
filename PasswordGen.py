import random
import string

def password (length=8):

  char = string.ascii_letters.lower() + string.digits + string.punctuation + string.ascii_letters.upper()

  return ''.join(random.choice(char) for i in range(length))

print("Generating a password with letters, digits and special characters!\n")

print ("First Random String ", password())
print ("Second Random String ", password())
print ("Third Random String ", password())
