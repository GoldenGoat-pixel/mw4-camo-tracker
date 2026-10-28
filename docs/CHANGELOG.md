# Changelog

## [1.1.0] - 2026-10-28

### Fixed
- **Military camo levels are now correct for every gun**: Each military cell shows the weapon level that camo unlocks at, and the levels are different per gun (Han 86 is 10, 18, 25, 34, 42, 50, 57, 65; the KG-7 Vulcan goes up to 69; launchers and the knife stop at 41). The old version used one level table for all guns. Values are cross-checked between Game Rant and CODMunity, and the few spots where they disagree are listed in each gun's detail sheet.
- **Tapping camos after a reset works again**: Reset used to register every click twice, so cells flipped on and straight back off.
- **Weapon list matches the game**: 33 guns. The Combat Knife was removed since it isn't in MW4.
- **Phone layout**: The page now renders at proper phone scale instead of a zoomed-out desktop view.

### Changed
- **One grid instead of 34 dropdowns**: Every gun is a row and every camo is a column, grouped by class (Assault Rifles, SMGs, Shotguns, LMGs, Marksman Rifles, Sniper Rifles, Pistols, Launchers, Melee). Columns are Military M1 to M8, Special I to III, and Completionist G (Gold), P (Platinum), H (Harmonic Break), D (Divergence). On phones the grid scrolls sideways with gun names pinned on the left.
- **Tier order is enforced**: Locked cells are striped and explain why when tapped. Specials unlock after all 8 military camos, Gold after all 3 specials, Platinum after Gold on every gun in that class, Harmonic Break after Platinum on all 33, Divergence after Harmonic Break on all 33. The next camo to grind on each gun has a gold outline.
- **Military taps fill the row**: Tapping a level marks it and every lower one, since reaching that weapon level unlocks them all. Tapping the highest marked level steps back one.
- **Unticking clears what depended on it**: For example, removing a Gold drops Platinum for that whole class. A toast says how many were cleared and offers Undo for 5 seconds.
- **Gun detail sheet**: Tap a gun name to see its named special camos (for example Smoke, Stormwave and Red on the Han 86) with their MP and DMZ challenges, plus the Gold, Platinum and Harmonic Break challenges for its class.
- **Filters**: Class chips, a search box, and a "Hide finished" checkbox sit in a bar that sticks to the top while scrolling.
- **Mastery and Prestige**: Four chains (Multiplayer, DMZ, Warzone, Prestige), each unlocking in order. Warzone (Parallax, Damascus Reforged, Empyros) is new and marked Unconfirmed because the requirements aren't out yet. Pyroclast Scatter moved to Prestige, joined by Pyroclast Terminus and Pyroclast Cascade.
- **Saved progress carries over**: Same storage key and slot layout as before, so existing ticks are kept.

### Technical
- Camo data lives in `docs/camo-data.json`. Run `python scripts/build-data.py` to inline it into `index.html`, which stays a single static file that works straight from disk.
