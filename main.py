import requests
import csv

page = 1

headers = {
    "API-Key": "YOUR_API_KEY"
}

url = "https://api.arkm.com/tag/top?tag=YOUR_selectedTag&page="

result = {}

total = requests.get("https://api.arkm.com/tag/cex/count_addresses", headers= headers).json()
print("Total addresses to fetch:", total)

while True:
    print("Fetching page:", page)
    try:
        response = requests.get(url+str(page), headers= headers, timeout= 100)
        data = response.json().get("addresses")
        for i in data:
            key = i.get("address")
            result[key] = {
                "address": i.get("address"),
                "entityName": i.get("arkhamEntity").get("name"),
                "entityId": i.get("arkhamEntity").get("id"),
                "chain": i.get("chain"),
                "isContract": i.get("contract")
            }
            if i.get("arkhamLabel"):
                result[key]["label"] = i.get("arkhamLabel").get("name")
            else:
                result[key]["label"] = "N/A"
        print(f"page {page} done, total addresses fetched: {len(result)}")
        page += 1
    except Exception as e:
        print(f"Error fetching page {page}: {e}")
        continue
    if len(result) >= total:
        break

with open("cex_addresses.csv", "w", encoding="utf-8") as f:
    fieldnames = ["address", "entityName", "entityId", "chain", "label", "isContract"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result)
