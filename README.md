# chrisfleisch.github.io

## Development

Running react in docker. `npm` only works inside Docker — a `preinstall`/`pre<script>` guard blocks it on the host and tells you to use Docker instead.

```bash
docker compose build
docker compose up -d
docker compose exec fe bash
# inside container
npm install
npm run dev  # Browse to http://localhost:5173
# install updates
npx npm-check-updates -u
rm package-lock.json
rm -r node_modules
npm install
```

Or, without an interactive shell, use the `docker-npm.sh` helper (`./scripts/docker-npm.sh <tools|fe> <npm-args...>`):

```bash
./scripts/docker-npm.sh fe install
./scripts/docker-npm.sh fe run dev  # Browse to http://localhost:5173
```

Use the `tools` service for the root `package.json` (e.g. after pulling changes to it):

```bash
./scripts/docker-npm.sh tools install
```

or to run tools container interactively:

```bash
docker compose run tools bash
# instide container
npx npm-check-updates -u
rm package-lock.json
rm -r node_modules
npm install
```

To get photos from flickr install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Setup pre-commit (Prettier/ESLint hooks run via the `tools` Docker service automatically)

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
./scripts/docker-npm.sh fe run build
uv run python -m http.server -d fe/build/client
```

Run the e2e test (builds, serves, and checks the page loads with no console/page errors or failed requests)

```bash
./scripts/docker-npm.sh fe run test:e2e
```

## Deployment

Create a PR and merge to main to initiate deployment to github pages.
