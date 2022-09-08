from __future__ import annotations
import numpy as np


class CaesarCipher:
    """Caesar Cipher class"""

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self) -> CaesarCipher:
        pass

    def _calculate_word(
        self, word: str, displacement: int, decrypt_mode: bool = False
    ) -> str:
        """Encrypt or decrypt a given word using Caesar Cipher method.

        Args:
            word (str): A word to be encrypted/decrypted.
            displacement (int): A positive integer number that represents
                                the displacement that will be applied in the
                                alphabet.
            decrypt_mode (bool, optional): Puts the method on encryption mode.
                                           Defaults to False.

        Returns:
            str: A encrypted/decrypted word.
        """
        if displacement >= 0:

            word = word.lower()
            sign = (-1) ** (int(decrypt_mode))
            char_idx_array = np.array([self.ALPHABET.index(char) for char in word])
            char_idx_array_after_displacement = (
                char_idx_array + sign * displacement
            ) % len(self.ALPHABET)

            new_word = ""

            for index in char_idx_array_after_displacement:
                new_word += self.ALPHABET[index]

            return new_word
        else:

            raise ValueError(
                "Negative number! This function only accepts positive integer numbers as displacement!"
            )

    def encrypt(self, word: str, displacement: int) -> str:
        """Return an encrypted word.

        Args:
            word (str): A word to be encrypted.
            displacement (int): A positive integer number that represents
                                the displacement that will be applied in the
                                alphabet.

        Returns:
            str: A encrypted word.
        """
        return self._calculate_word(word=word, displacement=displacement)

    def decrypt(self, word: str, displacement: int) -> str:
        """Return a decrypted word.

        Args:
            word (str): A word to be decrypted.
            displacement (int): A positive integer number that represents
                                the displacement that will be applied in the
                                alphabet.

        Returns:
            str: A decrypted word.
        """
        return self._calculate_word(
            word=word, displacement=displacement, decrypt_mode=True
        )
