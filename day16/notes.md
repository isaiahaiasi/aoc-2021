# Day 16 - Packet Decoder

hex input -> binary interpretation

```
0xD2FE28
110100101111111000101000
VVVTTTAAAAABBBBBCCCCC
```
decodes to:
```
0111 1110 0101
```
or 2021, in decimal

V - 3 bit packet version (110 -> v6)
T - 3 bit packet type ID (100 -> 4 -> Literal Value)
A, B - five bit groups, start w/ 1 (not last group), contain 4 bits each of the number (minus leading bit)
C - starts with 0, so this is the last bit. Read the 4 data bits.
Unmarked - extra, don't care

OTHER TYPES (not 4) are OPERATORS
Operator packet contains 1+ packets