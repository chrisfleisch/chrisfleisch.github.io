# chrisfleisch.github.io

## Development

Running react in docker

```bash
docker compose build
docker compose up -d
docker compose exec fe bash
# inside container
npm install
npm start  # Browse to http://localhost:3000
```

To get photos from flickr setup python env with [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uv venv --python 3.13
uv pip install -r scripts/requirements.txt
```

Create `.env` and fill in values

```bash
FLICKR_KEY=""
FLICKR_SECRET=""
FLICKR_ID=""
```

Tag new photos on flickr with `favorite`. Then run get photos

```bash
uv run python scripts/get_photos.py
```

JS Code formatter

```bash
docker compose run --rm fe npx prettier . --check
docker compose run --rm fe npx prettier . --write
```

Build and test static

```bash
docker compose run --rm fe npm run build
python -m http.server -d fe/build
```
