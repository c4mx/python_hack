#!/usr/bin/python


def hex_to_character(memory):
    """
    @description: convert memory value in little endian system to character 
    @parameter: momery a string represent a memory zone in lettle endian system
    """
    mem_units = []
    for i in range(0, len(memory), 8):
        mem_units.append(memory[i:i+8])
    
    res = ""
    for unit in mem_units:
        tmp = []
        for i in range(0, len(unit), 2):
            tmp.append(unit[i:i+2])
        res += "".join(reversed(tmp))
    return res.decode("hex")


print hex_to_character("000000200804b008b7fcfff40804857008049ff400000002bffffb94b7fd03e40000000d0804b00839617044282936646d617045b7000a64b7e5de55b7fed28000000000080485795204550008048570")