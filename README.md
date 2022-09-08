# Cryptography

<!-- [![main](https://github.com/jvscursulim/cryptography/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/jvscursulim/cryptography/actions/workflows/ci.yml) -->
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description

Implementations of some cryptographics methods

## License

[GNU GPL v.3.0](https://github.com/jvscursulim/cryptography/LICENSE)

## Example

```python
from crypto import CaesarCipher, EncryptionKey

caesar = CaesarCipher()

word_encrypted = caesar.encrypt(word="xyz", displacement=3)
word_decrypted = caesar.decrypt(word="abc", displacement=3)

enckey = EncryptionKey()

word_encrypted2 = enckey.encrypt(word="physics", key="sun")
word_decrypted2 = caesar.decrypt(word="hblkcpk", key="sun")
```
