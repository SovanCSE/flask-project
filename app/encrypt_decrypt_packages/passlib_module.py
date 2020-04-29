from passlib.hash import  pbkdf2_sha256

password = "spwelcome12345"
encrypted_password =pbkdf2_sha256.hash(password)
print("encrypted_password", encrypted_password)

print("Verify encrypted password", pbkdf2_sha256.verify('Sp721427, '
                                                        '$pbkdf2-sha256$29000$xNjbO0dIae19b83Zey9FyA$VsB/fU...'))