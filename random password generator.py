import random
import string

# extracting ascii
upper =string.ascii_uppercase
lower= string.ascii_lowercase
nun =string.digits
symbol=string.punctuation

# randomising each extract
up =random.sample(upper,2)
lo =random.sample(lower,2)
nu =random.sample(nun,2)
sy =random.sample(symbol,2)

# concatenating extractions
all = up + lo + nu + sy

# joing and removing spacing
passcode = ''.join(all)

# outputing the passcode
print('Generated passcode is: '+passcode)
