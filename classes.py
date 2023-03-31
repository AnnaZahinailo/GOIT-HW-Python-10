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
    def __init__(self, name:Name, *phone:Phone) -> None:
        self.name = name
        self.phone = phone

    phone_list = []

    def add_phone(self, phone):
        if phone:
            self.phone_list.append(phone)

    def change_phone(self, phone, new_phone):
        if phone in self.phone_list:
            ind = self.phone_list.index(phone)
            self.phone_list[ind] = new_phone
        else:
            raise ValueError(f"The phone number {phone} is not in the list")

    def delete_phone(self, phone):
        if phone in self.phone_list:
            self.phone_list.remove(phone)


class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data.update({record.name.value: record.phone_list})
