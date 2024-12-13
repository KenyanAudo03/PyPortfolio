from werkzeug.security import generate_password_hash, check_password_hash

password = input("Enter your password: ")

password_hash = generate_password_hash(password)
print(password_hash)

real_password = check_password_hash(password_hash, password)
print(real_password)