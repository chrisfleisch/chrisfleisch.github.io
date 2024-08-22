# chrisfleisch.github.io

Github Pages Site for chrisfleisch.com

## Development

Setup python env

```
micromamba create -n chrisfleisch python=3.11
micromamba activate chrisfleisch
pip install -r requirements.txt
```

Create `.env` and fill in values

```bash
FLICKR_KEY=""
FLICKR_SECRET=""
FLICKR_ID=""
```

Run get photos
```bash
python scripts/get_photos.py
```

Pelican
```bash
pelican content  # generate content
pelican --listen  # runserver at localhost:8000
```