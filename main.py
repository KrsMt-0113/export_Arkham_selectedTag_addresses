import requests
import csv

page = 1
# fill your api key here
headers = {
    "API-Key": "YOUR_API_KEY"
}
# fill the tag after 'tag=' ⬇️
url = "https://api.arkm.com/tag/top?tag=YOUR_TAG&page="

total = requests.get("https://api.arkm.com/tag/YOUR_TAG/count_addresses", headers= headers).json()
print("Total addresses to fetch:", total)

result = []

while True:
    print("Fetching page:", page)
    try:
        response = requests.get(url+str(page), headers= headers, timeout= 100)
        data = response.json().get("addresses")
        for i in data:
            temp_result = {
                "address": i.get("address"),
                "entityName": i.get("arkhamEntity").get("name"),
                "entityId": i.get("arkhamEntity").get("id"),
                "chain": i.get("chain"),
                "isContract": i.get("contract")
            }
            if i.get("arkhamLabel"):
                temp_result["label"] = i.get("arkhamLabel").get("name")
            else:
                temp_result["label"] = "N/A"
            result.append(temp_result)
        print(f"page {page} done, total addresses fetched: {len(result)}")
        page += 1
    except Exception as e:
        print(f"Error fetching page {page}: {e}")
        continue
    if len(result) >= total:
        break

with open("cex_addresses.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["address", "entityName", "entityId", "chain", "label", "isContract"])
    for address in result:
        writer.writerow([address["address"], address["entityName"], address["entityId"], address["chain"], address["label"], address["isContract"]])
