# PART 1 - SUM VERSION NUMBERS OF PACKETS
# parse heirarchy of packets

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
            # type = "literal"
            # no subpackets, so right now I can just return (base case)
            self.parse_literal()
        else:
            # type = "operator"
            if self.parsebits(1):
                # length type = 1 (subpacket count)
                subpacket_count = self.parsebits(11)
                for _ in range(subpacket_count):
                    self.parse_packet()
            else:
                # length type = 0 (subpackets by total bit length)
                subpacket_bit_len = self.parsebits(15)
                curptr = self.ptr
                while self.ptr < curptr + subpacket_bit_len:
                    self.parse_packet()

    def parse_literal(self):
        numbits = ''
        # read bits until leading bit is '1' (indicating last series)
        while ((bits := self.readbits(5))[0] == '1'):
            numbits += bits[1:]
        numbits += bits[1:]
        num = int(numbits, 2)
        print("LITERAL VALUE:", num)
        return num


if __name__ == "__main__":
    bd = get_data("input/input.txt")
    packetParser = PacketParser(bd)
    packetParser.parse_packet()
    print("version sum:", packetParser.v_sum)
