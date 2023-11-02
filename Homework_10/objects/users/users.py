import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    month_of_birth: str
    year_of_birth: str
    day_of_birth: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str