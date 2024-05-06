from collections import UserDict
from .Record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if (not self.__exists(record.name)):
            self.data[record.name.value] = record
        else:
            raise KeyError(f'Record with name "{
                           record.name}" is already exist')

    def find(self, name: str) -> Record:
        if (self.__exists(name)):
            return self.data[name]
        else:
            raise KeyError(f'Record with name "{name}" is not exist')

    def delete(self, name: str):
        if (self.__exists(name)):
            del self.data[name]
        else:
            raise KeyError(f'Record with name "{name}" is not exist')

    def __exists(self, name: str) -> bool:
        return name in self.data
