# Changelog

## [1.1.1] - 2026-10-28

### Fixed
- **Han 86 and M4 military levels now match the game**: Han 86 is 9, 17, 24, 33, 41, 49, 56, 64 and M4 is 9, 17, 25, 34, 43, 50, 58, 63, read off the in-game camo screen. The web guides behind 1.1.0 had both wrong, and not by a fixed amount, so their numbers can't be corrected with a formula.

### Changed
- **Unchecked levels are marked**: Military levels that haven't been read from the game yet show in grey italics, and the legend explains that some are wrong. Each gun's detail sheet says "checked in game" or "not checked in game" next to Military. Only Han 86 and M4 are checked so far.
- In `docs/camo-data.json`, each weapon now has a `verified` flag. Set it to true only for levels read from the game.

## [1.1.0] - 2026-10-28

### Fixed
- **Military camo levels are now per gun**: Each military cell shows the weapon level that camo unlocks at, and each gun has its own set. The old version used one level table for all guns. Values came from Game Rant and CODMunity. These later turned out to be unreliable (see 1.1.1).
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
