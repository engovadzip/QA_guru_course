from datetime import datetime, time


def test_dark_theme_by_time():
    night_beginning = time(hour=22)
    night_end = time(hour=6)
    current_time = datetime.now().time()
    is_dark_theme = None

    if current_time < night_end or night_beginning <= current_time:
        is_dark_theme = True
    else:
        is_dark_theme = False

    current_time_string = current_time.strftime("%H:%M")
    assert is_dark_theme, f'Dark theme turns on at 22:00 and turns off at 6:00. Current time is {current_time_string}.'


def test_dark_theme_by_time_and_user_choice():
    night_beginning = time(hour=22)
    night_end = time(hour=6)
    current_time = datetime.now().time()
    dark_theme_enabled_by_user = False

    is_dark_theme = None

    if dark_theme_enabled_by_user == True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user == False:
        is_dark_theme = False
    else:
        test_dark_theme_by_time()

    assert is_dark_theme, 'User turns off the dark theme.'


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_user = None

    for user in users:
        if user['name'] == 'Olga':
            suitable_user = user
            break

    assert suitable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []

    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def print_function_name(func, *args):
    function_name = func.__name__.replace('_', ' ').title()
    result = f"{function_name} [{', '.join(args)}]"
    return result

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_function_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
