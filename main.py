import random

import eth_utils.exceptions
import pyetherbalance
import web3
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/35e7bad38caf4bbca01316283f0f8c36")) #https://mainnet.infura.io/v3/35e7bad38caf4bbca01316283f0f8c36

acc = w3.eth.account.enable_unaudited_hdwallet_features()

infura_url = "https://mainnet.infura.io/v3/35e7bad38caf4bbca01316283f0f8c36"

ethbalance = pyetherbalance.PyEtherBalance(infura_url)


with open("text.txt", "r") as f:
    a = f.readlines()

word = []
for l in a:
    if len(l) != 1:
        word.append(l[:len(l) - 1])


b = 12
phrase = []
while True:
    try:
        w = word.copy()
        l = []
        for i in range(int(b)):
            s = random.choice(w)
            w.remove(s)
            l.append(s)
        phrase = " ".join(l)

        try:
            addr = w3.eth.account.from_mnemonic(phrase).address

            bal = w3.eth.get_balance(addr)
            if int(bal) > 0:
                print("[+] Success:", phrase, ":", bal, ":", addr)
        except eth_utils.exceptions.ValidationError:
            pass
        except Exception as e:
            print(e)
            print(phrase)
    except KeyboardInterrupt:
        break

print("[-] Finished!")
