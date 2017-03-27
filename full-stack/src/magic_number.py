def magic_number():
    user_num = input("pick a number between 1-10 ")
    user_num = int(user_num)
    return user_num


def magic(user_num):
    m_num = int(7)
    if user_num == m_num:
        print("you win!")
    else:
        print("you lose!")
        run()


def run():
    magic(magic_number())

run()
