import re
def get_d_sum(word):
  sum = 0
  word  = re.sub('[^A-Za-z0-9]+','',word)
  if word is not None:
    for char in word:
        sum  =  sum + ord(char.casefold())-ord('a')+1
  return sum
input = open('input.txt')
output = open('output.txt','w')
in_lines = input.readlines()
for line in in_lines:
  print(get_d_sum(line))
  output.write(str(get_d_sum(line)%9))
    

