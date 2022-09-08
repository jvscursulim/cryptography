from __future__ import annotations
import numpy as np


class EncryptionKey:
    """Encryption Key class"""

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self) -> EncryptionKey:
        pass

    def _calculate_word(self, word: str, key: str, decrypt_mode: bool = False) -> str:
        """Encrypt or decrypt a given word using Encryption Key method.

        Args:
            word (str): A word to be encrypted/decrypted.
            key (str): The key that will be used to encrypt/decrypt.
            decrypt_mode (bool, optional): Puts the method on encryption mode.
                                           Defaults to False.

        Returns:
            str: A encrypted/decrypted word.
        """
        word = word.lower()
        key = key.lower()
        sign = (-1) ** (int(decrypt_mode))
        char_word_idx_array = np.array([self.ALPHABET.index(char) for char in word])
        if len(key) > len(word):

            char_key_idx_array = np.array(
                [self.ALPHABET.index(char) for char in key[: len(word)]]
            )
            new_word_char_idx = (char_word_idx_array + sign * char_key_idx_array) % len(
                self.ALPHABET
            )
        elif len(key) < len(word):

            char_key_idx_array = np.array(
                [self.ALPHABET.index(key[i % len(key)]) for i in range(len(word))]
            )
            new_word_char_idx = (char_word_idx_array + sign * char_key_idx_array) % len(
                self.ALPHABET
            )
        else:

            char_key_idx_array = np.array([self.ALPHABET.index(char) for char in key])
            new_word_char_idx = (char_word_idx_array + sign * char_key_idx_array) % len(
                self.ALPHABET
            )

        new_word = ""
        for index in new_word_char_idx:
            new_word += self.ALPHABET[index]

        return new_word

    def encrypt(self, word: str, key: str) -> str:
        """Return an encrypted word

        Args:
            word (str): A word to be encrypted.
            key (str): The key that will be used to encrypt.

        Returns:
            str: A encrypted word.
        """
        return self._calculate_word(word=word, key=key)

    def decrypt(self, word: str, key: str) -> str:
        """Return a decrypted word.

        Args:
            word (str): A word to be decrypted.
            key (str): The key that will be used to decrypt.

        Returns:
            str: A decrypted word.
        """
        return self._calculate_word(word=word, key=key, decrypt_mode=True)
