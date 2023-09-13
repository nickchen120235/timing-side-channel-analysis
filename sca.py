from pwn import *
import string
import sys

valid_input = string.printable[:-6]
context.log_level = 'error'

def sca(file: str, password: str) -> int:
    log.debug(f'password: {password}')
    valgrind = process(['valgrind', '--tool=cachegrind', '--cachegrind-out-file=/dev/null', f'./{file}', password])
    valgrind.recvuntil(b'I   refs:')
    valgrind.close()
    return int(valgrind.recvline().decode('ascii').strip(' \n').replace(',', ''))

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <correct|wrong>')
    sys.exit(1)

if sys.argv[1] not in ['correct', 'wrong']:
    print(f'Usage: {sys.argv[0]} <correct|wrong>')
    sys.exit(1)

secret_len = len('5ecR3t_s7r1n9')
secret = ['~'] * secret_len
iref_best = 0
for i in range(len(secret)):
    print(f'Guessing position {i}')
    current_character = ''
    for c in valid_input:
        secret[i] = c
        guess = ''.join(secret)
        iref = sca(sys.argv[1], guess)
        # print(f'Guess {c}: {iref}')
        if iref_best == 0:
            iref_best = iref
            continue
        if iref > iref_best:
            iref_best = iref
            current_character = c
            break
    print(f'Best guess: {current_character}')

print(f'secret: {"".join(secret)}')
