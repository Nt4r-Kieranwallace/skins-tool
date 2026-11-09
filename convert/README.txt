R4NT | V1.2.0 - DEEP SPACE EDITION
====================================

Installation:
Install the required dependency:
pip install zstandard

For Pydroid 3:
Open Pip and install zstandard.

Directory Structure:
Only two directories are required. Both are automatically created when the program is run for the first time.

output_bytes/
    Stores .bytes and .pkg.bytes files.

output_xml/
    Stores .xml files.

Conversion Menu:

[1] Bytes -> XML
    Input: output_bytes/
    Output: output_xml/
    Automatically decompresses Zstandard (ZSTD) data before conversion.

[2] XML -> Bytes
    Input: output_xml/
    Output: output_bytes/
    Converts XML data back into Bytes format without compression.

Command-Line Execution:
python main.py decode
python main.py encode

Processing Rules:
- Recursively scans all subdirectories.
- Processes .pkg.bytes files entirely in RAM using BytesIO.
- Preserves original filenames during conversion.
- Successfully converted files are moved to the destination directory.
- Files that fail conversion are deleted.
- Empty directories are automatically removed.
- Configuration settings are managed through config.json.

Credit: R4NT | V1.2.0
