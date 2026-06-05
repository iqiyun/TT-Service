import json
import requests

RAPIDAPI_HOST = "tt-service.p.rapidapi.com"
RAPIDAPI_KEY  = "YOUR_RAPIDAPI_KEY"

BASE_URL = f"https://{RAPIDAPI_HOST}"

headers = {
    "x-rapidapi-host": RAPIDAPI_HOST,
    "x-rapidapi-key":  RAPIDAPI_KEY,
    "Content-Type":    "application/json",
}


def pretty(label, resp):
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  Status: {resp.status_code}")
    try:
        print(json.dumps(resp.json(), indent=2))
    except Exception:
        print(resp.text[:300])
    print(f"{'='*60}")


resp = requests.post(f"{BASE_URL}/dsign", headers=headers, json={
    "device": {
        "device": {
            "deviceModel":        "oriole",
            "deviceManufacturer": "google",
            "internalStorageSize": 128849018880,
            "ramTotalSize":        7993675776,
            "screenWidth":         1080,
            "screenHeight":        2400,
            "bootTimeUTC":         "1780570198",
            "sdcardSize":          90194313,
            "cpuCoreNum":          8,
            "densityDpi":          420,
            "cpuMaxFrequency":     "2802000",
            "apiLevel":            34,
            "cpuAbi":              "arm64-v8a",
            "deviceProduct":       "oriole",
            "deviceBootLoader":    "slider-1.3-11403664",
            "deviceChip":          "gs101",
            "deviceBoard":         "oriole"
        },
        "geo": {
            "timezoneName":     "Europe/Berlin",
            "language_format3": "de"
        }
    }
})
pretty("POST /dsign", resp)
