import os
import uuid
from Crypto.Cipher import DES


class EncryptDecrypt:
    def __init__(self):
        self.key = os.urandom(8)
        self.des = DES.new(self.key, DES.MODE_ECB)

    @staticmethod
    def pad_space(source_text):
        while len(source_text) % 8 != 0:
            source_text += ' '
        return source_text

    @staticmethod
    def write_file(encrypted_text):
        fileHandler = open('encrypted_str.bin', 'wb')
        fileHandler.write(encrypted_text)

    @staticmethod
    def read_file():
        fileHandler = open('encrypted_str.bin', 'rb')
        encrypted_text = fileHandler.read()
        return encrypted_text

    def do_encryption(self, source_text):
        padded_text = EncryptDecrypt.pad_space(source_text)
        encrypted_text = self.des.encrypt(padded_text)
        EncryptDecrypt.write_file(encrypted_text)

    def do_decryption(self):
        encrypted_text = EncryptDecrypt.read_file()
        decrypted_text = self.des.decrypt(encrypted_text)
        target_text = decrypted_text.decode('utf-8').strip()

        EncryptDecrypt.cleanup()
        return target_text

    @staticmethod
    def cleanup():
        if os.path.exists('encrypted_str.bin'):
            os.remove('encrypted_str.bin')
        else:
            print('File cleanup failed. Please delete the encrypted_str.bin file manually !!!')


if __name__ == '__main__':
    client_obj = EncryptDecrypt()
    source_text = 'Amritha01@'
    client_obj.do_encryption(source_text)

    client_obj.write_file(client_obj.key)
    target_text = client_obj.do_decryption()

    print(source_text == target_text)
