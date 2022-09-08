from crypto import EncryptionKey


class TestEncryptionKey:
    def test_encrypt(self):

        words = ["physics", "apple", "computer", "quantum", "shibainu"]
        keys = ["sun", "short", "warrior", "dice", "pineapple"]
        enckey = EncryptionKey()

        encrypted_words = [
            enckey.encrypt(word=word, key=key) for word, key in zip(words, keys)
        ]

        assert encrypted_words[0] == "hblkcpk"
        assert encrypted_words[1] == "swdcx"
        assert encrypted_words[2] == "yodgchvn"
        assert encrypted_words[3] == "tccrwco"
        assert encrypted_words[4] == "hpvfaxcf"

    def test_decrypt(self):

        encrypted_words = ["hblkcpk", "swdcx", "yodgchvn", "tccrwco", "hpvfaxcf"]
        keys = ["sun", "short", "warrior", "dice", "pineapple"]
        enckey = EncryptionKey()

        decrypted_words = [
            enckey.decrypt(word=word, key=key)
            for word, key in zip(encrypted_words, keys)
        ]

        assert decrypted_words[0] == "physics"
        assert decrypted_words[1] == "apple"
        assert decrypted_words[2] == "computer"
        assert decrypted_words[3] == "quantum"
        assert decrypted_words[4] == "shibainu"
