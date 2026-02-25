## Adding a new source

Please add your source entry to `sources.json`. Use this checklist:

- [ ] Entry added to `sources.json` with all required fields
- [ ] `slug` is lowercase, hyphenated (e.g., `apple-health`)
- [ ] `category` is one of: media, social, productivity, health, fitness, finance, browsing, communication, travel, shopping, home
- [ ] `method` is one of: `api`, `manual_export`, `gdpr_request`
- [ ] `steps` are clear and numbered
- [ ] `export_contents` lists what data you actually get
- [ ] `use_cases` lists what you can do with the data
- [ ] `last_verified` is set to today's date (YYYY-MM-DD)
- [ ] JSON is valid (run `python3 -c "import json; json.load(open('sources.json'))"`)

### Required fields

```json
{
  "name": "Service Name",
  "slug": "service-name",
  "category": "category",
  "description": "One-line description of what data you get",
  "website": "https://example.com",
  "method": "api | manual_export | gdpr_request",
  "method_details": "How the export method works",
  "steps": ["Step 1", "Step 2"],
  "export_format": "json | csv | xml | sqlite | zip",
  "export_contents": ["Data type 1", "Data type 2"],
  "use_cases": ["Use case 1", "Use case 2"],
  "gdpr": true,
  "estimated_time": "instant | a few hours | up to 30 days",
  "estimated_size": "under 1MB | 10MB-100MB",
  "last_verified": "2025-01-01"
}
```

### Optional fields

- `export_url` — Direct link to the export/download page
- `api_docs` — Link to API documentation
