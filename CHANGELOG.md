# Changelog

## Unreleased

- Site: a light theme, so the page and the logo stand out, with the clock preview kept dark like a screen on a desk.
- Site: the four top buttons are matching pills, with Open the clock no longer picked out in red.
- Site: a terracotta and slate navy footer, and the headline accent now matches it.
- The social preview image says "Any browser" instead of "Android".
- Clock: a bigger, chunkier board. Tiles grow with the screen (taller, like real flaps) and still shrink to fit ten cities.
- Clock: characters glow softly, like a backlit board, with a switch to turn it off.
- Clock: each row shows a sun or moon for day or night, and its time difference from home (+5H, −8H, +5:30).
- Clock: dates read "SUN 01 NOV" instead of "SUN 11/01", so they're the same in every country.
- Clock: colour pickers replace the accent themes: one for the characters and one for the accent, each with presets and any custom colour. Earlier theme choices carry over.
- Clock: sound previews in Preferences play even when the clock is muted.
- Clock: the settings panel is redesigned with brighter text, a single Done button and clearer controls. Tap a city in the list to add it, and tap it again to take it off the board.
- Clock: brighter row handles and remove buttons, and the seconds now turn over exactly on the second.
- Clock: Preferences is now called Settings, and the gear's tooltip says so.
- Clock: a Shortcuts tab in Settings lists the keys and the mouse and touch controls.
- Clock: a one-time hint on your first visit shows how to bring up the controls, flip the board and go full screen.
- Clock: sound previews play a single flap, so you hear exactly what each sound is like.
- Clock: all text uses two consistent, readable brightness levels, and the night-time dimming is gentler.
- Clock: every change is now a real two-half flap. The top half of the old character falls away and the bottom half of the new one drops into place.
- Clock: the sun, moon and time difference use the character colour, so they match the board whatever colour you pick.
- Clock: **F** sends one smooth wave across the board from left to right. Each tile counts up through the letters or digits just before its own and settles, and blank flaps stay still.

## 1.0.0 (2026-10-31)

First release as a web clock, with its own site.

- A split-flap departure board for up to ten of 290 cities, with the home city found from the device, drag to reorder, 12 or 24 hour time, seconds and dates.
- Flap animations, idle flips and a full-board cascade (**F**), three synthesised sound profiles with volume and mute, nine accent colours, film grain and a tint that warms through the evening.
- New: a full screen button and **Shift + F**, and the screen stays awake while the clock is showing.
- Fits every screen: tiles and text shrink to fit short screens and ten-row boards, which used to run off the bottom. Preferences keeps one height across its tabs and scrolls when space is tight.
- A tap shows the controls on touch screens, and the keyboard no longer pops up over the city list.
- Sound waits for your first click, tap or key press instead of filling the console with blocked-audio warnings.
- Removed the unused service worker, install, update and offline banners. The clock never needs the network, and there was no service worker to install.
- Renamed from "Terminal Time" to Split-Flap World Clock, with a new tab icon and a "Created by Shaz Moghaddam, London" credit in Preferences. Saved settings carry over.
- Reduced motion turns off the intro fade and the grain.
- A GitHub Pages site with a live preview, deployed from `main`, and a script to preview it locally.
- README with screenshots, a social preview image, contributing guide, security policy and Dependabot for the workflows.
