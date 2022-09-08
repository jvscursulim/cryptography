import pytest
from crypto import CaesarCipher


class TestCaesarCipher:
    def test_encrypt(self):

        words = ["abc", "xyz", "sun", "moon", "apple"]
        displacement_list = [1, 3, 26, 35, 0]
        caesar = CaesarCipher()
        encrypted_words = [
            caesar.encrypt(word=word, displacement=displacement)
            for word, displacement in zip(words, displacement_list)
        ]

        assert encrypted_words[0] == "bcd"
        assert encrypted_words[1] == "abc"
        assert encrypted_words[2] == "sun"
        assert encrypted_words[3] == "vxxw"
        assert encrypted_words[4] == "apple"

    def test_decrypt(self):

        encrypted_words = ["bcd", "abc", "sun", "vxxw", "apple"]
        displacement_list = [1, 3, 26, 35, 0]
        caesar = CaesarCipher()
        decrypted_words = [
            caesar.decrypt(word=word, displacement=displacement)
            for word, displacement in zip(encrypted_words, displacement_list)
        ]

        assert decrypted_words[0] == "abc"
        assert decrypted_words[1] == "xyz"
        assert decrypted_words[2] == "sun"
        assert decrypted_words[3] == "moon"
        assert decrypted_words[4] == "apple"

    def test_caesar_cipher_value_error(self):

        caesar = CaesarCipher()
        with pytest.raises(
            ValueError,
            match="Negative number! This function only accepts positive integer numbers as displacement!",
        ):
            _ = caesar.encrypt(word="abc", displacement=-1)
        with pytest.raises(
            ValueError,
            match="Negative number! This function only accepts positive integer numbers as displacement!",
        ):
            _ = caesar.decrypt(word="abc", displacement=-1)
