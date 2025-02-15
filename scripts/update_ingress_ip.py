import os
import requests

token = os.environ.get("DIGITALOCEAN_TOKEN")
base_domain = os.environ.get("BASE_DOMAIN", "bolster.online")
do_base_url = "https://api.digitalocean.com/v2"


def get_subdomain_id(subdomain):
    url = f"{do_base_url}/domains/{base_domain}/records"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    records = response.json()["domain_records"]
    for record in records:
        if record["type"] == "A" and record["name"] == subdomain:
            return record["id"]


def update_ingress_ip(subdomain, ip):
    record_id = get_subdomain_id(subdomain)
    url = f"{do_base_url}/domains/{base_domain}/records/{record_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {"name": subdomain, "data": ip}
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()
    print(f"Updated {subdomain}.{base_domain} to {ip}")


if __name__ == "__main__":
    ...
