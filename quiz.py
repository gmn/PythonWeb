
print( ''.join( ( chr(i) for i in [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 115, 100, 102, 103, 119, 114, 52, 52, 104, 114, 102, 104, 102, 104, 45, 119, 115 ] ) ) )

from cryptography import fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcsezP__hT8O3nyYmNROsgfTfWqkeXWhaEUephTvXmuRlNdP1FH5lLG8ukbmLRTt5H5BLkqBF6p1znz030qI8k4HF2UiG82W1iwLgaOhD7DZ74-aNCzb4U5onnhG3JWMTo-gmbL_36wZajyyv4mrcu8JfM4qHzABNV4lJO2juvYLVY4GvxVE_ZRC1mdYN8wNpbjGA1'

def main():
    f = fernet.Fernet(key)
    print(f.decrypt(message))

if __name__ == "__main__":
    main()
