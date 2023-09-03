#!/usr/bin/python3

from jinja2.exceptions import UndefinedError
from ansible.errors import AnsibleUndefinedVariable, AnsibleFilterError
from ansible.module_utils.common.text.converters import to_native

def luhn_check_digit(number):
    try:
        reversed_number = str(number)[::-1]
        total = 0
        for index, digit in enumerate(reversed_number):
            digit = int(digit)
            if index % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
        check_digit = (10 - (total % 10)) % 10
        return str(check_digit)
    except UndefinedError as e:
        raise AnsibleUndefinedVariable(to_native(e))
    except Exception as e:
        raise AnsibleFilterError(to_native(e))

class FilterModule(object):
    def filters(self):
        return {'luhn_check_digit': luhn_check_digit}


