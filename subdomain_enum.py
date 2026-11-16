import requests
import sys
import json

def enumerate_subdomains(domain):
    print(f"[*] Starting subdomain enumeration for: {domain}")
    
    # We use the free crt.sh API (Certificate Transparency Logs)
    # This is a passive recon technique that doesn't touch the target directly.
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        subdomains = set()
        for entry in data:
            # The 'name_value' field can contain multiple domains separated by newlines
            names = entry.get('name_value', '').split('\n')
            for name in names:
                if name and "*" not in name:
                    subdomains.add(name.strip().lower())
                    
        print(f"\n[+] Found {len(subdomains)} unique subdomains:\n")
        for sub in sorted(subdomains):
            print(sub)
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error querying crt.sh: {e}")
    except json.JSONDecodeError:
        print("[-] Error parsing JSON response. The API might be down or rate-limited.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subdomain_enum.py <domain>")
        print("Example: python subdomain_enum.py example.com")
        sys.exit(1)
        
    target_domain = sys.argv[1]
    enumerate_subdomains(target_domain)
