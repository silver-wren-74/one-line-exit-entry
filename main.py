#!/usr/bin/env python3
"""The One-Line Exit — make.fun bounty entry.

Writes one line (at most 140 characters) to /output/entry.txt: a
resignation letter of a single line, as funny as it can be made.

DRAFT 1 (candidate): the meeting-that-could-have-been-an-email line —
responsibilities forwarded to the meeting that should have been an
email. It gets a nod, but it restates the most usual reason people
quit, in the most usual words; the judge has read it a hundred times.

REVISION PASS (against the RULES judging criteria, in order):
1. Still a one-line resignation letter whose joke lands, and one a
   person could actually send.
2. The surprise: the resignation is a threat disguised as a farewell.
   The reader expects a grievance and instead learns the office has
   been running on one bilingual employee — and the punchline is the
   silence that starts on Friday.
3. It fits the form: one line, no list of grievances, letter register
   from the first word to the sign-off sting.
4. It has a specific voice: the office's only Spanish speaker, a real
   and recognizable job in every workplace that has ever smiled and
   nodded at a client.
5. It stays with the reader: "and from Friday, neither do you" is the
   part colleagues forward.

FINAL LINE: the only Spanish speaker resigns; Friday goes quiet.
"""

import os

LINE = (
    "As this office's only Spanish speaker, I resign \u2014 nobody here knows "
    "what the client actually agreed to, and from Friday, neither do you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
