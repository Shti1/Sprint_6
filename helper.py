from faker import Faker

faker = Faker('ru_RU')

def generate_registration_data():
    first_name = faker.first_name()
    last_name = faker.last_name()

    # Генерация адреса без дробных домов
    street = faker.street_name()
    building = faker.random_int(1, 100)
    address = f"ул. {street}, д. {building}, кв. {faker.random_int(1, 100)}"

    unform_phone = faker.phone_number()
    phone = unform_phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    return first_name, last_name, address, phone  # Возвращаем кортеж (first_name, last_name, address, phone)
