# Contributing

## Setup

```bash
bundle install
cd automation && npm install
```

## Checks

```bash
bundle exec jekyll build
cd automation && npm test
```

`automation` currently contains operational scripts. If `npm test` is still the placeholder script, use a dry run instead:

```bash
bash ./update_data.sh --dry-run
```

## Content Rules

- Prefer updating existing pages before creating new public pages.
- Keep public navigation centered on `index.md` and `content_hub.md`.
- Put operational logs and generated intermediate artifacts under `automation/` or ignored paths.
- Do not commit secrets, private biomedical data, or private service credentials.

