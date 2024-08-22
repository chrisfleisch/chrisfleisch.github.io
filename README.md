# chrisfleisch.github.io

## Development

Running react in docker

```bash
docker compose build
docker compose up -d
docker compose exec fe bash
# inside container
npm install
npm start
```


To get photos from flickr setup python env
```
micromamba create -n chrisfleisch python=3.10
micromamba activate chrisfleisch
pip install -r scripts/reqs.txt
```

Run get photos
```
python scripts/get_photos.py
```
