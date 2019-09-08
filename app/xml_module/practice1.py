import requests, json
import xml.etree.ElementTree as Et


def read_xml():
    url = 'http://api.tektravels.com/SharedServices/SharedData.svc/rest/CountryList'
    data = {
      "TokenId": "52ea6c51-9839-4d6d-ab6c-fc7a2e280d77",
      "ClientId": "ApiIntegrationNew",
      "EndUserIp": "192.168.1.22"
    }
    response_data = requests.post(url=url, json=data)
    print("==", response_data.status_code)
    country_list = response_data.json().get('CountryList')
    countrylist_xml = Et.fromstring(country_list)
    print('vv', type(countrylist_xml))
    print(countrylist_xml.findall('Country')[0].find('Code').text)
    print(countrylist_xml.findall('Country')[0].find('Name').text)




if __name__ == "__main__":
    read_xml()