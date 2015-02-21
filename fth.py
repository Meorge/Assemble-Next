# Code is from http://stackoverflow.com/questions/23624212/how-to-convert-a-float-into-hex
# Thanks to Jonathon Reinhart for le code, although I doubt he'll ever read this.

import struct

def floattohex(f):
    return hex(struct.unpack('>I', struct.pack('>f', f))[0])

def hextofloat(f):
    return struct.unpack('>f', struct.pack('>I', int(f, 0)))[0]
# return struct.pack('>f', int(f[2:], 16))

print(floattohex(5.0))
# repr(floattohex(5.0))
# print(hextofloat(0x40a00000))
# repr(hextofloat(0x40a00000))
