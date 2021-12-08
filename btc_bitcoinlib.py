
#%%
import bitcoinlib as btl
from bitcoinlib.wallets import wallet_delete_if_exists

passphrase = btl.mnemonic.Mnemonic().generate()
print(passphrase)
nome = "prova_legacy"
if wallet_delete_if_exists(nome): pass
k = btl.wallets.Wallet.create(nome)
print("Nome wallet appena creato: ", k)

print("seckey wif: ", k.get_key().wif)
# %%
