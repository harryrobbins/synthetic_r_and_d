"""Concatenate claims/<CID>-*/sections/*.md into claims/<CID>-*/claim.md and report word count."""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

for cid in sys.argv[1:] or [p.name.split("-")[0] for p in sorted((ROOT / "claims").glob("C*-*"))]:
    dirs = sorted((ROOT / "claims").glob(f"{cid}-*"))
    if not dirs:
        print(f"{cid}: no folder"); continue
    d = dirs[0]
    parts = sorted((d / "sections").glob("*.md"))
    text = "\n\n---\n\n".join(p.read_text().strip() for p in parts) + "\n"
    (d / "claim.md").write_text(text)
    print(f"{cid}: {len(parts)} sections, {len(text.split()):,} words -> {d.relative_to(ROOT)}/claim.md")
