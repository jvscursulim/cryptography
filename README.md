# Cryptography

[![cryptography](https://github.com/jvscursulim/cryptography/actions/workflows/ci.yaml/badge.svg?branch=master)](https://github.com/jvscursulim/cryptography/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/jvscursulim/cryptography/branch/master/graph/badge.svg?token=Y65L2MLO25)](https://codecov.io/gh/jvscursulim/cryptography)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description

Implementations of some basic cryptographics methods

## License

[GNU GPL v.3.0](https://github.com/jvscursulim/cryptography/LICENSE)

## Example

### How to use

```python
from crypto import CaesarCipher, EncryptionKey

caesar = CaesarCipher()

word_encrypted = caesar.encrypt(word="xyz", displacement=3)
word_decrypted = caesar.decrypt(word="abc", displacement=3)

enckey = EncryptionKey()

word_encrypted2 = enckey.encrypt(word="physics", key="sun")
word_decrypted2 = enckey.decrypt(word="hblkcpk", key="sun")
```

## References

[Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
