from http.client import HTTPConnection
from urllib.parse import urlparse

def connectioned(url, timeout=5):
    parser = urlparse(url)
    error = Exception("ERROR")
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            print("CONNECTED")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error

urlprovided = input("What is the url of the site you want to check the connection for? ")
print("Checking connectivity...")
if connectioned(urlprovided) == True:
    print(f"Connected to {urlprovided} successfully")
else:
    pass
