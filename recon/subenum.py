import requests
def check_subdomain(domain, sub):
    try:
        r = requests.get(f'https://{sub}.{domain}', timeout=3)
        return r.status_code
    except Exception:
        return None
if __name__=='__main__':
    print(check_subdomain('example.com','test'))
