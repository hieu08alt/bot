import json

def config_bot():
  with open('config.json', 'r') as f:
    config = json.load(f)
    return config

def write_log(user):
  with open("log.csv", 'w') as f:
    f.write(user + '\n')

def ghi_hoa(list_bad_word):
    for i in range(len(list_bad_word)):
      list_bad_word[i] = list_bad_word[i].upper()
    return list_bad_word


def get_badword():
  with open("bad_word.txt", "r") as f:
    list_bad_word = f.read().splitlines()
    list_bad_word = ghi_hoa(list_bad_word)

  with open("bad_word1.txt", "r") as f:
    list_bad_word1 = f.read().splitlines()
    list_bad_word1 = ghi_hoa(list_bad_word1)
  for i in range(len(list_bad_word1)):
    list_bad_word1[i] = list_bad_word1[i] + " "
  
  return list_bad_word + list_bad_word1

#test
# print(get_badword())
# -> ham thanh cong