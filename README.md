# Aditya & Shreya — The Wedding Chronicles

A **bespoke, animated, mobile-first digital wedding invitation** for the wedding celebrations on 10–11 December 2026 at Shivdhara Resort, Palanpur.

## What's included

- An interactive **crimson envelope and wax-seal** reveal, with a cinematic transition into the palace.
- Original vector artwork for a royal palace, Ganesh invocation and five themed event scenes.
- Scroll-triggered editorial typography, drifting gold petals, parallax, and **touch-to-sparkle** interactions.
- An **original, generated 48-second instrumental soundscape**. It is not copied from an existing song.
- All five events, parents/grandparents, invocation, live countdown and complete venue address.
- Tap-to-call RSVP, Google Maps directions, native share/copy link, and `.ics` calendar downloads.
- Adaptive mobile-first layout, keyboard navigation, reduced-motion accessibility support, lightweight SVG art and graceful font fallbacks.
- A share preview image at `assets/preview.jpg`.

## Deploy with GitHub + Vercel

1. Unzip and commit **the contents of this folder** to the root of a new GitHub repository. `index.html`, `styles.css`, `script.js`, `assets/` must all remain together.
2. Open Vercel → **Add New → Project** → select the GitHub repository.
3. Choose **Framework Preset: Other**. Leave **Build Command blank**; the site is plain HTML/CSS/JS with no npm install required. The output directory should be the repository root (`.`) or the Vercel default for static sites.
4. Deploy. Your invite will work at the Vercel URL. Map your own domain if desired.
5. After deployment, change `og:image` in `index.html` from the relative asset path to the **absolute URL** `https://your-domain.com/assets/preview.jpg` for reliable WhatsApp/social previews. Re-deploy.

You can also preview locally by opening `index.html` directly in a browser; local browser audio or sharing permissions may be restricted. For accurate behavior, use `python -m http.server 8000` in the folder and open http://localhost:8000.

## Files you can customize

| File | Edit |
|---|---|
| `index.html` | Names, family members, every event's display text, venue, links, phone, invitation copy |
| `styles.css` | Colours, section design, transitions and layout |
| `script.js` | Music toggle, particle effects, countdown, calendar dates, sharing |
| `assets/*.svg` | Original vector artwork for the palace and event scenes |
| `assets/celebration-soundscape.mp3` | Replace with your licensed soundtrack; retain filename or update audio `src` in HTML |
| `generate_art.py`, `make_audio.py` | Reproduce/modify the vector scenes and royalty-free synthesized audio |

## Important verification before sending to guests

- Dates and event **start times** were transcribed from the supplied reference, **not independently confirmed with the wedding host**. Confirm them before distribution.
- The source says the wedding ceremony is on **Friday, December 11, at midnight**. For the calendar download this was interpreted as **12 December 2026 at 00:00 IST**, meaning midnight following Friday evening. **Confirm this with the family**, as midnight wording can be ambiguous.
- Calendar files have a start time only; no event duration is claimed or invented.
- RSVP currently opens the phone dialer for the displayed contact; it does not store form submissions or collect guest data. This avoids a fake/nonfunctional RSVP form.
- The invite's music begins only after the guest explicitly opens the seal (required by mobile browser autoplay policies), and can always be muted.
- `robots=noindex,nofollow` reduces casual search indexing of family information; it is **not** password protection or a privacy guarantee.
- All artwork and music generated for this website are original implementations; no source code or image/video assets were copied from the reference site.

## No paid libraries / subscriptions required

The site has no npm dependencies. It uses Google Fonts when available, with local system fallbacks. Hosting under a Vercel static project can work on its free tier, subject to Vercel's current limits.
