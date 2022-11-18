from dataclasses import dataclass, field
import dataclasses

@dataclass
class User:
    name: str
    permission_level: int = 0 # We can specify optional defaults


class AltUser:
    def __init__(self, name:str):
        self.name = name



# __init__ method has been created for us
test_user = User("dan")
test_user2 = User("dan")

test_alt_user = AltUser("fred")
test_alt_user2 = AltUser("fred")

if test_alt_user == test_alt_user2:
    print("non-dataclass users are equal")

# __eq__ method has been created for us
if test_user == test_user2:
    print("dataclass users are equal")

# __repr__ method has been created for us 
print("DATACLASS USER: ", test_user)
print("NON-DATACLASS USER: ", test_alt_user)

# Here we see some optional parameters, a very useful one being the frozen=true for immutability

@dataclass(frozen=True)
class immutableUser:
    name:str
    permission_level:str = 0

test_immutable_user = immutableUser("test",2)

try:
    test_immutable_user.name = "test2"
except dataclasses.FrozenInstanceError:
    print("You can't change an immutable dataclass")


# Here you can see how to set mutable defaults safely in dataclasses

@dataclass
class Manager:
    employees: list[User] = field(default_factory=list)