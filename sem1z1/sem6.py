#1. определить с помощью рекурсии, число Х
# является простым
























#2. определить с помощью рекурсии , является ли
# слово полиндромом

def is_palindrom(word):
    if len[word]==word[-(k+1)]:
        print(word)
        return True
    if word[0]==word[-1]:
        print(word)
        return is_palindrom(word[1:-1])
    else:
        return False
word = input()
result= is_palindrom(word.lower())

if result:
    print(f"{word} - палиндром")
else: print(f"{word} - не палиндром")



# def is_palindrome(word):
# if len(word) == 0:
# print(word)
# return True
# if word[0] == word[-1]:
# print(word)
# return is_palindrome(word[1:-1])
# else:
# return False
# word = input("Введите слово: ")
# result = is_palindrome(word.lower())

# if result:
# print(f"{word} - палиндром.")
# else:
# print(f"{word} - не палиндром.")
