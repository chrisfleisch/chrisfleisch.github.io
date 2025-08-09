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

To get photos from flickr install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Setup pre-commit

```sh
uvx pre-commit install
```

Create `.env` and fill in values

```bash
FLICKR_KEY=""
FLICKR_SECRET=""
```

Tag new photos on flickr with `favorite`. Then run get photos

```bash
uv run get_photos.py
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

## Deployment

Create a PR and merge to main to initiate deployment to github pages.
