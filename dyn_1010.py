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


resp = requests.post(f"{BASE_URL}/dyn/1010", headers=headers, json={
    "params": "passport-sdk-version=19&os_api=22&device_type=SM-G975N&ssmix=a&manifest_version_code=2021806060&dpi=240&uoo=0&carrier_region=AR&region=IQ&app_name=musical_ly&version_name=18.6.6&timezone_offset=10800&ts=1660261379&ab_version=18.6.6&residence=AR&cpu_support64=false&current_region=US&ac2=wifi&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=2021806060&channel=googleplay&_rticket=1660261381871&device_platform=android&iid=7126814077612115718&build_number=18.6.6&locale=ar&op_region=AR&version_code=180606&timezone_name=Europe%2FMoscow&cdid=86654e69-0edf-405a-a5a1-181f0e7aa14f&openudid=1c8a72b315ac7fbf&sys_region=IQ&device_id=6833300910404519430&app_language=ar&resolution=1280*720&os_version=5.1.1&language=en&device_brand=samsung&aid=1233&mcc_mnc=310410",
    "stub": "80FBE5B1515304B1223CD7457388785C"
})
pretty("POST /dyn/1010", resp)
