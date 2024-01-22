from typing import TypedDict, Required, NotRequired


class Registration(TypedDict):
    reg_1: int
    reg_2: int
    name_1: Required[str]
    name_2: NotRequired[str]


reg: Registration = {'reg_1': 1, 'reg_2': 2, 'name_1': 'Jayanth',
                     'name_2': 'shannu'}  # here the dictionary of Registration type we use TypeDict library to do so

print(reg)
