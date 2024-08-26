import html
import json
from pathlib import Path

import flickrapi
from dateutil.parser import parse
from decouple import config

BASE_DIR = Path(__file__).parent.parent

FLICKR_KEY = config("FLICKR_KEY")
FLICKR_SECRET = config("FLICKR_SECRET")
FLICKR_ID = config("FLICKR_ID")
FLICKR_TAG = "favorite"  # grab photos with this tag


def get_photos(flickr=None, page=1, per_page=1):
    return flickr.photos.search(
        user_id="me",
        tags=FLICKR_TAG,
        page=page,
        per_page=per_page,
        extras="date_taken, url_o, url_n, url_k, url_q",
    )


def main():
    print(f"Fetching photos from Flickr with tag: {FLICKR_TAG}")
    flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format="parsed-json")
    flickr.authenticate_via_browser(perms="read")  # o-auth token saved to ~/.flickr/

    page = 1
    per_page = 10

    photos = get_photos(flickr=flickr, page=page, per_page=per_page)
    total_pages = photos["photos"]["pages"]

    photo_data = []  # hold photo data

    while page <= total_pages:
        for photo in photos["photos"]["photo"]:
            if photo["ispublic"] == 1:
                if "url_k" not in photo:
                    photo["url_k"] = photo["url_o"]
                print(photo["title"], photo["datetaken"])
                photo_data.append(
                    {
                        "title": html.escape(photo["title"]),
                        "datetaken": parse(photo["datetaken"]).strftime(
                            "%Y-%b-%d, %I:%M %p"
                        ),
                        "orig_datetaken": photo["datetaken"],
                        "url_q": photo["url_q"],  # thumbnail square 150
                        "height_q": photo["height_q"],
                        "width_q": photo["width_q"],
                        "url_n": photo["url_n"],  # small 320
                        "height_n": photo["height_n"],
                        "width_n": photo["width_n"],
                        "url_k": photo["url_k"],  # large size 2048
                        "height_k": photo["height_k"],
                        "width_k": photo["width_k"],
                        "url_o": photo["url_o"],  # original
                        "height_o": photo["height_o"],
                        "width_o": photo["width_o"],
                    }
                )
            else:
                print(f"{photo['title']} is not public")

        page += 1
        photos = get_photos(flickr=flickr, page=page, per_page=per_page)

    photo_data = sorted(photo_data, key=lambda x: x["orig_datetaken"], reverse=True)
    with Path(BASE_DIR / "fe/src/data/photos.json").open("w") as f:
        json.dump(photo_data, f, ensure_ascii=False, indent=2)

    print("Found", len(photo_data), "photos.")


if __name__ == "__main__":
    # execute only if run as a script
    main()
