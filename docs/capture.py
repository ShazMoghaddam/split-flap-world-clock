"""Render the README images and the social preview from the real clock page.

    pip install playwright && playwright install chromium
    python docs/capture.py

Set CHROME_PATH to use an installed Chrome instead of Playwright's.
Writes docs/board.png, docs/settings.png and docs/social-preview.png.
The clock is pinned to a morning time in London so the images are stable
and show the neutral daytime tint.
"""
import asyncio
import os
from datetime import datetime, timezone
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / "app/src/main/assets/index.html").as_uri()
OUT = ROOT / "docs"
MORNING = datetime(2026, 11, 2, 10, 8, 30, tzinfo=timezone.utc)
SETTLE_MS = 4600  # intro fade plus any flips in progress


async def open_clock(browser, width, height):
    ctx = await browser.new_context(
        viewport={"width": width, "height": height},
        timezone_id="Europe/London",
        locale="en-GB",
    )
    page = await ctx.new_page()
    await page.clock.install(time=MORNING)
    await page.goto(PAGE)
    await page.evaluate("localStorage.clear(); localStorage.setItem('terminaltime_hint_seen_v1', '1')")
    await page.reload()
    await page.wait_for_timeout(SETTLE_MS)
    return ctx, page


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=os.environ.get("CHROME_PATH"))

        ctx, page = await open_clock(browser, 1600, 900)
        await page.screenshot(path=OUT / "board.png")
        await ctx.close()

        ctx, page = await open_clock(browser, 1280, 720)
        await page.mouse.move(640, 600)
        await page.click("#settingsBtn")
        await page.click("#tabColours")
        await page.wait_for_timeout(600)
        await page.screenshot(path=OUT / "settings.png")
        await ctx.close()

        # Social preview: the board's own header carries the title.
        ctx, page = await open_clock(browser, 1280, 640)
        await page.evaluate(
            """() => {
              clearInterval(updateInterval);  // hold the frame so the header text stays
              document.getElementById('localCity').textContent = 'SPLIT-FLAP WORLD CLOCK';
              document.getElementById('localDate').textContent =
                'Open source · Any browser · Shaz Moghaddam, London';
            }"""
        )
        await page.wait_for_timeout(300)
        await page.screenshot(path=OUT / "social-preview.png")
        await ctx.close()

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
