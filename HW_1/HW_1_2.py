# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# вывела на экран все значения x,y,z истинности утверждения 
print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
         if not (x or y or z) == (not x and not y and not z): 
            print(x, y, z) 