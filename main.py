# Задача №55.  Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import functions


while True:
    print('1. вывод, 2. добавление, 3. поиск, 4. редактирование, 5. удаление')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.edit_data()
    elif mode == 5:
        functions.delete_data()
    else:
        print('Выход из меню')
        break


# Leelo Ilves | 123654789
# Paul MesiMumm | 654123987
# Triinu Tamm | 852364127
# Vaino Saar | 785412369
# Monica Klemet | 369852147
# Ott Lepp | 987456321
# Kaia Kallas | 951267843
# Margus Mustikas | 321569874
# Hipp Rebane | 145263987
# Harvy Milk|52146321456