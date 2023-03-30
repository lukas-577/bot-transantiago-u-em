import requests
import json

hola = 'xD' 
print(hola)

if __name__ == '__main__':
    url = 'https://api.xor.cl/sismo/recent'
    args = {'magnitude':'5'}
    response = requests.get(url,params=args)
    #print(response.json()) es lo mismo que usar el content
    print(response.url)

response_json = json.loads(response.text)

if response.status_code == 200:
    # response_json = response.json() #es un diccionario
    # utc_date = response_json['events']
    # print(utc_date)

    
    for indice in response_json['events']:
        
        #print('el temblor fue a:  ' + response_json['events'][indice]['geo_reference'])
        #print( response_json['events'][indice]['magnitude']['value'])
        print('el temblor fue a:  ' + indice['geo_reference'])
        print(indice['magnitude']['value'])


else: print(response_json)