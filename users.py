import json
from werkzeug.security import generate_password_hash

users = {
    "chair": {
        "password": str(generate_password_hash("ieee123")),
        "role": "chair"
    },
    "secretary": {
        "password": str(generate_password_hash("sb2024")),
        "role": "secretary"
    },
    "vicechair": {
        "password": str(generate_password_hash("vssutvc")),
        "role": "vicechair"
    },
    "treasurer": {
        "password": str(generate_password_hash("bankieee")),
        "role": "treasurer"
    },
    "webmaster": {
        "password": str(generate_password_hash("ieeedev")),
        "role": "webmaster"
    }
}

with open("users.py", "w") as f:
    py.dump(users, f, indent=4)

print("users.py created with hashed passwords and roles.")