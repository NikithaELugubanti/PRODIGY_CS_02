try:
    path = r'C:\Users\USER\Downloads\python.jpg'
    key = int(input('Enter Key for decryption of Image: '))
    print('The path of file:', path)
    print('Note: The encryption key and decryption key must be the same.')
    print('Key for Decryption:', key)
    with open(path, 'rb') as fin:
        image = fin.read()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    with open(path, 'wb') as fout:
        fout.write(image)

    print('Decryption Done...')
except Exception as e:
    print('Error caught:', e)
