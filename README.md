
# Version Message

### Test Driven Exercise


```python
# Exercise 2.1

from io import BytesIO
from network import VersionMessage
from helper import (
    encode_varint,
    int_to_little_endian
)

class VersionMessage(VersionMessage):

    def serialize(self):
        '''Serialize this message to send over the network'''
        # version is 4 bytes little endian
        # services is 8 bytes little endian
        # timestamp is 8 bytes little endian
        # receiver services is 8 bytes little endian
        # IPV4 is 10 00 bytes and 2 ff bytes then receiver ip
        # receiver port is 2 bytes, little endian
        # sender services is 8 bytes little endian
        # IPV4 is 10 00 bytes and 2 ff bytes then sender ip
        # sender port is 2 bytes, little endian
        # nonce
        # useragent is a variable string, so varint first
        # latest block is 4 bytes little endian
        # relay is 00 if false, 01 if true
        pass
```
