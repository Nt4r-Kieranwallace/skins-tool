# Zstd Tool (credit: Nt4r)

1. `pip install -r requirements.txt` (or run `run.bat`)
2. Put files in `out_zstd_key/` (any depth of subfolders)
3. Dict is embedded in `zstd_dict()` inside zstd_tool.py (falls back to a file in `zstd_dict/` if empty)
4. Run `python zstd_tool.py`

- Files with a zstd magic -> decompressed -> `decompression_zstd/`
- Other files -> compressed (header `22 4A 00 EF` + 4-byte length + zstd) -> `compress_zstd/`
- `.pkg.bytes` is unpacked, processed and repacked entirely in memory (BytesIO); nothing is extracted to disk, one output file per pkg, same name
- Extensions: .xml .bytes .txt .assetbundle .pkg.bytes
- Originals in `out_zstd_key/` are deleted after success (files with errors are kept)
