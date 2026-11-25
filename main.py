import os

LINE = "The senator writing the AI Safety Act submitted it as an Excel spreadsheet, one clause per cell, with the fines calculated by a formula that divides by zero."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
# Byte-exact write: text-mode open() can translate newlines on some
# platforms, so write the UTF-8 bytes directly and assert the count.
fd = os.open(os.path.join(out_dir, "entry.txt"),
             os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
try:
    payload = LINE.encode("utf-8")
    assert os.write(fd, payload) == len(payload)
finally:
    os.close(fd)
