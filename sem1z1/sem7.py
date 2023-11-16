 Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных
Created 3 months ago
Урок 8. Работа с файлами

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PhoneBook {
    private final Map<String, List<String>> phoneBook;

    public PhoneBook() {
        this.phoneBook = new HashMap<>();
    }

    // Добавление номера телефона
    public void add(String name, String phoneNumber) {
        phoneBook.computeIfAbsent(name, k -> new ArrayList<>()).add(phoneNumber);
    }

    // Получение списка телефонов по имени
    public List<String> get(String name) {
        return phoneBook.getOrDefault(name, new ArrayList<>());
    }

    public static void main(String[] args) {
        PhoneBook phoneBook = new PhoneBook();

        phoneBook.add("Иванов", "+1234567890");
        phoneBook.add("Иванов", "+0987654321");
        phoneBook.add("Петров", "+1111222233");

        System.out.println("Телефоны Иванова: " + phoneBook.get("Иванов"));
        System.out.println("Телефоны Петрова: " + phoneBook.get("Петров"));
    }
}




https://gist.github.com/Oscardkyou/e57efab61c1de6749700ba91d81dc78b