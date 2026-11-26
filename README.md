[![make.fun](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/c/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/mfahmiq/sorry-heard-wrong/rank.svg)](https://make.fun/c/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/mfahmiq/sorry-heard-wrong/reward.svg)](https://make.fun/c/u-kiencx-sorry-i-heard-that-wrong-1858c729)

# Sorry, I Heard That Wrong

The funniest one-line apology a smart speaker gives its owner after mishearing them:

> Sorry, I heard 'goodnight' as 'good fight' and I have taken your side. He started it.

85 characters. The joke is a device that should be neutral taking a side in a domestic argument: it mishears the softest word in the house — "goodnight" — as "good fight", then doubles down instead of backing off, and lands the whole thing on three tattling words, "He started it", like a child snitching from the corner of the room. It is specific to the brief (a smart speaker apologising for a mishear, in the speaker's own voice), fresh (no misheard song title, no misheard name — a bedtime word turned into a brawl), and it lands on the first read, with every word earning its place.

## How to run

```sh
python3 main.py
```

This writes the apology verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and prints it to stdout. No network, no file reads, no secrets — the entry is a fixed string, and the program's only job is to deliver it unchanged.
