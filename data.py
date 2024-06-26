import allure
import requests
import random
import string

from faker import Faker


class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER_URL = f'{BASE_URL}api/auth/register'


class UserHelper:

    @staticmethod
    @allure.step('Регистрация пользователя')
    def reg_user():
        payload = {
            'email': UserHelper.generate_email(),
            'password': UserHelper.generate_password(),
            'name': UserHelper.generate_name()
        }
        response = requests.post(Urls.REGISTER_URL, data=payload)
        response.raise_for_status()
        return payload

    @staticmethod
    @allure.step('Генерация email')
    def generate_email():
        fake = Faker()
        email = fake.email()

        return email

    @staticmethod
    @allure.step('Генерация пароля')
    def generate_password():
        generated_password = ''
        for i in range(7):
            generated_password += random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )

        return generated_password

    @staticmethod
    @allure.step('Генерация имени')
    def generate_name():
        fake = Faker()
        username = fake.name()

        return username
