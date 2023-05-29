def read_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        return file.read()



def show_data() -> None:
    """Выводит информацию из справочника"""
    #contacts = read_data()
    print(read_data())



def edit_file():
    return read_data().split('\n')



def add_data() -> None:
    """Добавляет информацию в справочник."""
    name = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n {name} | {phone}')
        print('Контакт записан')



def find_data():
    """Печатает результат поиска по справочнику."""
    phonebook = edit_file()
    data_to_find = input('Введите данные для поиска: ')
    result = search_data(phonebook, data_to_find)
    print(result)



def search_data(phonebook: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = []
    for entry in phonebook:
        if info in entry:
            result.append(entry)
    if len(result) == 0:
        print('Совпадений не найдено')
    else:
        if len(result) == 1:
            print('\n'.join(result))
        elif len(result) > 1:
            print('\n'.join(result))
            print('Уточните данные')
    return result


def edit_data() -> None:
    """Редактирует найденные записи в списке по запросу"""
    phonebook = edit_file()
    old_entry = input('Данные для редактирования: ')
    old_entry = search_data(phonebook, old_entry)
    phonebook = str('\n'.join(phonebook))
    if old_entry:
        name = input('Введите ФИО: ')
        phone = input('Введите номер телефона: ')
        new_entry = name +' ' + '|'+' ' + phone
        phonebook = phonebook.replace(str('\n'.join(old_entry)), new_entry)
    else:
            print('Совпадений не найдено')
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(phonebook)


def delete_data() -> None:
    """Удаляет найденные по запросу записи из списка"""
    phonebook = edit_file()
    remove_entry = input('Введите данные для удаления: ')
    remove_entry = search_data(phonebook, remove_entry)
    phonebook.remove(remove_entry)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(phonebook))
        print('Запись удалена')


