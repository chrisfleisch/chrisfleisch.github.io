from dateutil.parser import parse


import flickrapi
import html
import json
import os
import yaml


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
FLICKR_TAG = 'favorite'  # grab photos with this tag


def get_photos(flickr=None, page=1, per_page=1):
    return flickr.photos.search(user_id='me', tags=FLICKR_TAG,
        page=page, per_page=per_page,
        extras='date_taken, url_o, url_n, url_k, url_q')


def main():
    print(f'Fetching photos from Flickr with tag: {FLICKR_TAG}')
    flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET,
                                 format='parsed-json')
    flickr.authenticate_via_browser(perms='read')  # o-auth token saved to ~/.flickr/

    page = 1
    per_page = 5

    photos = get_photos(flickr=flickr, page=page, per_page=per_page)
    # print(photos)
    total_pages = photos['photos']['pages']

    photo_data = [] # hold photo data

    while page <= total_pages:
        for photo in photos['photos']['photo']:
            if 'url_k' not in photo:
                photo['url_k'] = photo['url_o']

            print(photo['title'])
            # print(photo['datetaken'])
            # print(photo['url_q']) # thumbnail square 150
            # print(photo['url_n']) # small 320
            # print(photo['url_k']) # large size 2048
            # print(photo['url_o']) # original
            # print('========')
            photo_data.append({
                'title': html.escape(photo['title']),
                'datetaken': parse(photo['datetaken']).strftime("%Y-%b-%d, %I:%M %p"),
                'url_q': photo['url_q'], # thumbnail square 150
                'url_n': photo['url_n'], # small 320
                'url_k': photo['url_k'], # large size 2048
                'url_o': photo['url_o'] # original
            })

        page += 1
        photos = get_photos(flickr=flickr, page=page, per_page=per_page)

    with open(os.path.join(BASE_DIR, '_data/photos.yml'), "w") as f:
        yaml.dump(photo_data, f)

    print('Found', len(photo_data), 'photos.')

    # print(photos)


if __name__ == "__main__":
    # execute only if run as a script
    main()
