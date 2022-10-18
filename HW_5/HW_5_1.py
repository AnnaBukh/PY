# replace - склеит все без фразы 
# будет функция, куда заходит количество и буквы "абв"
# sample 
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import choices
# from random import sample 

def create_line(kol: int, line: str):
  line_1 = []
  for i in range(kol):
    line_2 = choices(line, k=3)
    line_1.append("".join(line_2))
  line_1 = " ".join(line_1)
  return line_1

my_list = create_line(10, 'абв')
print(my_list)
    
def find_line(all_line: str, f_line: str):
  all_line = all_line.replace(f_line, "")
  return all_line

print(find_line(my_list, "абв"))