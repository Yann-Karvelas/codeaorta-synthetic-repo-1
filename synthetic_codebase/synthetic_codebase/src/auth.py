import hashlib
import os  # Unused

# Finding 1: Insecure Hash
def hash_password(password):
    hashed_pass = hashlib.md5(password.encode()).hexdigest()
    return hashed_pass

# Finding 2: Hardcoded Secret
SECRET_KEY = "my_super_secret_key_123"
