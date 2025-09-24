import os
import re
import argparse
import unicodedata

def clean_filename(filename: str, ascii_only: bool = False) -> str:
    """
    Clean filename while preserving semantic richness for metadata:
    - Replace spaces with underscores
    - Preserve accents/Unicode unless ascii_only=True
    - Allow alphanumeric (incl. Unicode), underscore, dash, and dot
    - Collapse multiple underscores
    """
    name, ext = os.path.splitext(filename)

    # Replace spaces with underscores
    name = name.replace(" ", "_")

    if ascii_only:
        # Normalize accents to ASCII
        name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()

    # Keep Unicode letters and numbers; remove weird symbols like °, ?, !
    name = re.sub(r"[^\w\-.]", "_", name, flags=re.UNICODE)

    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name)

    # Strip leading/trailing underscores/dots
    name = name.strip("._-")

    return f"{name}{ext}"

def rename_files(directory: str, dry_run: bool = True, ascii_only: bool = False):
    seen = {}
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if not os.path.isfile(old_path):
            continue

        new_filename = clean_filename(filename, ascii_only=ascii_only)
        base, ext = os.path.splitext(new_filename)

        # Handle collisions
        counter = 1
        while new_filename in seen or os.path.exists(os.path.join(directory, new_filename)):
            new_filename = f"{base}_{counter}{ext}"
            counter += 1

        seen[new_filename] = True

        if filename != new_filename:
            print(f"{filename}  →  {new_filename}")
            if not dry_run:
                os.rename(old_path, os.path.join(directory, new_filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean up filenames for RAG pipelines")
    parser.add_argument("directory", type=str, nargs="?", default=".", help="Target directory")
    parser.add_argument("--apply", action="store_true", help="Actually rename (default: dry-run)")
    parser.add_argument("--ascii", action="store_true", help="Convert accented chars to ASCII")
    args = parser.parse_args()

    rename_files(args.directory, dry_run=not args.apply, ascii_only=args.ascii)
