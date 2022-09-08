from crypto import CaesarCipher, EncryptionKey

caesar = CaesarCipher()

word_encrypted = caesar.encrypt(word="xyz", displacement=3)
word_decrypted = caesar.decrypt(word="abc", displacement=3)

enckey = EncryptionKey()

word_encrypted2 = enckey.encrypt(word="physics", key="sun")
word_decrypted2 = caesar.decrypt(word="hblkcpk", key="sun")