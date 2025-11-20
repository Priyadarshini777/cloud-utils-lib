import re
from pathlib import Path

PYPROJECT = Path("pyproject.toml")


def bump_patch(version: str) -> str:
    major, minor, patch = version.split(".")
    patch = str(int(patch) + 1)
    return ".".join([major, minor, patch])


def main():
    content = PYPROJECT.read_text()
    match = re.search(r'version\s*=\s*"([^"]+)"', content)
    if not match:
        raise SystemExit("version not found in pyproject.toml")
    current = match.group(1)
    new = bump_patch(current)
    new_content = re.sub(
        r'version\s*=\s*"[^"]+"',
        f'version = "{new}"',
        content,
    )
    PYPROJECT.write_text(new_content)
    print(f"Bumped version: {current} -> {new}")


if __name__ == "__main__":
    main()
