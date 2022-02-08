import time

forsen = "happy"
frozen = 0


def lul_e():
    while forsen == "happy":
        print(forsen)
        break


start = time.time()
while frozen < 11:
    print(frozen)
    frozen = frozen + 1
    if frozen == 11:
        break
end = time.time()

print(end - start)

lul_e()
