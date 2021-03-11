import os
import sys


def main(hcidev):
    last_bd_addr = None
    with open("last_bd_addr.txt", "rb") as f:
        last_bd_addr = f.read().strip()
        print("last_bd_addr: {}".format(last_bd_addr))
    assert len(last_bd_addr) == 12+5
    hex_val = int(last_bd_addr.replace(":",""),16)
    print("hex_val: 0x%x" % hex_val)
    this_bd_addr_val = hex_val + 1
    this_bd_addr_str_tmp = "%012X" % this_bd_addr_val
    this_bd_addr_str_parts = []
    for i in range(6):
        part = this_bd_addr_str_tmp[i*2:(i*2)+2]
        print("part:", part)
        this_bd_addr_str_parts.append(part)
    print("this_bd_addr_str_parts:", this_bd_addr_str_parts)
    this_bd_addr_str = ":".join(this_bd_addr_str_parts)
    print("this_bd_addr_str:", this_bd_addr_str)
    for cmd in [
            "btmgmt power on",
            "./bdaddr -i {} {}".format(hcidev, this_bd_addr_str)
    ]:
        print("exec cmd:", cmd)
        assert 0 == os.system(cmd)
    
    with open("last_bd_addr.txt", "wb") as f:
        f.write(this_bd_addr_str)
    print "=== SUCCESS ==="


if __name__ == "__main__":
    print("target hci dev: {}".format(sys.argv[1]))
    main(sys.argv[1])
