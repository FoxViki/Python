import os

def zag_data(file_path):
    contacts = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                contacts.append({'surname': data[0], 'name': data[1], 'phone_number': data[2], 'com': data[3]})
    return contacts

def write_data(file_path, contacts):
    with open(file_path, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(f"{contact['surname']},{contact['name']},{contact['phone_number']}, {contact['com']}\n")

def print_contacts(contacts):
    if len(contacts) > 0:
        for contact in contacts:
            print(f"{contact['surname']}, {contact['name']}, {contact['phone_number']}, {contact['com']}")
    else: print(f"Файл не существует.")

def add_contact(contacts, surname, name, phone_number, com):
    contacts.append({'surname': surname, 'name': name, 'phone_number': phone_number, 'com': com})

def find_contact(contacts, key, value):
    results = [contact for contact in contacts if contact[key].lower() == value.lower()]
    return results

def update_contact(contacts, surname, name, phone_number, com):
    for contact in contacts:
        if contact['surname'].lower() == surname.lower() and contact['name'].lower() == name.lower():
            contact['phone_number'] = phone_number
            contact['com'] = com
            

def delete_contact(contacts, surname, name):
    contacts[:] = [contact for contact in contacts if contact['surname'].lower() != surname.lower() or contact['name'].lower() != name.lower()]

def main():
    file_tel = "phonebook_tel.txt"
    contacty = zag_data(file_tel)

    while True:
        print("1. Посмотреть все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("Контакты:")
            print_contacts(contacty)

        elif choice == '2':
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            com = input("Введите комментарий: ")
            add_contact(contacty, surname, name, phone_number, com)
            write_data(file_tel, contacty)
            
        elif choice == '3':
            find_key = input("Выберите характеристику для поиска: фамилия - surname/имя - name: ")
            find_value = input("Введите значение для поиска: ")
            results = find_contact(contacty, find_key, find_value)
            if results:
                print("Контакт:")
                print_contacts(results)
            else:
                print("Ничего нет.")
                
        elif choice == '4':
            surname = input("Введите фамилию для изменения: ")
            name = input("Введите имя для изменения: ")
            phone_number = input("Введите новый номер телефона: ")
            com = input("Введите комментарий: ")
            update_contact(contacty, surname, name, phone_number, com)
            write_data(file_tel, contacty)
            
        elif choice == '5':
            surname = input("Введите фамилию для удаления: ")
            name = input("Введите имя для удаления: ")
            delete_contact(contacty, surname, name)
            write_data(file_tel, contacty)

        elif choice == '6':
            print("До свидания.")
            break
        else:
            print("Ошибка. Выберите действие: ")

main()