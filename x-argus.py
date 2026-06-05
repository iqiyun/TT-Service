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


resp = requests.post(f"{BASE_URL}/sign", headers=headers, json={
    "params": "passport-sdk-version=5050090&manifest_version_code=410452&_rticket=1780570246021&app_language=en&app_type=normal&iid=7577158742728754999&channel=googleplay&device_type=SM-G986B&language=en&host_abi=arm64-v8a&locale=en&resolution=1440*2923&openudid=84858b4df4f8c40d&update_version_code=410452&ac2=wifi5g&cdid=438d1535-fbc1-422e-877e-8ca5be155b4f&sys_region=US&os_api=33&timezone_name=America/Chicago&dpi=600&ac=wifi&device_id=7505572926982309418&os=android&os_version=13&timezone_offset=-21600&version_code=410452&app_name=musically_go&ab_version=41.4.52&version_name=41.4.52&device_brand=samsung&op_region=GB&ssmix=a&device_platform=android&build_number=41.4.52&region=GB&aid=1340&mcc_mnc=310260&ts=1780570246",
    "payload": "email=486c666d6069696045636476716b676a7d2b666a68&mix_mode=1&account_sdk_source=app",
    "sig_data": {
        "app": {
            "appId":      1340,
            "appVersion": "41.4.52",
            "channel":    "googleplay"
        },
        "device": {
            "deviceId":   "7505572926982309418",
            "installId":  "7577158742728754999",
            "osVersion":  "13",
            "deviceType": "SM-G986B",
            "apiLevel":   "33",
            "cpuAbi":     "arm64-v8a"
        },
        "extra": {
            "licenseId":        "224921550",
            "MSSDKVersion":     "v05.00.00-alpha.124-ov-android",
            "MSSDKVersionCode": "83886112",
            "x_bd_kmsv":        "0",
            "x_bd_lanusk":      "none",
            "seed":             "",
            "seedAlgorithm":    0,
            "secDeviceIdToken": "",
            "dynTaskVersion":   [1003, 1010],
            "cookie":           {}
        },
        "geo": {
            "mccMnc": "310260"
        }
    }
})
pretty("POST /sign", resp)
