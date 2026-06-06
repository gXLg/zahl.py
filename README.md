# zahl.py
Python script to write out numbers in German

The script was written to be as short
as possible, while keeping the ability
to write any possible integer as a word
in German langauge

For reference on the naming system
check out the German Wikipedia page
[Zahlennamen](https://de.m.wikipedia.org/wiki/Zahlennamen)

The script was developed on Discord
with the help of these amazing people:
* @blueberrypi (my coc server and DMs)
* @krowten024nabru (official python server)

Current status (ignoring the trailing newline):

| Bytes | Chars |
|-------|-------|
|   994 |   991 |

# Contents

* `zahl.py` - the golfed script
* `original.py` - the original script which
  is more readable
* `compare.py` - compares the outputs of both
  scripts on 2000 fixed and 1000 random samples

# Usage
in your python script:
```py
from zahl import zahl

s = zahl(1234) # -> 'Eintausendzweihundertvierunddreißig'
```

# History

* The idea for this program was created
  around September 2022 in the "World of
  Coding" Discord server during a
  conversation about German language
* Around the same time private Clash of Code
  events have been popular on the server and
  blueberrypi and I who were battling
  equally for the top of the leaderboard
  came up with the idea of creating an
  own code golf challenge
* The initial program has been written
  around a week later and was `2661 bytes`
* Original goal was to be able to send the
  code as a single Discord message
* First big clean-up happened in
  October 2022 and the program was brought down
  to `1656 bytes`
* Since it went down so quicky, our next goal
  was to bring it under 1k
* At the end of December 2022: `1337 bytes`
* After creating my own CoC server,
  the golfing discussion went on there
  with various tips from different
  community members
* We hit the hard bottom in May 2023 at around
  `1050 bytes`. I joined the official Python
  community and inquired some help, but only
  one guy, krowten024nabru, could help
  and brought the code down by 1 byte
* August 24th 2023 final 5 bytes have been
  shaved off and the code size is `999 bytes`.
  With that our goal was achieved and we
  finished working on it any further
* In June 2024 I came back to the project
  and was able to cut down 5 more bytes to
  the current `994 bytes`

# Original Constrains
* We only cared about character count during our golfing,
  so the amount of bytes was mostly ignored;
  but given that the final code only has three umlauts (`üöß`)
  and each is only used once, the amount of bytes
  is also at the current lowest
* The code must provide the `zahl(int) -> str` function,
  but it was not fobidden to use any following `**kwargs`;
  without that constraint the size could be reduced even more,
  replacing `zahl` with a single-letter function name
* No imports, but that wouldn't have been a huge boost anyways
  and would grow way more size that it would reduce it

# Open Goals
* Get rid of inner loops by maybe using
  generators or potentially eval
* Especially the `while V` loop, which could
  shove off a few bytes by removing whitespace
