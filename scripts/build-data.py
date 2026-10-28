"""Inline docs/camo-data.json into index.html between the DATA markers.

The page stays a single static file with no fetch, so it also works when
opened straight from disk. Run after editing the JSON:  python scripts/build-data.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Save-file ids from v1. Changing one orphans that gun's saved progress.
IDS = {
    "Han 86": "han86", "M4": "m4", "Hyeon Burst": "hyeon_burst", "Kastov 762": "kastov762",
    "Patriot XMR": "patriot_xmr", "Axion": "axion", "Oden": "oden", "Cronen Squall": "cronen_squall",
    "ISO Nightshade": "iso_nightshade", "PPSh-41": "ppsh41", "X-58 Nyx": "x58_nyx",
    "Wz.55 Striga": "wz55_striga", "VEL 46": "vel46", "Rezi 12": "rezi12", "Warlord": "warlord",
    "APOC-338": "apoc338", "FiNN LMG": "finn_lmg", "Type 73": "type73", "MAR-9": "mar9",
    "Mosin-Nagant": "mosin_nagant", "Oris 8.6": "oris86", "Astaroth .57": "astaroth57",
    "KG-7 Vulcan": "kg7_vulcan", "Signal 50": "signal50", ".50 GS": "gs50", "Krait P68": "krait_p68",
    "Mojave .357": "mojave357", "SANG 9mm": "sang9mm", "JOKR": "jokr", "PILA": "pila",
    "PM-40 Anvil": "pm40_anvil", "RPG-8": "rpg8", "FSS Carbon Edge 1095": "fss_carbon",
}
CLASS_IDS = {"ar", "smg", "shotgun", "lmg", "marksman", "sniper", "pistol", "launcher", "melee"}


def challenge(c):
    if not isinstance(c, dict):
        return None
    out = {k: c.get(k) for k in ("mp", "dmz") if c.get(k)}
    return out or None


def main():
    src = json.loads((ROOT / "docs" / "camo-data.json").read_text(encoding="utf-8"))
    weapons = []
    for w in src["weapons"]:
        if w["name"] not in IDS:
            raise SystemExit(f"Unknown weapon name {w['name']!r}, add it to IDS")
        if w["class"] not in CLASS_IDS:
            raise SystemExit(f"Unknown class {w['class']!r} on {w['name']}")
        mil = w.get("military") or []
        if len(mil) != 8:
            raise SystemExit(f"{w['name']} needs exactly 8 military levels (use null for unknown)")
        sp = (w.get("special") or []) + [None] * 3
        weapons.append({
            "id": IDS[w["name"]],
            "name": w["name"],
            "cls": w["class"],
            "mil": mil,
            # Web guides got these wrong, so only levels read from the game count as verified.
            "v": bool(w.get("verified")),
            "sp": [
                {"name": s.get("name"), **(challenge(s) or {})} if isinstance(s, dict) else None
                for s in sp[:3]
            ],
            "gold": challenge(w.get("gold")),
            "notes": w.get("notes") or None,
        })
    data = {
        "weapons": weapons,
        "gold": None,
        "platinum": {k: challenge(v) for k, v in (src.get("platinum") or {}).items()},
        "harmonic": {k: challenge(v) for k, v in (src.get("harmonic_break") or {}).items()},
        "divergence": src.get("divergence") or None,
    }
    page = ROOT / "index.html"
    html = page.read_text(encoding="utf-8")
    block = "const DATA = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";"
    new, n = re.subn(r"(/\* DATA:BEGIN[^\n]*\n).*?(\n/\* DATA:END \*/)",
                     lambda m: m.group(1) + block + m.group(2), html, flags=re.S)
    if n != 1:
        raise SystemExit("DATA markers not found in index.html")
    page.write_text(new, encoding="utf-8")
    print(f"Inlined {len(weapons)} weapons")


if __name__ == "__main__":
    main()
