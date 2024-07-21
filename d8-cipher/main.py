
from pic import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def process(cipher_txt, shifter, direction):
  shifter %= 26
  res = []
  cipher_idx = [alphabet.index(letter) for letter in cipher_txt]
  
  for ele in cipher_idx:
    if direction == "encode":
      ele = (ele + shifter)%26
    else:
      ele = (ele - shifter)%26
      if ele < 0:
        ele += 26
    res.append(ele)

  return res

# read both encrypt and decrypt code
def code_reader(idx_list):
  res = [alphabet[idx] for idx in idx_list]
  res = "".join(res)
  print(f"Here's the encoded result: {res}")

while True:
  direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = str(input("Type your message:\n")).lower()
  shift = int(input("Type the shift number:\n"))
  
  newId = process(text, shift, direction)
  code_reader(newId)


  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    break
    
