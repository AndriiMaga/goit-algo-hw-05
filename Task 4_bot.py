def input_error(func): # декоратор для обробки помилок введення
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please, write a valid name"
        except ValueError:
            return "Write name and phone"
        except IndexError:
            return "Enter a user name"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split() # Розбиваємо введений рядок на команду та аргументи
    cmd = cmd.strip().lower() #видаляємо пробіли та робимо нижній регістр
    return cmd, *args

@input_error
def add_contact(args, contacts): # Додаємо новий контакт у словник

    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):  # Змінюємо номер телефону для наявного контакту

    name, new_phone = args
    if name in contacts:
        old_phone = contacts[name] # Зберігаємо старий номер
        contacts[name] = new_phone # Оновлюємо старий номер на новий
        return f"Updated: {old_phone} was changed to {new_phone} for {name}."
    else:
        return f"Contact {name} not found."

@input_error
def show_phone(args, contacts):

    name, = args
    return f"{name}: {contacts[name]}"


def show_all(contacts): #виводимо всі збережені контакти
    if contacts:
        result = []  # створюємо список для імен та номерів
        for name, phone in contacts.items():
            line = f"{name}: {phone}"
            result.append(line)
        return "\n".join(result) # об'єднуємо рядки
    else:
        return "No contacts found."

def main():
    contacts = {} # Створюємо порожній словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!") # Вихід з програми при відповідній команді
            break
        elif command == "hello":
            print("How can I help you?") # вітання
        elif command == "add":
            print(add_contact(args, contacts)) # додавання контакту
        elif command == "change":
            print(change_contact(args, contacts)) # зміна номера
        elif command == "phone":
            print(show_phone(args, contacts)) # пошук номера
        elif command == "all":
            print(show_all(contacts)) # виведення всіх номерів
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()