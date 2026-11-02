# Terminal Space Program (Asciiverse packaging)

jasonfen's orbital-mechanics rocket simulator in Go (Bubble Tea, braille
canvas); packaged for the Asciiverse catalog and as system packages. Not our
code: keep changes small, list every one in PATCHES.md, and offer fixes
upstream.

- Remotes: `upstream` is github.com/jasonfen/terminal-space-program,
  `origin` is github.com/theasciiverse/terminal-space-program.
- Branch `asciiverse` = an upstream release tag plus our commits. Upstream
  releases several times a day; to follow it, rebase `asciiverse` onto the
  newer `vX.Y.Z` tag and tag `vX.Y.Z-av.1`.
- Our `.github/workflows/release.yml` replaces upstream's goreleaser one (it
  publishes to upstream's tap, bucket and Cloudsmith); keep ours on rebase.
- Local static build: `docker run --rm -e CGO_ENABLED=0 -v "$PWD":/src -w /src
  golang:1.26-alpine go build -buildvcs=false -trimpath -ldflags "-s -w -X
  github.com/jasonfen/terminal-space-program/internal/version.Version=0.64.8"
  -o stage/terminal-space-program ./cmd/terminal-space-program`.
- Sizes: designed for 140x40, playable from 104x24 ("terminal too small"
  below). The preview records at 140x40 and the catalog crops it.
- In a pty that answers no terminal queries (asciinema driven by a script),
  the first frame takes about 10 s; keys sent before it are lost.
- Quit is Ctrl+C, then `n` (don't save) and `y`; `q` points the ship.
- Saves in `~/.local/state/terminal-space-program/`, mods in
  `~/.config/terminal-space-program/`. Multiplayer is ssh, hosted from the
  game (`--serve`, port 23234); the store page says local network.
