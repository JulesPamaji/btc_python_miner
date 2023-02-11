from bitcoin import *

my_private_key = random_key()
print("Private Key: %sn" % my_private_key)
my_public_key = privtopub(my_private_key)
print("Public Key: %sn" % my_public_key)
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %sn" % my_bitcoin_address)