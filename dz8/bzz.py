def main():
    while True:
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "6":
            break
        elif choice == "2":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_entry(surname, name, phone)
        elif choice == "4":
            surname = input("Введите фамилию: ")
            name = input("Введите новое имя (оставьте пустым, чтобы не менять): ")
            phone = input("Введите новый номер телефона (оставьте пустым, чтобы не менять): ")
            update_entry(surname, name, phone)
        elif choice == "5":
            surname = input("Введите фамилию для удаления: ")
            delete_entry(surname)
        elif choice == "3":
            surname = input("Введите фамилию для поиска: ")
            entry = find_entry(surname)
            if entry:
                print(f"Имя: {entry[0]}, Номер телефона: {entry[1]}")
            else:
                print("Запись не найдена.")
        else:
            print("Неизвестное действие.")


if __name__ == "__main__":
    main()
    
    
 