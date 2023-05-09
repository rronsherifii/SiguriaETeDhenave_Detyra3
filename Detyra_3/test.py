# sub keys
# Key = 64 bit hex -> binary √
# Gjenru dictionary me indeksa √
# Key 64 bit e kthejme ne 56 bit dhe e bejme PC1 (permes PC1) √
# Key 56 bit, sherben si hyrje per round 1
# Round 1: Key 56 bit ndahet ne dy pjese dhe secila behet shift left (varet) dhe behen join
# Round 2: Key 56 bit nga round 1, ndahet ne dy pjese dhe behet shift left, dhe join
# ...
# Round i: Key 56 bit nga round i-1, ndahet ne dy pjese behet shift left dhe join
# ...
# Per secilin round kemi nje PC2, i cili na i kthen ne 48 bit dhe i ben permute

from FeistelCipher import *
from SubKeyGenerator import *

message = "Hello Guys"
message2 = "HlÍ<k::3ÏËC5pÏI"
key = '1234567887654321'

feistel = FeistelCipher(message2, key)

feistel.execute_d()

