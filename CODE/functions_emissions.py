import requests


def extract_values(url_base, lon, lat, particle, year):
    eps = 0.0005
    url_full = (
            f"{url_base}&layers={particle}&query_layers={particle}&styles="
            "&crs=EPSG:4326"
            f"&bbox={lat-eps},{lon-eps},{lat+eps},{lon+eps}"
            "&width=3&height=3&i=1&j=1"
            "&info_format=application/json"
            f"&time={year}-01-01T00:00:00Z")
    req = requests.get(url=url_full, headers={"User-Agent": "ENSAE Projet Python - Emissions"})
    features = req.json()["features"]
    return features[0]["properties"]["GRAY_INDEX"] if features else None
