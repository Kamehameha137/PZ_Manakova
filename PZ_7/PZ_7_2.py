#вариант 31 
#Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими). 
# Найти длину самого короткого слова

stroka = input("Введите строку: ")
words = stroka.split()
min_len = min(len(word) for word in words)

print()  # 1