# Phatcraft Server
# Copyright 2026 Phatcraft

import toml


# Check server config file
try:
    open("config.toml", "r")
except:
    print("File config not found")
    exit()


# Load server config
config = toml.load(open("config.toml", "r"))
DOMAIN     = config["server"]["domain"]
HTTP_PORT  = config["server"]["http-port"]
HTTPS_PORT = config["server"]["https-port"]

CERTIFICATE = config["certificate"]["cert-file"]
PRIVATE_KEY = config["certificate"]["key-file"]

TEMPLATES_FOLDER = config["folders"]["template"]
STATIC_FOLDER    = config["folders"]["static"]


# Main server
if __name__ == "__main__":
    print(f"Domain: {DOMAIN}")
    print(f"HTTP Port: {HTTP_PORT}\nHTTPS Port: {HTTPS_PORT}")
    print(f"\nCertificate: {CERTIFICATE}\nPrivate key: {PRIVATE_KEY}")
    print("\nFolders")
    print(f"Template: {TEMPLATES_FOLDER}")
    print(f"Static  : {STATIC_FOLDER}")