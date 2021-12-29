from cryptography.fernet import Fernet
import rsa

msg = "hello world!"

key = Fernet.generate_key()
f = Fernet(key)

cryp_msg = f.encrypt(msg.encode())
decryp_msg = f.decrypt(cryp_msg)
print("-- Fernet --")
print("original - %s" % msg)
print("encrypted - %s" % cryp_msg)
print("encrypted - %s" % decryp_msg.decode())

publicKey, privateKey = rsa.newkeys(512)

rsa_cryp = rsa.encrypt(msg.encode(), publicKey)
print("\n")
print("-- RSA --")
print("original - %s" % msg)
print("encrypted - %s" % rsa_cryp)
rsa_decryp = rsa.decrypt(rsa_cryp, privateKey).decode()
print("decrypted - %s" % rsa_decryp)
