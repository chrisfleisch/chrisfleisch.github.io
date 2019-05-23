import flickrapi
import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# JSON-based secrets module
with open(os.path.join(BASE_DIR, 'settings.json')) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return exception."""
    return secrets[setting]


FLICKR_KEY = get_secret('FLICKR_KEY')
FLICKR_SECRET = get_secret('FLICKR_SECRET')
FLICKR_ID = get_secret('FLICKR_ID')
FLICKR_TAG = 'favorite' # or collection or album?


def main():

    print(f'Fetching photos from Flickr with tag: {FLICKR_TAG}')
    pass


if __name__ == "__main__":
    # execute only if run as a script
    main()
