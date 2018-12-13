# An extremely basic text encrypter and decrypter

from cryptography.fernet import Fernet
cipher_key = Fernet.generate_key()
print("The cipher key is: " + str(cipher_key))
cipher = Fernet(cipher_key)
text = input(str("Enter the secret message: "))
inputText = text.encode() 
encryptedText = cipher.encrypt(inputText)
print("The encrypted text is: " + str(encryptedText))
decryptedText = cipher.decrypt(encryptedText)
