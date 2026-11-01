# Changelog

## 1.0.0 (2026-11-01)

First release as a web clock, with its own site.

### The board
- A split-flap departure board for up to ten of 290 cities. Your home city comes from your device's time zone and stays on top, and you can drag the others into any order. It shows 12 or 24 hour time, seconds and dates.
- Real two-half flaps: the old character's top half falls away and the new bottom half drops into place. This applies to the clock ticking, the idle flips and the cascade.
- **F** sends one smooth wave from left to right. Each tile counts up through the letters or digits just before its own and settles, and blank flaps stay still.
- Each row shows a sun or moon for day or night, and its time difference from home ("+5H", "−8H", "+5:30"), in the character colour.
- Dates read "MON 02 NOV", the same in every country.
- A soft backlit glow on the characters, which you can turn off.
- The board grows with the screen, with tiles a little taller than wide like real flaps, and still shrinks so ten cities fit on short screens.
- A full screen button and **Shift + F**, and the screen stays awake while the clock is showing.
- The seconds turn over exactly on the second.
- A tint that warms to amber through the evening, with gentle dimming, film grain and three synthesised flap sounds with volume and mute.

### Settings
- Four tabs: Cities, Colours, Sound and Shortcuts, with readable text, a rounded panel and one Done button.
- Tap a city to add it, and tap it again to remove it. Your search stays put after either.
- Colour pickers for the characters and the accent, each with presets and any custom colour, plus Reset. Accent themes chosen in earlier versions carry over.
- Sound previews play a single flap, even when the board is muted.
- A one-time hint on the first visit shows the controls and shortcuts. The site's preview doesn't use it up.
- A "Created by Shaz Moghaddam, London" credit that links to his website.

### Under the hood
- Renamed from "Terminal Time" to Split-Flap World Clock, with a new tab icon. Saved settings carry over.
- Removed the unused service worker and the install, update and offline banners. The clock never needs the network.
- Sound waits for your first click, tap or key press, so the browser doesn't log blocked-audio warnings.
- Touch friendly: a tap shows the controls, and the keyboard doesn't pop up over the city list.
- Reduced motion turns off the intro fade, the grain and the flap animation.

### Site and repo
- A GitHub Pages site with a live preview of the clock: a light theme with pill buttons and a terracotta and slate navy footer, deployed from `main`, plus a script to preview it locally.
- README with screenshots, a social preview image, a contributing guide, a security policy and Dependabot for the workflows.
