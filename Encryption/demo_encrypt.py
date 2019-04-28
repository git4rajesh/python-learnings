from cryptography.fernet import Fernet
import pickle


class EncryptDecrypt:
    def __init__(self):
        key = Fernet.generate_key()
        self.fernet_obj = Fernet(key)


        str_key = key.decode('utf-8')
        fileHandler = open('pickleFile.txt', 'w')
        print('>>>', type(str_key), str_key)
        pickle.dump(str_key, fileHandler)


    def do_encryption(self, source_str):
        source_str_in_bytes = source_str.encode('utf-8')
        return self.fernet_obj.encrypt(source_str_in_bytes).decode('utf-8')

    def do_decryption(self, encrypted_str):
        encrypted_str_in_bytes = encrypted_str.encode('utf-8')
        source_str_in_bytes = self.fernet_obj.decrypt(encrypted_str_in_bytes)
        return source_str_in_bytes.decode('utf-8')


if __name__ == '__main__':
    client_obj = EncryptDecrypt()
    encrypted_str = client_obj.do_encryption('Amritha01@')
    print('Encryption Done', encrypted_str)
    # decrypted_str = client_obj.do_decryption(encrypted_str)
    # print('Decryption Done', decrypted_str)



