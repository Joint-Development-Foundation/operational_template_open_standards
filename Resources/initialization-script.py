#!/usr/bin/env python3
import argparse, pathlib, re, sys, yaml
from typing import Any, Dict

PLACEHOLDER_RE = re.compile(r"\{\{\s*([A-Za-z0-9_.-]+)\s*\}\}")

def flatten(d: Dict[str, Any], prefix: str = "", out: Dict[str, str] = None):
    """Flatten nested dict into dotted keys: {'a': {'b': 1}} -> {'a.b': '1'}"""
    if out is None:
        out = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else str(k)
        if isinstance(v, dict):
            flatten(v, key, out)
        else:
            out[key] = "" if v is None else str(v)
    return out

def load_yaml(path: pathlib.Path) -> Dict[str, str]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML root must be a mapping (key: value).")
    flat = flatten(data)
    # Also expose top-level keys without dot notation
    for k, v in list(data.items()):
        if not isinstance(v, dict):
            flat.setdefault(str(k), "" if v is None else str(v))
    return flat

def replace_content(text: str, mapping: Dict[str, str], strict: bool, missing: set):
    def repl(m):
        key = m.group(1)
        if key in mapping:
            return mapping[key]
        else:
            missing.add(key)
            return m.group(0) if not strict else ""
    return PLACEHOLDER_RE.sub(repl, text)

def main():
    p = argparse.ArgumentParser(
        description="Replace {{KEY}} placeholders in Markdown files using values from a YAML file."
    )
    p.add_argument("yaml_file", type=pathlib.Path, help="YAML file with key: value pairs")
    p.add_argument("inputs", nargs="+", help="Markdown files or globs (e.g., docs/**/*.md)")
    p.add_argument("--dry-run", action="store_true", help="Show changes but do not write files")
    p.add_argument("--strict", action="store_true",
                   help="If a key is missing, leave empty instead of keeping the placeholder")
    p.add_argument("--backup", action="store_true", help="Write a .bak file alongside each edited file")
    args = p.parse_args()

    mapping = load_yaml(args.yaml_file)

    # Expand globs to paths
    files = []
    for pattern in args.inputs:
        matches = list(pathlib.Path().glob(pattern))
        if matches:
            files.extend(matches)
        else:
            # treat as direct path
            files.append(pathlib.Path(pattern))

    if not files:
        print("No files matched.", file=sys.stderr)
        sys.exit(1)

    overall_missing = set()
    for path in files:
        if not path.exists() or not path.is_file():
            print(f"skip: {path} (not a file)", file=sys.stderr)
            continue
        original = path.read_text(encoding="utf-8")
        missing = set()
        updated = replace_content(original, mapping, args.strict, missing)
        overall_missing |= missing

        if args.dry_run:
            if original != updated:
                print(f"--- {path} (changes)")
            else:
                print(f"=== {path} (no changes)")
        else:
            if original != updated:
                if args.backup:
                    path.with_suffix(path.suffix + ".bak").write_text(original, encoding="utf-8")
                path.write_text(updated, encoding="utf-8")
                print(f"wrote: {path}")
            else:
                print(f"ok: {path} (no changes)")

    if overall_missing:
        miss = ", ".join(sorted(overall_missing))
        print(f"Note: missing keys encountered: {miss}", file=sys.stderr)
        if args.strict:
            print("Tip: remove --strict to keep unknown placeholders unchanged.", file=sys.stderr)

if __name__ == "__main__":
    main()
