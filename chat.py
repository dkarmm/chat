import os


def create_profiles():
    data = dict()
    users = registration(data)
    return users


def main(users_data):
    user = authentication(users_data)
    print(f"\nДобро пожаловать в чат {user.title()}!")
    while True:
        try:
            with open("chat.txt", "a", encoding='utf-8') as chat_file:
                activ = input(f"\nТекущие команды чата: "
                              f"\n1. Посмотреть текущую историю чата."
                              f"\n2. Отправить сообщение"
                              f"\n3. Выйти из профиля."
                              f"\n4. Закрыть программу."
                              f"\n5. Стереть переписку. "
                              f"\nВвод: ")
            if activ == "1":
                if os.stat("chat.txt").st_size == 0:
                    print("\nНа данный момент история сообщений отсутствует.")
                else:
                    with open("chat.txt", "r", encoding='utf-8') as chat_file:
                        for i_line in chat_file:
                            print(i_line, "\n")
            elif activ == "2":
                with open("chat.txt", "a", encoding='utf-8') as chat_file:
                    message = input("Введите сообщение: \n")
                    chat_file.write(f"\n{user}: {message}\n__________________________")
            elif activ == "3":
                main(users_data)
                break
            elif activ == "4":
                break
            elif activ == "5":
                os.remove('chat.txt')
            else:
                raise SyntaxError
        except SyntaxError:
            print("Ошибка ввода.")


def get_name():
    return input("Введите логин пользователя: ")


def get_pass():
    return input("Введите пароль: ")


def new_registration_check():
    while True:
        try:
            question_reg = input("\nХотите зарегистрировать ещё одного пользователя? Y/N: ").lower().strip()
            if question_reg == "y":
                return True
            elif question_reg == "n":
                return False
            else:
                raise SyntaxError
        except SyntaxError:
            print("\nОшибка ввода.")


def registration(users_dict):
    while True:
        print("\nПроизводится регистрация.")
        first_user_name = get_name()
        users_dict[first_user_name] = get_pass()
        flag = new_registration_check()
        if not flag:
            return users_dict


def authentication(users_dict):
    if len(users_dict) == 1:
        print("\nВы единственный зарегистрировавшийся пользователь!")
        for name in users_dict.keys():
            return name
    while True:
        print("\nАутентификация пользователя.")
        try:
            user_name = get_name()
            if user_name not in users_dict:
                raise NameError
            else:
                password = get_pass()
                if users_dict[user_name] != password:
                    raise ValueError
                else:
                    return user_name
        except NameError:
            print("\nОшибка ввода. Пользователь отсутствует.")
        except ValueError:
            print("\nНеверно введен пароль.")


data = create_profiles()
main(data)
