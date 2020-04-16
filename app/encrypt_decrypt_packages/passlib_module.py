from passlib.hash import  pbkdf2_sha256

password = "spwelcome12345"
encrypted_password =pbkdf2_sha256.hash(password)
print("encrypted_password", encrypted_password)

print("Verify encrypted password", pbkdf2_sha256.verify(password, encrypted_password))