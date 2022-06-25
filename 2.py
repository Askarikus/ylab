def int32_to_ip(int32):
    ret_string = ""
    for i in range(3, -1, -1):
        ret_string += str(int32 >> (i * 8)) + '.'
        int32 = int32 % 2 ** (i * 8)
    return ret_string.rstrip('.')


if __name__ == '__main__':
    int32_to_ip(2149583361)
    int32_to_ip(2154959208)
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"
