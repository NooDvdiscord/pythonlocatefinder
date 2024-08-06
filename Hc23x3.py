import requests

def get_location():
    try:
        ip_response = requests.get('https://api.ipify.org?format=json')
        ip_address = ip_response.json()['ip']
        location_response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        location_data = location_response.json()
        city = location_data.get('city')
        region = location_data.get('region')
        country = location_data.get('country_name')
        postal_code = location_data.get('postal')

        return {
            "IP Address": ip_address,
            "City": city,
            "Region": region,
            "country": country,
            "Postal code": postal_code
        }
    
    except Exception as e:
        return{"error": str(e)}
    

    if __name__ == "__name__":
        location_info = get_location()
        print(location_info)