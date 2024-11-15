from pwn import * 

p = remote('109.233.56.90', 11573)

while True:
    str_with_number = p.recvline()
    print(str_with_number)
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    str = p.recvline().decode("utf-8")


    if (str == "|_| |_| \\___|/_/\\_\\\r\n"):  
        res = str_with_number.decode("utf-8").split(" ")
        hex_str = hex(int(res[1]))[2:]
        payload = bytes(hex_str , 'utf-8')
        p.sendline(payload)
        print(p.recvline())
        print(p.recvline())

    elif str == " \\___/  \\___| \\__| \\__,_||_|\r\n":  
        res = str_with_number.decode("utf-8").split(" ")
        oct_str = oct(int(res[1]))[2:]
        payload = bytes(oct_str , 'utf-8')
        p.sendline(payload)
        print(p.recvline())
        print(p.recvline())

    elif str == "|____/ |_| \\__, | |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n": 
        res = str_with_number.decode("utf-8").split(" ")
        num = int(res[1])
        p.sendline(p64(num, endian='big'))
        print(p.recvline())
        print(p.recvline())


    elif str == "|_____||_| \\__| \\__||_| \\___| |_____||_| |_| \\__,_||_| \\__,_||_| |_| \\___/    |_|  \r\n": 
        res = str_with_number.decode("utf-8").split(" ")
        num = int(res[1])
        p.sendline(p64(num))
        print(p.recvline())
        print(p.recvline())









