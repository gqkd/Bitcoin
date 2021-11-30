#%%
from bitcoin import *

#generate a random secret key
secret_key = random_key()
print(f"secret key in hex format {secret_key}\n")

#to indicate the compressed private key add 01 as suffix
secret_key_compressed = secret_key + '01'
print(f"secret key compressed in hex format {secret_key_compressed}\n")

#convert the secret key in decimal form
secret_key_decimal = decode_privkey(secret_key,'hex')
print(f"secret key in decimal format {secret_key_decimal}\n")

#secret key in wif
secret_key_wif = encode_privkey(secret_key_decimal,'wif')
print(f"secret key in wif format {secret_key_wif}\n")

#secret key in compressed wif
secret_key_wif_comp = encode_privkey(decode_privkey(secret_key_compressed,'hex'),'wif_compressed')
print(f"secret key in compressed wif format {secret_key_wif_comp}\n")

#to validate the secret key must be between 0 and N
print(f"the key is valid? {0<secret_key_decimal<N}")


# %%

#public key generation
public_key = fast_multiply(G,secret_key_decimal)
print(f"public key x,y coordinates {public_key}\n")

#encode as hex, prefix 04
public_key_hex = encode_pubkey(public_key,'hex')
print(f"public key in hex format {public_key_hex}\n")

#compressed public key
(x,y) = public_key
compressed_prefix = '02' if (y % 2) == 0 else '03'
public_key_hex_comp = compressed_prefix + (encode(x,16).zfill(64))
print(f"public key in compressed hex format {public_key_hex_comp}\n")

#address generation from public key
add = pubkey_to_address(public_key)
print(f"bitcoin address b58 {add}")

#compressed address generation from public key
add_comp = pubkey_to_address(public_key_hex_comp)
print(f"bitcoin compress address {add_comp}")

# %%
print(history("3EXgJzvdkVxiRCjNc9Mz1jzJzrdhkVCU58"))

# %%
