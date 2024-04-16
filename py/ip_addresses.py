import test


def ips_between(start, end):
    s = start.split('.')
    e = end.split('.')

    ip_int = lambda x: int(x[0])*256**3 + int(x[1])*256**2 + int(x[2])*256 + int(x[3])
    return ip_int(e) - ip_int(s)


assert ips_between("10.0.0.0", "10.0.0.50") == 50
assert ips_between("20.0.0.10", "20.0.1.0") == 246
assert ips_between("171.240.238.54", "173.137.43.121") == 26754371