from faker import Faker
import random


fake = Faker(locale='ru_RU')


email_domains = [
    'gmail.com',
    'yandex.ru',
    'mail.ru',
    'outlook.com'
]


def generate_user_data():
    user_name = fake.unique.user_name()
    domain = random.choice(email_domains)
    email = f'{user_name}@{domain}'

    return {
        'email': email,
        'password': fake.password(length=10),
        'name': fake.first_name()
    }
