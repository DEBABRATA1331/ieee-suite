from werkzeug.security import generate_password_hash

users = {
    "chair": {
        "password": generate_password_hash("ieee123"),
        "role": "chair"
    },
    "secretary": {
        "password": generate_password_hash("sb2024"),
        "role": "secretary"
    },
    "vicechair": {
        "password": generate_password_hash("vssutvc"),
        "role": "vicechair"
    },
    "treasurer": {
        "password": generate_password_hash("bankieee"),
        "role": "treasurer"
    },
    "webmaster": {
        "password": generate_password_hash("ieeedev"),
        "role": "webmaster"
    }
}

# Write this as a proper Python file
with open("users.py", "w") as f:
    f.write("users = " + repr(users) + "\n")

print("users.py created with hashed passwords and roles.")
