digs = [
  "null", "eins", "zwei",
  "drei", "vier", "fünf",
  "sechs", "sieben",
  "acht", "neun"
]
ttn = [
  "zehn", "elf", "zwölf",
  "dreizehn", "vierzehn",
  "fünfzehn", "sechzehn",
  "siebzehn", "achtzehn",
  "neunzehn"
]
tens = [
  "zwanzig", "dreißig", "vierzig",
  "fünfzig", "sechzig", "siebzig",
  "achtzig", "neunzig"
]
def zahl(n, r = False):

  g = ""
  n = int(n)
  if n < 0:
    g = "minus "
    n = - n

  s = ""
  if n < 10:
    return "ein" if r and n == 1 else (
      digs[n] if r else (g + digs[n]).capitalize()
    )

  a = n % 1_000
  b = a % 100
  if b == 0:
    pass
  elif b < 10:
    s += digs[b]
  elif b < 20:
    s += ttn[b - 10]
  else:
    c = b % 10
    if c == 1:
      s += "einund"
    elif c:
      s += digs[c] + "und"
    s += tens[b // 10 - 2]
  d = a // 100
  if d == 1:  s = "einhundert" + s
  elif d: s = digs[d] + "hundert" + s

  t = (n // 1_000) % 1_000
  if t: s = zahl(t, True) + "tausend" + s

  m = n // 1_000_000
  z = 6
  while m:
    p = m % 1_000
    if p > 1: s = zahl(p, True) + " " + nulls(z, True) + " " + s
    elif p: s = "eine " + nulls(z) + " " + s
    m = m // 1_000
    z += 3
  s = (g + s).strip()
  return s if r else s[0].upper() + s[1 :]
one = [
  "mi", "bi", "tri", "quadri",
  "quinti", "sexti", "septi",
  "okti", "noni"
]
onee = [
  ["un", ""], ["duo", ""], ["tre", "s"],
  ["quattuor", ""], ["quin", ""], ["se", "x"],
  ["septe", "mn"], ["okto", ""], ["nove", "mn"]
]
tenn = [
 ["n", "dezi"], ["ms", "viginti"], ["ns", "triginta"],
 ["ns", "quadraginta"], ["ns", "quinquaginta"],
 ["n", "sexaginta"], ["n", "septuaginta"],
 ["mx", "oktoginta"], ["", "nonaginta"]
]
hunn = [
  ["nxs", "zenti"], ["n", "duzenti"],
  ["ns", "trezenti"], ["ns", "quadringenti"],
  ["ns", "quingenti"], ["n", "seszenti"],
  ["n", "septingenti"], ["mx", "oktingenti"],
  ["", "nongenti"]
]
def nulls(z, m = False):
  s = ""
  a = z // 6
  b = z % 6
  if b:
    s += "arde"
    if m: s += "n"
  else:
    s += "on"
    if m: s += "en"
  c = ""
  while a:
    d = a % 1_000
    c = name(d) + "lli" + c
    a //= 1_000
  return c.capitalize() + s

def name(a):
  if a == 0: return "ni"
  if a < 10: return one[a - 1]
  c = (a // 10) % 10
  d = a % 10
  e = a // 100
  if c:
    if e:
      return (combine(onee[d - 1], tenn[c - 1]) + hunn[e - 1][1] if d else
        tenn[c - 1][1] + hunn[e - 1][1])
    else:
      return (combine(onee[d - 1], tenn[c - 1])[: - 1] + "i" if d else
        tenn[c - 1][1][: - 1] + "i")
  else:
    return combine(onee[d - 1], hunn[e - 1]) if d else hunn[e - 1][1]
def combine(a, b):
  s = ""
  for i in a[1]:
    if i in b[0]:
      s += i
      break
  return a[0] + s + b[1]
