def get_user_age():
    user_age_string = input("Enter your age: ")
    user_age_int = int(user_age_string)
    return user_age_int


def calculate_age_in_seconds(age_years):
    return age_years * 365 * 24 * 60 * 60


def run():
    print("Your age in seconds is {}.".format(calculate_age_in_seconds(get_user_age())))

run()


