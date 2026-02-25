# my-data.download

A directory of services and how to download your personal data from each one. Your data belongs to you.

**[my-data.download](https://my-data.download)**

## What is this?

A simple, static website that lists services (Spotify, Netflix, GitHub, Instagram, etc.) and provides step-by-step instructions for downloading your personal data from each one. No build step. No frameworks. Just HTML, CSS, and JSON.

## JSON API

The source data is available as JSON at:

```
https://my-data.download/sources.json
```

Use it to build your own tools, dashboards, or automation.

## Contributing

Add a new source by editing `sources.json` and opening a pull request.

Each source entry needs:

| Field | Description |
|-------|-------------|
| `name` | Service name |
| `slug` | Lowercase, hyphenated identifier |
| `category` | One of: media, social, productivity, health, fitness, finance, browsing, communication, travel, shopping, home |
| `method` | One of: `api`, `manual_export`, `gdpr_request` |
| `description` | One-line summary of what data you get |
| `steps` | Numbered export instructions |
| `export_format` | File format (json, csv, xml, sqlite, zip) |
| `export_contents` | List of data types included |
| `use_cases` | What you can do with the data |
| `estimated_time` | How long the export takes |
| `estimated_size` | Approximate download size |
| `last_verified` | Date you last confirmed the instructions work (YYYY-MM-DD) |

Validate your JSON before submitting:

```sh
python3 -c "import json; json.load(open('sources.json'))"
```

## Running locally

```sh
python3 -m http.server
# Open http://localhost:8000
```

## Related

- [samla](https://github.com/janschill/samla) — A local-first toolkit for collecting and analyzing your personal data
