from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

salt = b"!l0ng*rand0m%salt$string@"

# DERIVING THE HASH
s_enc = Scrypt(
                salt=salt,
                length=64,
                n=2048,
                r=8,
                p=1,
            )
enc_pword = s_enc.derive(b"Password_2_be_kept_secret!")
print("Derived Key: " + str(enc_pword))

# VERIFYING THE HASH
s_enc = Scrypt(
    salt=salt,
    length=64,
    n=2048,
    r=8,
    p=1,
)

print("Password Exception: ")
#print(s_enc.verify(b"Password_2_be_kept_secret!", enc_pword))
print(s_enc.verify(b"Password_2_be_kept_secret", enc_pword))