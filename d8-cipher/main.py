
from pic import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ENCODE FUNC

# encrypt code
def encode(plain_text, shifter):
  plain_index = []
  x = int()
  global en_index
  en_index = []
  for letter in plain_text:
    try:
      plain_index.append(alphabet.index(letter))
    except:
      plain_index.append(letter)

  for i in range(len(plain_text)):
    try:
      x = plain_index[i] + shifter
      if x > 25:
        x = 25-(plain_index[i]+shifter)
      else:
        pass
      en_index.append(x)
    except:
      en_index.append(plain_index[i])

# read encrypted code
def read_en(num_list):
  y = int()
  new_en = ""
  for i in range(len(num_list)):
    try:
      if num_list[i] > 0:
        new_en += alphabet[num_list[i]]
      else:
        y = (-num_list[i])-1
        new_en += alphabet[y]
    except:
      new_en += num_list[i]
  print(f"Here's the encoded result: {new_en}")


# DECODE FUNC

# decrypt code
def decode(cipher_text, shifter):
  cipher_index = []
  z = int()
  global de_index
  de_index = []
  for letter in cipher_text:
    try:
      cipher_index.append(alphabet.index(letter))
    except:
      cipher_index.append(letter)

  for i in range(len(cipher_index)):
    try:
        z = cipher_index[i] - shifter
        de_index.append(z)
    except:
      de_index.append(cipher_index[i])

# read decrypted code
def read_de(num_list):
  x = int()
  new_de = ""
  for i in range(len(num_list)):
    try:
      new_de += alphabet[num_list[i]]
    except:
      new_de += num_list[i]
  print(f"Here's the decoded result: {new_de}")

# LOOP
should_end = False

while should_end == False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  
  if direction == "encode":
    encode(text, shift)
    read_en(en_index)
  elif direction == "decode":
    decode(text, shift)
    read_de(de_index)
  else:
    break

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    print("Goodbye")
    should_end = True

