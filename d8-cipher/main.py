
from pic import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# encrypt code
def encode(plain_txt, shifter):
  shifter %= 26
  en_idx = []
  plain_idx = [alphabet.index(letter) for letter in plain_txt]
  for ele in plain_idx:
      ele += shifter
      en_idx.append(ele)
  return en_idx

# decrypt code
def decode(cipher_txt, shifter):
  shifter %= 26
  de_idx = []
  cipher_idx = [alphabet.index(letter) for letter in cipher_txt]
  for ele in cipher_idx:
    ele -= shifter
    de_idx.append(ele)
  return de_idx

# read both encrypt and decrypt code
def code_reader(idx_list):
  res = [alphabet[idx] for idx in idx_list]
  res = "".join(res)
  print(f"Here's the encoded result: {res}")


end = False

while end == False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = str(input("Type your message:\n")).lower()
  shift = int(input("Type the shift number:\n"))
  
  if direction == "encode":
    en_id = encode(text, shift)
    code_reader(en_id)
  else:
    de_id = decode(text, shift)
    code_reader(de_id)


  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    print("Bye Bye.")
    end = True
