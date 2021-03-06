from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


"""
with open("key2.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password='OhShit',
        backend=default_backend()
    )

#Serialization
pem = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.BestAvailableEncryption(b'OhShit')
)
pem.splitlines()[0]
b'-----BEGIN ENCRYPTED PRIVATE KEY-----'


#Signing
message = b"U R A HOE"
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)


#Verification
public_key = private_key.public_key()
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
"""

#Encryption
def encryptmessage( message, public_key):
	message = b"U R A Hoe"
	ciphertext = public_key.encrypt(
    	message,
    	padding.OAEP(
        	mgf=padding.MGF1(algorithm=hashes.SHA256()),
        	algorithm=hashes.SHA256(),
        	label=None
   	)
	)
	return ciphertext

#Decrypt
def decryptmessage( private_key,ciphertext):
	plaintext = private_key.decrypt(
    	ciphertext,
    	padding.OAEP(
        	mgf=padding.MGF1(algorithm=hashes.SHA256()),
        	algorithm=hashes.SHA256(),
        	label=None
    	)
	)
	return plaintext

