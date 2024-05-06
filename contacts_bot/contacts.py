from .decorators import input_error_catch, require_two_args, name_min_length
from .helpers import exists

@input_error_catch
@require_two_args
@name_min_length
def add_contact(args, contacts):
    name, phone = args
    if (not (name and phone)):
        raise ValueError('Name and phone shouldn\'t be empty')

    if (exists(name, contacts)):
        raise KeyError('The user is already exsist')

    contacts[name] = phone
    return "Contact added."


@input_error_catch
@require_two_args
@name_min_length
def change_contact(args, contacts):
    name, phone = args
    if (not (name and phone)):
        raise ValueError('Name and phone shouldn\'t be empty')

    if (not exists(name, contacts)):
        raise KeyError('The user is not exsist')

    contacts[name] = phone
    return "Contact updated."


@input_error_catch
def get_contact_phone(args, contacts):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: name')
    name = args[0]
    if (not name):
        raise ValueError('Name shouldn\'t be empty')

    if (not exists(name, contacts)):
        raise KeyError('The user is not exsist')

    return contacts[name]


def get_all(contacts):
    res = ''
    for name, phone in contacts.items():
        res += f"{name} {phone}\n"
    return res
