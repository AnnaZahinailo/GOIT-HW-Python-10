from collections import UserDict


class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)


class Name(Field): 
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name:Name, phone:Phone=None) -> None:
        self.name = name
        self.phone = phone

    phone_list = []

    def add_phone(self, phone:Phone):
        if phone:
            self.phone_list.append(phone.value)

    def change_phone(self, phone:Phone, new_phone:Phone):
        ind = self.phone_list.index(phone.value)
        self.phone_list[ind] = new_phone.value


    def delete_phone(self, phone:Phone):
        if phone.value in self.phone_list:
            self.phone_list.remove(phone.value)


class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data.update({record.name.value: record.phone_list})
