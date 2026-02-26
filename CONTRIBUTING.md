# Contributing

Thanks for helping build the directory! Adding a source is straightforward — edit one JSON file and open a pull request.

## Adding a source

1. Fork this repository
2. Edit `sources.json` — add your entry to the array
3. Validate: `python3 -c "import json; json.load(open('sources.json'))"`
4. Open a pull request

## Source schema

Every source needs these fields:

```json
{
  "name": "Service Name",
  "slug": "service-name",
  "category": "media",
  "description": "One-line summary of what data you get",
  "website": "https://example.com",
  "method": "manual_export",
  "method_details": "How the export works in plain language",
  "steps": [
    "Go to example.com/settings/export",
    "Click 'Download your data'",
    "Save the file"
  ],
  "export_format": "json",
  "export_contents": [
    "Activity history with timestamps",
    "Account and profile data"
  ],
  "use_cases": [
    "Analyze your usage over time",
    "Back up your account data"
  ],
  "gdpr": true,
  "estimated_time": "instant",
  "estimated_size": "under 10MB",
  "last_verified": "2025-02-01"
}
```

### Optional fields

- `export_url` — Direct link to the export/download page
- `api_docs` — Link to API documentation

### Field guidelines

| Field | Rules |
|-------|-------|
| `slug` | Lowercase, hyphenated (e.g., `apple-health`) |
| `category` | One of: media, social, productivity, health, fitness, finance, browsing, communication, travel, shopping, home |
| `method` | `api` (fully scriptable), `manual_export` (click and download), or `gdpr_request` (request and wait) |
| `steps` | Clear, numbered instructions anyone can follow |
| `export_format` | json, csv, xml, sqlite, zip, etc. |
| `estimated_time` | "instant", "a few hours", "up to 30 days", etc. |
| `last_verified` | YYYY-MM-DD — the date you confirmed the steps work |

## Updating a source

If export instructions have changed, update the relevant fields and set `last_verified` to today's date.

## How the API is generated

CI automatically generates `/api/` endpoints from `sources.json` on every push to `main`. Contributors never need to run the build — just edit `sources.json`.

## Running locally

```sh
python3 -m http.server
# Open http://localhost:8000
```

No build step needed. Edit files, refresh browser. To preview the API locally:

```sh
python3 scripts/build-api.py
```
