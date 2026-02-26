#!/usr/bin/env python3
"""Generate API directory from sources.json.

Creates:
  api/index.json          — full array of all sources
  api/{slug}/index.json   — individual source object
"""

import json
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_PATH = os.path.join(ROOT, "sources.json")
API_DIR = os.path.join(ROOT, "api")


def main():
    with open(SOURCES_PATH) as f:
        sources = json.load(f)

    # Clean and recreate api/
    if os.path.exists(API_DIR):
        shutil.rmtree(API_DIR)
    os.makedirs(API_DIR)

    # api/index.json — full array
    with open(os.path.join(API_DIR, "index.json"), "w") as f:
        json.dump(sources, f, indent=2)

    # api/{slug}/index.json — individual sources
    for source in sources:
        slug = source["slug"]
        slug_dir = os.path.join(API_DIR, slug)
        os.makedirs(slug_dir, exist_ok=True)
        with open(os.path.join(slug_dir, "index.json"), "w") as f:
            json.dump(source, f, indent=2)

    print(f"Built API: {len(sources)} sources → api/")


if __name__ == "__main__":
    main()
