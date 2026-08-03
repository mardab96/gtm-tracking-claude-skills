# Changelog

All notable changes to this pack are documented here. Format follows Keep a
Changelog, loosely.

## [1.1.0] - 2026-08-03

### Fixed
- Install command now creates `~/.claude/skills` before copying, so it works on
  a machine where Claude Code has not created the folder yet. The previous
  `cp -r repo/* ~/.claude/skills/` failed with "Not a directory" on a fresh
  setup.
- Install command copies only skill folders plus `references/`, instead of
  dumping the repo's README and internal folders into the skills root.

### Added
- MIT `LICENSE` (the pack was described as open source; now it formally is).
- `AGENTS.md` with durable guidance on how the pack behaves and composes.
- This changelog.

## [1.0.0] - 2026-06-17

### Added
- Initial public release: 15 diagnostic skills for GTM, GA4, Google Ads
  conversions, Meta Pixel + CAPI, Consent Mode and deduplication, with shared
  `references/`, worked `examples/` and a validator script.
