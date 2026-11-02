# Changes from upstream

This is the Asciiverse packaging of [Terminal Space Program](https://github.com/jasonfen/terminal-space-program)
by jasonfen (MIT), built from upstream's tag `v0.64.8` (`aa3b608`, 2 November
2026). Upstream is the `upstream` remote; the `asciiverse` branch carries the
changes below. The game itself is unchanged.

## Packaging

- `.github/workflows/release.yml` **replaces upstream's workflow of the same
  name.** Upstream's runs goreleaser and publishes to upstream's own Homebrew
  tap, Scoop bucket and Cloudsmith repository; it must not run here. Ours
  builds av archives for Linux (static), macOS (x86-64 and ARM64) and Windows
  (x86-64; upstream builds no Windows ARM64 either), plus SHA256SUMS, and
  .deb, .rpm, .apk and Arch packages. The binary reports upstream's version
  (`0.64.8`), as upstream's own builds do, so the multiplayer server's
  release readout compares like with like.
- `asciiverse/nfpm.yaml`: the system packages.
- `asciiverse/record-preview.py`: records the catalog preview at 140x40 (the
  quick start: target the Moon, plant the transfer, warp to the burn, zoom out).

## Ours

- **How to play it, at the top of README.md.** A short note on installing
  and starting it with av; the original text follows unchanged.
