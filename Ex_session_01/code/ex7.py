#ex 7 parity

ODD_PARITY = 1
EVEN_PARITY = 0

parity = EVEN_PARITY #let's assume even

n = int(raw_input())
numberOf1s = 0

while n>0:
    remainder = n % 2
    if remainder == 1:
        numberOf1s+=1
    n = n /2

parityBit = (numberOf1s + parity) % 2
print(parityBit)
