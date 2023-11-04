class Mem:
    MAX_MEM = 1024 * 64
    Data = [0] * MAX_MEM

    def initialize(self):
        self.Data = [0] * self.MAX_MEM

class CPU:
    def __init__(self):
        self.PC = 0 # program counter
        self.SP = 0 # stack pointer

        # registers
        self.A = 0
        self.X = 0
        self.Y = 0

        # status flags
        self.flags = 0b1111111

    def set_flag_C(self, value: int):
        if value:
            self.flags |= 0b0000001
        else:
            self.flags &= 0b1111110

    def check_flag_C(self) -> int:
        return (self.flags & 0b0000001)

    def set_flag_Z(self, value: int):
        if value:
            self.flags |= 0b0000010
        else:
            self.flags &= 0b1111101

    def check_flag_Z(self) -> int:
        return (self.flags & 0b0000010)

    def set_flag_I(self, value: int):
        if value:
            self.flags |= 0b0000100
        else:
            self.flags &= 0b1111011

    def check_flag_I(self) -> int:
        return (self.flags & 0b0000100)

    def set_flag_D(self, value: int):
        if value:
            self.flags |= 0b0001000
        else:
            self.flags &= 0b1110111

    def check_flag_D(self) -> int:
        return (self.flags & 0b0001000)

    def set_flag_B(self, value: int):
        if value:
            self.flags |= 0b0010000
        else:
            self.flags &= 0b1101111

    def check_flag_B(self) -> int:
        return (self.flags & 0b0010000)

    def set_flag_V(self, value: int):
        if value:
            self.flags |= 0b0100000
        else:
            self.flags &= 0b1011111

    def check_flag_V(self) -> int:
        return (self.flags & 0b0100000)

    def set_flag_N(self, value: int):
        if value:
            self.flags |= 0b1000000
        else:
            self.flags &= 0b0111111

    def check_flag_N(self) -> int:
            return (self.flags & 0b1000000)

    def reset(self, mem):
        self.PC = 0xFFFC
        self.SP = 0x0100
        self.set_flag_C(0)
        self.set_flag_Z(0)
        self.set_flag_I(0)
        self.set_flag_D(0)
        self.set_flag_B(0)
        self.set_flag_V(0)
        self.set_flag_N(0)
        self.A = self.X = self.Y = 0

        mem.initialize()



def main():
    mem = Mem()
    cpu = CPU()
    cpu.reset(mem)
