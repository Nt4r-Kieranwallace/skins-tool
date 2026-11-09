
import io
import os
import sys
import json
import zipfile
from pathlib import Path

import codec

BASE = Path(__file__).resolve().parent
CFG_PATH = BASE / "config.json"

DEFAULT_CFG = {
    "color": True,
    "delete_failed": True,
    "delete_empty_folders": True,
    "keep_other_files_in_pkg": False,
    "bytes_dir": "output_bytes",
    "xml_dir": "output_xml",
}

# ---------- space UI ----------
RST = "\033[0m"
GRAD = [93, 99, 63, 39, 45, 51]


def load_cfg():
    cfg = dict(DEFAULT_CFG)
    if CFG_PATH.exists():
        try:
            cfg.update(json.loads(CFG_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    else:
        CFG_PATH.write_text(json.dumps(DEFAULT_CFG, indent=2), encoding="utf-8")
    return cfg


CFG = load_cfg()


def col(n, text):
    return f"\033[38;5;{n}m{text}{RST}" if CFG["color"] else text


def bold(text):
    return f"\033[1m{text}{RST}" if CFG["color"] else text


LOGO = [
    "██████╗ ██╗  ██╗███╗   ██╗████████╗",
    "██╔══██╗██║  ██║████╗  ██║╚══██╔══╝",
    "██████╔╝███████║██╔██╗ ██║   ██║   ",
    "██╔══██╗╚════██║██║╚██╗██║   ██║   ",
    "██║  ██║     ██║██║ ╚████║   ██║   ",
    "╚═╝  ╚═╝     ╚═╝╚═╝  ╚═══╝   ╚═╝   ",
]

SKY = [
    "  ·   ˚   ✦    .     *     ·     ✧    .    ˚   ·  ",
    "     .    ★        ·    ˚      .    ✦      .      ",
]


def banner():
    print()
    print(col(60, SKY[0]))
    for i, line in enumerate(LOGO):
        print("   " + bold(col(GRAD[i], line)))
    print(col(60, SKY[1]))
    print(col(141, "   ✦ B Y T E S  ⇄  X M L  //  D E E P  S P A C E ✦"))
    print(col(244, "                     R4NT  ·  V1.2.0"))
    print()


def footer():
    line = "✦ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ✦"
    print()
    print(col(60, line))
    print(col(213, "   ☄  C R E D I T   :   ") + bold(col(51, "R 4 N T")))
    print(col(141, "   ★  V 1 . 2 . 0   ·   D E E P   S P A C E"))
    print(col(60, line))
    print()


def menu():
    print(col(99, "  ╭─── M I S S I O N   C O N T R O L ───"))
    print(col(99, "  │"))
    print(col(99, "  │ ") + col(51, "[1]") + "  LAUNCH   bytes ➜ xml   " + col(244, "(zstd decompress)"))
    print(col(99, "  │ ") + col(213, "[2]") + "  ORBIT    xml ➜ bytes")
    print(col(99, "  │ ") + col(244, "[0]") + "  ABORT")
    print(col(99, "  │"))
    print(col(99, "  ╰───────────────────────────────────────"))


def bar(i, total, width=18):
    f = int(width * i / total) if total else width
    return col(51, "█" * f) + col(60, "░" * (width - f))


# ---------- convert ----------
def convert_blob(mode, data):
    return codec.bytes_to_xml(data) if mode == "decode" else codec.xml_to_bytes(data)


def target_ext(mode):
    return ".bytes" if mode == "decode" else ".xml"


def swap_ext(name, mode):
    if mode == "decode":
        return name[: -len(".bytes")] + ".xml"
    return name[: -len(".xml")] + ".bytes"


def handle_pkg(mode, data):

    zin = zipfile.ZipFile(io.BytesIO(data))
    out = io.BytesIO()
    ok = bad = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            if info.is_dir():
                continue
            raw = zin.read(info.filename)
            if info.filename.lower().endswith(target_ext(mode)):
                try:
                    zout.writestr(swap_ext(info.filename, mode), convert_blob(mode, raw))
                    ok += 1
                except Exception:
                    bad += 1
            elif CFG["keep_other_files_in_pkg"]:
                zout.writestr(info.filename, raw)
    if ok == 0:
        raise ValueError("pkg has no convertible file")
    return out.getvalue(), ok, bad


def run(mode):
    bytes_dir = (BASE / CFG["bytes_dir"]).resolve()
    xml_dir = (BASE / CFG["xml_dir"]).resolve()
    bytes_dir.mkdir(parents=True, exist_ok=True)
    xml_dir.mkdir(parents=True, exist_ok=True)

    if mode == "decode":
        src_root, dst_root, label = bytes_dir, xml_dir, "bytes ➜ xml"
    else:
        src_root, dst_root, label = xml_dir, bytes_dir, "xml ➜ bytes"

    files = []
    for p in sorted(src_root.rglob("*")):
        if not p.is_file():
            continue
        low = p.name.lower()
        if low.endswith(".pkg.bytes") or low.endswith(target_ext(mode)):
            files.append(p)

    print(col(141, f"\n  ✦ MISSION: {label}"))
    print(col(244, f"    from : {src_root.name}/   to : {dst_root.name}/"))
    print(col(244, f"    targets locked: {len(files)}\n"))

    if mode == "decode" and codec.zstd is None:
        print(col(214, "  ⚠ zstandard not installed -> ไฟล์ที่บีบอัดจะอ่านไม่ได้ (pip install zstandard)\n"))

    done = failed = 0
    total = len(files)
    for n, src in enumerate(files, 1):
        rel = src.relative_to(src_root)
        is_pkg = src.name.lower().endswith(".pkg.bytes")
        try:
            data = src.read_bytes()
            if is_pkg:
                result, ok, bad = handle_pkg(mode, data)
                out_path = dst_root / rel
                tag = f"pkg ✦ {ok} ok / {bad} lost"
            else:
                result = convert_blob(mode, data)
                out_path = dst_root / rel.parent / swap_ext(src.name, mode)
                tag = "ok"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(result)
            src.unlink()
            done += 1
            print(f"  {bar(n, total)} {col(120, '✔')} {rel}  {col(244, tag)}")
        except Exception as e:
            failed += 1
            tag = type(e).__name__
            if CFG["delete_failed"]:
                try:
                    src.unlink()
                    tag += " · destroyed"
                except OSError:
                    pass
            print(f"  {bar(n, total)} {col(203, '✖')} {rel}  {col(203, tag)}")

    removed = 0
    if CFG["delete_empty_folders"]:
        for dirpath, _, _ in os.walk(src_root, topdown=False):
            p = Path(dirpath)
            if p != src_root and not any(p.iterdir()):
                p.rmdir()
                removed += 1

    print(col(60, "\n  ╭─── MISSION REPORT ───"))
    print(col(60, "  │ ") + col(120, f"landed   : {done}"))
    print(col(60, "  │ ") + col(203, f"destroyed: {failed}"))
    print(col(60, "  │ ") + col(244, f"void dirs swept: {removed}"))
    print(col(60, "  ╰──────────────────────"))


def main():
    CFG_PATH.exists() or load_cfg()
    (BASE / CFG["bytes_dir"]).mkdir(exist_ok=True)
    (BASE / CFG["xml_dir"]).mkdir(exist_ok=True)

    banner()
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    if arg in ("decode", "encode"):
        run(arg)
        footer()
        return

    while True:
        menu()
        try:
            c = input(col(51, "\n  ➜ select: ")).strip()
        except (EOFError, KeyboardInterrupt):
            break
        if c == "1":
            run("decode")
        elif c == "2":
            run("encode")
        elif c == "0":
            break
        else:
            print(col(203, "  ✖ unknown command"))
        print()
    footer()


if __name__ == "__main__":
    main()
