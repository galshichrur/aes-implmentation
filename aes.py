from aes128.aes import AES

key = b"1234567890123456" # 16 bytes
pt  = b"gal_is_the_best_" # 16 bytes

aes = AES(key)
ct = aes.aes128_encrypt(pt)
decrypted_ct = aes.aes128_decrypt(ct)

print(decrypted_ct)