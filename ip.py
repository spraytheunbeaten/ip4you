import requests
import os

os.system("clear")

print(' mmmmm  mmmmm     mm m     m  mmmm  m    m')
print('   #    #   "#   m"#  "m m"  m"  "m #    #')
print('   #    #mmm#"  #" #   "#"   #    # #    #')
print('   #    #      #mmm#m   #    #    # #    #')
print(' mm#mm  #          #    #     #mm#  "mmmm"')
print("\n")
def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "postal_code": response.get("postal"),
        "isp": response.get("org"),
        "asn": response.get("asn"),
        "languages": response.get("languages")
    }
    return location_data

ip_address = input("Enter an IP address: ")
location_data = get_location(ip_address)
os.system("clear")
print("Thanks for using my script.")
print("\n")
print(location_data)