from cryptography.fernet import Fernet

f_key = Fernet.generate_key()
print("KEY: " + str(f_key))
f_enc = Fernet(f_key)

enc_string = f_enc.encrypt(b"Password_2_be_kept_secret!")

print("ENCRYPTED: " + str(enc_string))
print("DECRYPTED: " + str(f_enc.decrypt(enc_string)))