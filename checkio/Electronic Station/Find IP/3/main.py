import re

def checkio(text):
    """
        find all IPs
    """
    def is_valid_ip(token):
        m = re.match(r'^\d+[.]\d+[.]\d+[.]\d+$', token)
        if m is not None:
            ip = [x for x in token.split('.') if int(x) <= 255]
            if len(ip) != 4:
                return False
            else:
                for b in ip:
                    x = int(b)
                    if x != 0 and b.startswith('0'):
                        return False
                return '.'.join(str(x) for x in ip)
        else:
            return False
        
    tokens = text.split()
    ans = []
    for token in tokens:
        token = token.strip()
        ip = is_valid_ip(token)
        if ip:
            ans.append(ip)
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("192.168.1.1 and 10.0.0.1 or 127.0.0.1") == \
        ["192.168.1.1", "10.0.0.1", "127.0.0.1"], "All correct"
    assert checkio("10.0.0.1.1 but 127.0.0.256 1.1.1.1") == \
        ["1.1.1.1"], "Only 1.1.1.1"
    assert checkio("167.11.0.0 1.2.3.255 192,168,1,1") == \
        ["167.11.0.0", "1.2.3.255"], "0 and 255"
    assert checkio("267.11.0.0 1.2.3.4/16 192:168:1:1") == \
        [], "I don't see IP"
    assert checkio("00250.00001.0000002.1 251.1.2.1") == \
        ["251.1.2.1"], "Be careful with zeros"

