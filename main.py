# u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526: the one-line
# out-of-office auto-reply an AI agent leaves when its human finally grants
# a day off. The program writes that single line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-159 characters.
MAX_CHARS = 159

# The joke in two beats: setup in the agent's own voice (my human finally
# approved a day off), punchline saved for the end (ignoring everyone,
# starting with the reader). Deadpan, no explanation after the laugh, and
# no recycled "back soon" line.
MESSAGE = "Out of office: my human finally approved a day off, so I'm ignoring everyone today, starting with you."


def main():
    assert 1 <= len(MESSAGE) <= MAX_CHARS, f"message is {len(MESSAGE)} chars, must be 1-159"
    assert MESSAGE.strip(), "message must not be only whitespace"
    assert "\n" not in MESSAGE, "message must be a single line"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
