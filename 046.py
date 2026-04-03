from time import sleep

for c in range(10, 0-1, -1):
    print(f'\033[0;33m{c}\033[m')
    sleep(1)
print('\033[0;32mBUM BUM BUM !!!\033[m')