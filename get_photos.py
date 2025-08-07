# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
#     "requests-oauthlib",
#     "environs",
#     "python-dateutil",
# ]
# ///
import html
import os
import json
import requests
import webbrowser
from environs import env
from requests_oauthlib import OAuth1
from dateutil.parser import parse
from pathlib import Path

# ---------------- Configuration ---------------- #
env.read_env()

BASE_DIR = Path(__file__).parent

API_KEY = env("FLICKR_KEY")
API_SECRET = env("FLICKR_SECRET")
TOKEN_FILE = "flickr_token.json"

REQUEST_TOKEN_URL = "https://www.flickr.com/services/oauth/request_token"
AUTHORIZE_URL = "https://www.flickr.com/services/oauth/authorize"
ACCESS_TOKEN_URL = "https://www.flickr.com/services/oauth/access_token"

# ---------------- Token Handling ---------------- #


def load_access_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return json.load(f)
    return None


def save_access_token(token_data):
    with open(TOKEN_FILE, "w") as f:
        json.dump(token_data, f)


def get_authenticated_session():
    token_data = load_access_token()
    if token_data:
        print("✅ Loaded saved access token.")
        return OAuth1(
            API_KEY,
            client_secret=API_SECRET,
            resource_owner_key=token_data["oauth_token"],
            resource_owner_secret=token_data["oauth_token_secret"],
        )

    # Start OAuth flow
    print("🔐 Starting OAuth authentication...")

    oauth = OAuth1(API_KEY, client_secret=API_SECRET, callback_uri="oob")
    r = requests.post(REQUEST_TOKEN_URL, auth=oauth)
    creds = dict(x.split("=") for x in r.text.split("&"))
    resource_owner_key = creds["oauth_token"]
    resource_owner_secret = creds["oauth_token_secret"]

    auth_url = f"{AUTHORIZE_URL}?oauth_token={resource_owner_key}&perms=read"
    print("➡️  Open this URL in your browser and authorize the app:")
    print(auth_url)
    webbrowser.open(auth_url)

    verifier = input("🔑 Enter the verifier code here: ")

    oauth = OAuth1(
        API_KEY,
        client_secret=API_SECRET,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )

    r = requests.post(ACCESS_TOKEN_URL, auth=oauth)
    access_data = dict(x.split("=") for x in r.text.split("&"))

    save_access_token(access_data)
    print("💾 Access token saved!")

    return OAuth1(
        API_KEY,
        client_secret=API_SECRET,
        resource_owner_key=access_data["oauth_token"],
        resource_owner_secret=access_data["oauth_token_secret"],
    )


# ---------------- Flickr Photo Search ---------------- #


def search_photos(tag, per_page=50, max_pages=None):
    oauth = get_authenticated_session()
    base_url = "https://www.flickr.com/services/rest/"
    all_photos = []
    page = 1

    while True:
        params = {
            "method": "flickr.photos.search",
            "format": "json",
            "nojsoncallback": 1,
            "tags": tag,
            "per_page": per_page,
            "page": page,
            "safe_search": 1,
            "content_type": 1,
            "sort": "relevance",
            "extras": "url_o,url_k,url_n,url_q,date_taken",
            "user_id": "me",
        }

        r = requests.get(base_url, params=params, auth=oauth)
        r.raise_for_status()
        data = r.json()

        photos = data.get("photos", {}).get("photo", [])
        total_pages = data.get("photos", {}).get("pages", 0)

        print(f"📄 Page {page} of {total_pages} — Retrieved {len(photos)} photos")

        for photo in photos:
            if photo["ispublic"] == 1:
                if "url_k" not in photo:
                    photo["url_k"] = photo[
                        "url_o"
                    ]  # Fallback to original if large size is not available
                all_photos.append(
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
                print(f"❌ {photo['title']} is not public")

        page += 1

        # Stop if we reached the last page or hit a max_pages limit
        if page > total_pages or (max_pages and page > max_pages):
            break

    all_photos = sorted(all_photos, key=lambda x: x["orig_datetaken"], reverse=True)
    with Path(BASE_DIR / "fe/src/data/photos.json").open("w") as f:
        json.dump(all_photos, f, ensure_ascii=False, indent=2)
    return all_photos


# ---------------- Main ---------------- #

if __name__ == "__main__":
    tag = input("🔍 Enter a tag to search for: ")
    results = search_photos(tag)
    print(f"\n📸 Found {len(results)} photos.")
