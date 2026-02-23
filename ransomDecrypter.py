import os
from cryptography.fernet import Fernet


def get_directory_path():
    directory_path = input("Enter the directory path to encrypt: ")
    
    if os.path.exists(directory_path):

        normalized_path = os.path.normpath(directory_path)
        return normalized_path
    else:
        print("Directory not found, please try again.")
        return get_directory_path()



def load_key():
    with open("encrypted_key.key","rb") as key_file:
        key=key_file.read()
    return key


def find_encrypted_files(directory_path):
    encrypted_files=[]
    for item in os.listdir(directory_path):
        full_path=os.path.join(directory_path,item)
        if os.path.isfile(full_path) and item.endswith(".encrypted"):
            encrypted_files.append(full_path)
    return encrypted_files


def decrypt_files(file_list, key):
    cipher=Fernet(key)

    for file_path in file_list:

        with open(file_path,"rb") as encrypted_file:
            encrypted_data=encrypted_file.read()
        decrypted_data=cipher.decrypt(encrypted_data)
        with open(file_path,"wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        new_path=file_path[:-10]
        os.rename(file_path,new_path)

        print(f"decrypted {new_path}")



def main():
    
    directory_path=get_directory_path()
    key=load_key()
    encrypted_files=find_encrypted_files(directory_path)

    if encrypted_files:
        print(f"found {len(encrypted_files)} encrypted files. Starting decryption...")
        decrypt_files(encrypted_files, key)
        print("\nSUCCESS: All target files are now decrypted.")
    else:
        print("No target files found in the directory.")
    

if __name__ == "__main__":
    main()
