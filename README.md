# chrisfleisch.github.io

## Development

Running react in docker

```bash
docker compose build
docker compose up -d
docker compose exec fe bash
# inside container
npm install
npm run dev  # Browse to http://localhost:5173
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

Build and test static

```bash
docker compose run --rm fe npm run build
uv run python -m http.server -d fe_rr/build/client
```

## Deployment

Create a PR and merge to main to initiate deployment to github pages.
