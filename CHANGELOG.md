# Changelog

## Unreleased

- Site: a light theme, so the page and the logo stand out, with the clock preview kept dark like a screen on a desk.
- Site: the four top buttons are matching pills, with Open the clock no longer picked out in red.
- Site: a terracotta and slate navy footer, and the headline accent now matches it.
- The social preview image says "Any browser" instead of "Android".

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
