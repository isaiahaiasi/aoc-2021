# PART 1 - SUM VERSION NUMBERS OF PACKETS
# parse heirarchy of packets
from math import prod


def get_bin(hexdata: str):
    h_size = len(hexdata) * 4
    return (bin(int(hexdata, 16))[2:]).zfill(h_size)  # strips off "0b"


def get_data(path) -> bytes:
    with open(path, 'r') as fp:
        data = fp.read()
    return get_bin(data)


# right now, just return total versions
# recursively call parse_packet to get heirarchical sum
class PacketParser:
    def __init__(self, data):
        self.data = data
        self.ptr = 0
        self.v_sum = 0

    def parsebits(self, count: int):
        return int(self.readbits(count), 2)

    def readbits(self, count: int):
        data = self.data[self.ptr: self.ptr + count]
        self.ptr += count
        return data

    def parse_packet(self):
        version = self.parsebits(3)
        self.v_sum += version

        typeid = self.parsebits(3)
        print("TYPE:", "LIT" if typeid == 4 else "OP")
        print("VERSION:", version)

        if typeid == 4:
            # type 4 is a literal, so no subpackets
            return self.get_packet_fn(typeid)()

        # type = "operator"
        subpacket_values = []

        if self.parsebits(1):
            # length type = 1 (subpacket count)
            subpacket_count = self.parsebits(11)
            for _ in range(subpacket_count):
                subpacket_values.append(self.parse_packet())
        else:
            # length type = 0 (subpackets by total bit length)
            subpacket_bit_len = self.parsebits(15)
            curptr = self.ptr
            while self.ptr < curptr + subpacket_bit_len:
                subpacket_values.append(self.parse_packet())

        return self.get_packet_fn(typeid)(subpacket_values)

    def parse_literal(self):
        numbits = ''
        # read bits until leading bit is '1' (indicating last series)
        while ((bits := self.readbits(5))[0] == '1'):
            numbits += bits[1:]
        numbits += bits[1:]
        num = int(numbits, 2)
        print("LITERAL VALUE:", num)
        return num

    def get_packet_fn(self, i: int):
        packet_fns = [
            sum,
            prod,
            min,
            max,
            self.parse_literal,
            lambda x: 1 if x[0] > x[1] else 0,     # greater than
            lambda x: 1 if x[0] < x[1] else 0,     # less than
            lambda x: 1 if x[0] == x[1] else 0     # equal to
        ]
        return packet_fns[i]


if __name__ == "__main__":
    bd = get_data("input/input.txt")
    # bd = get_bin("9C0141080250320F1802104A08")
    packetParser = PacketParser(bd)
    val = packetParser.parse_packet()
    print(val)
