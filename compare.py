from original import zahl as zahl1
from zahl import zahl as zahl2
from random import randint

def diff(a, b):
  m = max(map(len, [a, b]))
  a = a + "_" * (m - len(a))
  b = b + "_" * (m - len(b))
  for i in range(m):
    if a[i] != b[i]:
      print("Should be:", "." + a[:i] + "!" + a[i:i + 10] + ".", "Was:", "." + b[:i] + "!" + b[i:i + 10] + ".", sep = "\n\n")
      return False

rand = 1000
fix = 1000

print(
  all(
    (
      ((i := randint(- 10**1000, 10**1000)) or 1)
      and
      (
        zahl1(i) == zahl2(i)
        or
        diff(zahl1(i), zahl2(i))
      )
    ) if j > 2 * fix else (
      zahl1(j - fix) == zahl2(j - fix)
      or
      diff(zahl1(j - fix), zahl2(j - fix))
    )
    for j in range(2 * fix + rand)
  )
)
