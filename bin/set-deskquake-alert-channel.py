#!/usr/bin/env python3

import argparse
import pathlib
import re
import sys


DEFAULT_CHANNEL_INDEX = 5
DEFAULT_CHANNEL_LABEL = "KL5PF"
INDEX_KEY = "USERPREFS_DESKQUAKE_ALERT_CHANNEL_INDEX"
LABEL_KEY = "USERPREFS_DESKQUAKE_ALERT_CHANNEL_LABEL"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Set the DeskQuake build-time alert channel in userPrefs.jsonc."
    )
    parser.add_argument(
        "--userprefs",
        default="userPrefs.jsonc",
        help="Path to the userPrefs.jsonc file to update.",
    )
    parser.add_argument(
        "--channel-index",
        type=int,
        help=f"DeskQuake alert channel index. Default prompt value is {DEFAULT_CHANNEL_INDEX}.",
    )
    parser.add_argument(
        "--channel-label",
        help=f"DeskQuake alert channel label. Default prompt value is {DEFAULT_CHANNEL_LABEL}.",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Require explicit arguments and skip prompts.",
    )
    return parser.parse_args()


def prompt_value(prompt: str, default: str) -> str:
    response = input(f"{prompt} [{default}]: ").strip()
    return response or default


def validate_channel_index(raw_value: str) -> int:
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise ValueError("Channel index must be an integer.") from exc

    if value < 0 or value > 7:
        raise ValueError("Channel index must be between 0 and 7.")
    return value


def validate_channel_label(value: str) -> str:
    label = value.strip()
    if not label:
        raise ValueError("Channel label must not be empty.")
    if '"' in label:
        raise ValueError("Channel label must not contain double quotes.")
    return label


def upsert_key(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf'^(\s*//\s*)?"{re.escape(key)}"\s*:\s*"[^"]*"\s*,?\s*$', re.MULTILINE)
    replacement = f'  "{key}": "{value}",'
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)

    closing_brace = text.rfind("}")
    if closing_brace == -1:
        raise ValueError("userPrefs.jsonc does not contain a closing brace.")

    prefix = text[:closing_brace].rstrip()
    suffix = text[closing_brace:]
    if not prefix.endswith("{"):
        prefix += "\n"
    return prefix + replacement + "\n" + suffix


def main() -> int:
    args = parse_args()
    userprefs_path = pathlib.Path(args.userprefs)

    if not userprefs_path.exists():
        print(f"userPrefs.jsonc not found: {userprefs_path}", file=sys.stderr)
        return 1

    if args.non_interactive and (args.channel_index is None or args.channel_label is None):
        print("--non-interactive requires --channel-index and --channel-label.", file=sys.stderr)
        return 1

    try:
        raw_index = str(args.channel_index) if args.channel_index is not None else prompt_value(
            "DeskQuake alert channel index", str(DEFAULT_CHANNEL_INDEX)
        )
        raw_label = args.channel_label if args.channel_label is not None else prompt_value(
            "DeskQuake alert channel label", DEFAULT_CHANNEL_LABEL
        )

        channel_index = validate_channel_index(raw_index)
        channel_label = validate_channel_label(raw_label)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    text = userprefs_path.read_text()
    text = upsert_key(text, INDEX_KEY, str(channel_index))
    text = upsert_key(text, LABEL_KEY, channel_label)
    userprefs_path.write_text(text)

    print(
        f"Updated {userprefs_path} with {INDEX_KEY}={channel_index} and {LABEL_KEY}={channel_label}."
    )
    print("Rebuild the firmware so the new DeskQuake alert channel is compiled in.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())