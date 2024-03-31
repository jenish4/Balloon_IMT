# Jenish SHAH IMT Atlantique Rennes 03/24
# This script takes the string of balloon coreconf data and decodes it 
# Example in CLI:$ python3 decode.py DgGhGQPrGXOvAAAAAAAAAA==

import pycoreconf
import base64
import re
import sys

# convert the input string to useful cbor data
arguments = sys.argv
data_base64 = arguments[1]
data_bytes= base64.b64decode(data_base64) 
data_hex = data_bytes.hex() 
req_data= data_hex[4:18]
cbor_data = bytes.fromhex(req_data)

# decode
ccm = pycoreconf.CORECONFModel("balloon@unknown.sid") # Create the model object
decoded_json = ccm.toJSON(cbor_data)
temperature = (float(re.sub(r'\D', '', decoded_json))-27300)/100
print("Decoded data in json:", decoded_json)
print("Temperature in celcius:", temperature)
