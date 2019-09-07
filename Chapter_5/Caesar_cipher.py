"""
5.5.3 Simple Cryptography
Page 216
"""


class CaesarCipher:
    def __init__(self, shift):
        self._shift = shift
        encoder = [None] * 26
        decoder = [None] * 26
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._encoder = ''.join(encoder)
        self._decoder = ''.join(decoder)

    def encrypt(self, message):
        msg = list(message)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = (ord(msg[k]) - ord('A')) % 26
                msg[k] = self._encoder[j]
        return ''.join(msg)

    def decrypt(self, message):
        msg = list(message)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = (ord(msg[k]) + ord('A')) % 26
                msg[k] = self._decoder[j]
        return ''.join(msg)


if __name__ == '__main__':
    obj = CaesarCipher(2)
    cipher = obj.encrypt(input('Upper characters:'))
    print(cipher)
    check = obj.decrypt(cipher)
    print(check)
