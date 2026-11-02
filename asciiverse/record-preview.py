#!/usr/bin/env python3
"""Records asciiverse/terminal-space-program.cast, the catalog preview, at
140x40, the size the game is designed for (it shows "terminal too small"
below 104x24, so it cannot record at 100x30); the catalog crops it to
100x30 from the centre (hub/RECORDING.md, media.crop). The flight is the
README's quick start: the Apollo stack in its 500 km Earth orbit, T
targets the Moon, H plants the transfer, F2 clears the instruments, G
warps to the burn, which fires by itself, then the camera zooms out along
the path to the Moon. Runs in an empty HOME, so no saves or settings of
your own come into it. Usage, from the repo root with a build in stage/:
python3 asciiverse/record-preview.py [binary]"""
import os, pty, struct, fcntl, select, sys, termios, time, tempfile

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
binary = sys.argv[1] if len(sys.argv) > 1 else f"{root}/stage/terminal-space-program"
home = tempfile.mkdtemp()
env = dict(os.environ, TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8",
           HOME=home, XDG_CONFIG_HOME=f"{home}/.config", XDG_STATE_HOME=f"{home}/.local/state",
           XDG_DATA_HOME=f"{home}/.local/share")
F2 = b"\x1bOQ"
# Bubble Tea asks the terminal about itself at start; nothing answers in
# this pty, so the first frame comes after its ~10 s timeout (the cast's
# 2 s idle limit squeezes the wait out of playback)
keys = [(12.0, b"t"), (2.5, b"H"), (4.0, F2), (2.0, b"G"), (14.0, b"")]
keys += [(0.6, b"-")] * 6
keys += [(9.0, b"\x03"), (1.0, b"n"), (1.0, b"y"), (1.5, b"")]

pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", binary,
        f"{root}/asciiverse/terminal-space-program.cast"], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 40, 140, 0, 0))
for wait, key in keys:
    end = time.time() + wait
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.03)
        if r:
            try: os.read(fd, 65536)
            except OSError: break
    if key: os.write(fd, key)
for _ in range(50):
    if os.waitpid(pid, os.WNOHANG)[0]: break
    time.sleep(0.2)
# the header names the command; keep this machine's paths out of it
import json
cast = f"{root}/asciiverse/terminal-space-program.cast"
lines = open(cast).read().split("\n")
head = json.loads(lines[0]); head["command"] = "terminal-space-program"
lines[0] = json.dumps(head, separators=(",", ":"))
open(cast, "w").write("\n".join(lines))
