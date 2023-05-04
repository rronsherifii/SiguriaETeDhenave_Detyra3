# remove 8th parity bits
# pc1 for keys based on table
# divide key in two parts, shift the parts based on the round
# bits that are shifted left in the beginning are appended at the end of the part of the key
# Concatenate the two parts for each round
# for each of 16 subkeys, apply pc2 based on specified table like in pc1
# win 16 subkeys of des