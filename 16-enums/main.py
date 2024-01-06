from enum import Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE.value)
print(State.INACTIVE.value)

print(State(0).name)
print(State(1).name)

print(State['ACTIVE'].value)
print(State['INACTIVE'].value)

print(list(State))
print(len(State))
