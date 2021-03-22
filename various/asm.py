class ASM:
    def __init__(self, program):
        self.program = program
        self.__ip = 0
        self.__registry = {}