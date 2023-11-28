def tri(b, h):
    return 0.5 * b * h

def circle(r):
    return 3.14 * r ** 2

def rect(b, a):
    return b * a

# def main():
#     print('Начало модуля1')
#     print('Начинаем считать сложную фигуру')
#     area = rect(20, 30) - circle(5) + tri(20, 15)
#     print(f'{area=}')
#     print('Конец модуля1')
   
# if __name__ == '__main__':
#     main()
    var2
if __name__ == '__main__':
    print('Начало модуля1')
    print('Начинаем считать сложную фигуру')
    area = rect(20, 30) - circle(5) + tri(20, 15)
    print(f'{area=}')
    print('Конец модуля1')