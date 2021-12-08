#%%
import ecdsa, binascii, hashlib, base58

#generate private key
priv_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk = priv_key.to_pem()
print("Private key")
print("Binary : ", priv_key.to_string())
print("Hex : ", priv_key.to_string().hex())

#calculate public key
pub_key = '04' + priv_key.get_verifying_key().to_string().hex()
print("Public key: ",pub_key)

#calculate address
#calculate sha256
hash256 = hashlib.sha256(binascii.unhexlify(pub_key)).hexdigest()
print("sha256 of public key: ",hash256)
#calculate ripemd160
ripemd = hashlib.new('ripemd160',binascii.unhexlify(hash256)).hexdigest()
print("ripemd: ", ripemd)

#prefix 00
prep = '00' + ripemd
print("prepend network byte to ripemd(sha256(public)): ",prep)

#calculate checksum
hash = prep
for i in range(1, 3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    print("sha256 ",i,": ",hash)

checksum = hash[:8]
print("checksum :",checksum)

appendchecksum = prep + checksum
print("append checksum to to ripemd(sha256(public)): ",appendchecksum)

#base58 encoding
address = base58.b58encode(binascii.unhexlify(appendchecksum)).decode('utf8')
print("bitcoin address: ",address)
# %%
