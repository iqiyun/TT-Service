# TT-Service

> A fast and reliable API for TikTok mobile service.

TT-Service is a high-performance REST API designed for developers working with TikTok's mobile app infrastructure. It provides up-to-date support for the latest TikTok versions (45.x and above), including request signing, device fingerprinting and dynamic function execution.

---

## 🚀 What's New

- ✅ **Argus 45.x** — Full support for the latest Argus signing algorithm used in TikTok 45.x
- ✅ **tt-ticket-guard v3** — Latest tt-ticket-guard header generation including EC key management and guard data construction
- ✅ **dsign** — Device property fingerprint generation for the TikTok device registration flow
- ✅ **Dynamic Functions** — dyn_1002, dyn_1003, dyn_1008, dyn_1010 fully supported

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/sign` | Generate Argus, Gorgon, Khronos and Ladon headers |
| `POST` | `/ttticket/keys` | Generate SECP256k1 EC key pair |
| `POST` | `/ttticket/build` | Build tt-ticket-guard v3 headers |
| `POST` | `/dsign` | Generate hashed device properties |
| `POST` | `/dyn/1002` | Execute dynamic function 1002 |
| `POST` | `/dyn/1003` | Execute dynamic function 1003 |
| `POST` | `/dyn/1008` | Execute dynamic function 1008 |
| `POST` | `/dyn/1010` | Execute dynamic function 1010 |
| `GET`  | `/health` | Health check |

---

## 🔐 POST /sign

Generates valid request signatures for TikTok API requests. Supports TikTok 45.x and above.

**Request Body:**
```json
{
    "params": "aid=1233&device_id=...&ts=...",
    "payload": "email=...&mix_mode=1",
    "sig_data": {
        "app": {
            "appId": 1233,
            "appVersion": "45.4.16",
            "channel": "beta"
        },
        "device": {
            "deviceId": "...",
            "installId": "...",
            "osVersion": "14",
            "deviceType": "Pixel 6",
            "apiLevel": "34",
            "cpuAbi": "arm64-v8a"
        },
        "extra": {
            "licenseId": "2142840551",
            "MSSDKVersion": "v05.02.07-alpha.6-ov-android",
            "MSSDKVersionCode": "84018976",
            "x_bd_kmsv": "0",
            "x_bd_lanusk": "none",
            "seed": "",
            "seedAlgorithm": 0,
            "secDeviceIdToken": "",
            "dynTaskVersion": [1003, 1010],
            "cookie": {}
        },
        "geo": {
            "mccMnc": "26202"
        }
    }
}
```

**Response:**
```json
{
    "X-Argus": "...",
    "X-Gorgon": "...",
    "X-Khronos": "1780570246",
    "X-Ladon": "...",
    "X-SS-Stub": "...",
    "X-SS-Req-Ticket": "..."
}
```

---

## 🔑 POST /ttticket/keys

Generates a SECP256k1 EC key pair for the tt-ticket-guard v3 flow.

**Request Body:**
```json
{}
```

**Response:**
```json
{
    "private_hex": "cc9361b7e688...",
    "public_b64": "BL0VT2ZEhOYk..."
}
```

---

## 🎫 POST /ttticket/build

Builds the complete tt-ticket-guard v3 header set for TikTok 45.x and above.

**Request Body:**
```json
{
    "path": "/passport/account/info/v2/",
    "device_token": "1|{\"aid\":1233,\"av\":\"45.4.16\",\"did\":\"...\",\"iid\":\"...\"}",
    "dtoken_sign": "ts.1.MEQC...",
    "private_hex": "cc9361b7e688..."
}
```

**Response:**
```json
{
    "headers": {
        "tt-ticket-guard-client-data": "...",
        "tt-ticket-guard-iteration-version": "0",
        "tt-ticket-guard-version": "3",
        "tt-ticket-guard-public-key": "..."
    },
    "guard_data_decoded": { ... },
    "keys": {
        "private_hex": "...",
        "public_b64": "..."
    }
}
```

---

## 📱 POST /dsign

Generates hashed device properties for the TikTok device registration flow.

**Request Body:**
```json
{
    "device": {
        "device": {
            "deviceModel": "oriole",
            "deviceManufacturer": "google",
            "internalStorageSize": 128849018880,
            "ramTotalSize": 7993675776,
            "screenWidth": 1080,
            "screenHeight": 2400,
            "bootTimeUTC": "1780570198",
            "sdcardSize": 90194313,
            "cpuCoreNum": 8,
            "densityDpi": 420,
            "cpuMaxFrequency": "2802000",
            "apiLevel": 34,
            "cpuAbi": "arm64-v8a",
            "deviceProduct": "oriole",
            "deviceBootLoader": "slider-1.3-11403664",
            "deviceChip": "gs101",
            "deviceBoard": "oriole"
        },
        "geo": {
            "timezoneName": "Europe/Berlin",
            "language_format3": "de"
        }
    }
}
```

**Response:**
```json
{
    "device_properties": {
        "device_model": "a3f2...",
        "device_manufacturer": "b8c1...",
        ...
    }
}
```

---

## ⚡ POST /dyn/1002, 1003, 1008, 1010

Executes TikTok dynamic signing functions.

**Request Body:**
```json
{
    "params": "aid=1233&device_id=...&ts=...",
    "stub": "80FBE5B1515304B1223CD7457388785C"
}
```

**Response:**
```json
{
    "result": "a3f2b8c1..."
}
```

---

## 🌐 RapidAPI

**TT-Service is available on RapidAPI:**

👉 [https://rapidapi.com/iqiyun/api/tt-service](https://rapidapi.com/iqiyun/api/tt-service)

---

## 💬 Support

For support and inquiries contact us on Telegram:

👉 [https://t.me/iqiyun](https://t.me/iqiyun)
