def split_chunks(data: bytes, size: int = 16):
    """
    Generator that splits the input data into chunks of the given size.
    """
    for i in range(0, len(data), size):
        yield data[i:i+size]

class PKCS7:
    @staticmethod
    def pad(data: bytes, size: int = 16) -> bytes:
        """
        Returns the data padded so its length is a multiple of size.
        """
        padding_size: int = size - (len(data) % size)
        padding: bytes = bytes([padding_size]) * padding_size
        return data + padding

    @staticmethod
    def unpad(data: bytes, size: int = 16):
        """
        Return the original data from padded data.
        """
        padding_size: int = int(data[-1])
        return data[:-padding_size]

    @staticmethod
    def test():
        data = input("Enter data to test: ").encode()
        padded = PKCS7.pad(data)
        unpadded = PKCS7.unpad(padded)

        print(f"Original data: {data}, length: {len(data)}")
        print(f"Padded: {padded}")
        print(f"Unpadded: {unpadded}")
        print("Success!" if data == unpadded else "Fail!")

if __name__ == '__main__':
    PKCS7.test()
