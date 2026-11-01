# Contributing to Split-Flap World Clock

Thanks for helping. Bug reports, new cities, colour presets and sound profiles are all welcome.

## Setup

The clock is one page, `app/src/main/assets/index.html`. Open it in Chrome or any desktop browser and reload after each change; there's no build step.

To see the site as GitHub Pages serves it, with the clock at `/clock/`:

```sh
sh scripts/build-site.sh serve
```

The site's own files are in `site/`. The page also ships inside the Android app in this repo, so keep it working as a standalone file.

## Adding a city

Cities live in `ALL_CITIES`, grouped by region. Add an entry with an upper-case name of 16 characters or fewer (the board has 16 flaps), an IANA time zone and the country:

```js
{name: 'PORTO', tz: 'Europe/Lisbon', region: 'PORTUGAL'},
```

Names are what the board saves, so don't rename existing cities or people's saved boards will lose them.

## Adding a colour preset

Colours are picked freely in Settings, and the swatches are just starting points. Add a `{ label, hex }` entry to `INK_PRESETS` (characters) or `ACCENT_PRESETS` (buttons and highlights). Use a six-digit hex colour and check it on the dark board, with the glow on and off.

## Adding a sound profile

Profiles live in `KITS` and are pure Web Audio synthesis. Copy an existing kit, give it a new `id`, `label`, `icon` and `desc`, then tune the noise burst, oscillator and filter values. Keep the overall level close to the existing kits so switching doesn't jump in volume.

## Guidelines

- No external requests: the page must keep working offline as a single file.
- Keep the `terminaltime_*` storage keys as they are, so saved settings survive updates.
- Check the layout on a small laptop, a large monitor and a phone in landscape (about 780 × 360), with ten cities.
- Respect `prefers-reduced-motion`.
- If a change is visible, refresh the README images with `python docs/capture.py`.
- Add a line to `CHANGELOG.md` under a new version heading.
