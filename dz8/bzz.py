import os

def load_data(file_path):
    contacts = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                contacts.append({'surname': data[0], 'first_name': data[1], 'middle_name': data[2], 'phone_number': data[3]})
    return contacts

def save_data(file_path, contacts):
    with open(file_path, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['surname']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']}\n")

def display_contacts(contacts):
    if len(contacts) > 0:
        for contact in contacts:
            print(f"{contact['surname']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}")
    else: print(f"Файл не существует.")

def add_contact(contacts, surname, name, phone, com):
    contacts.append({'surname': surname, 'name': name, 'phone': phone, 'com': com})

def find_contact(contacts, key, value):
    results = [contact for contact in contacts if contact[key].lower() == value.lower()]
    return results

def update_data(contacts, last_name, first_name, middle_name, phone_number):
    for contact in contacts:
        if contact['surname'].lower() == last_name.lower() and contact['first_name'].lower() == first_name.lower():
            contact['middle_name'] = middle_name
            contact['phone_number'] = phone_number

def delete_data(contacts, last_name, first_name):
    contacts[:] = [contact for contact in contacts if contact['surname'].lower() != last_name.lower() or contact['first_name'].lower() != first_name.lower()]

def copy_data(source_contacts, destination_contacts, line_number):
    if 0 < line_number <= len(source_contacts):
        contact_to_copy = source_contacts[line_number - 1]
        destination_contacts.append(contact_to_copy)
        print("Контакт успешно скопирован.")
    else:
        print("Некорректный номер строки для копирования.")





def main():
    
    filename = "phonebook.txt"
    contacts = load_data(filename)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    while True:
        file = "phonebook_source.txt"
        contacts = load_data(file)
        
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта по фамилии")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "6":
            break
        elif choice == "1":
            display_data(contacts)
        elif choice == "2":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            comment = input("Введите коментарий: ")
            add_data(surname, name, phone, comment)
        elif choice == "4":
            surname = input("Введите фамилию: ")
            name = input("Введите новое имя: ")
            phone = input("Введите новый номер телефона: ")
            comment = input("Введите коментарий: ")
            update_data(surname, name, phone, comment)
        elif choice == "5":
            surname = input("Введите фамилию для удаления: ")
            delete_data(surname)
        elif choice == "3":
            surname = input("Введите фамилию для поиска: ")
            entry = find_contact(surname)
            if entry:
                print(f"Имя: {entry[0]}, Номер телефона: {entry[1]}, Комментарий: {entry[2]}")
            else:
                print("Запись не найдена.")
        else:
            print("Неизвестное действие.")


if __name__ == "__main__":
    main()
    
    
 