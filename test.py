from aes128.main import aes128_encrypt, aes128_decrypt

key = b"1234567890123456" # 16 bytes
pt  = b"gal_is_the_best_" # 16 bytes

ct = aes128_encrypt(key, pt)
decrypted_ct = aes128_decrypt(key, ct)

print(decrypted_ct)