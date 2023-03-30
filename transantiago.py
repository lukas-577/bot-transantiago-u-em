import requests
import json

hola = 'xD' 
print(hola)
paradero = 'PA4'
if __name__ == '__main__':
    url = 'https://api.xor.cl/red/bus-stop/'+paradero
    response = requests.get(url)
    #print(response.json()) es lo mismo que usar el content
    print(response.url)

response_json = json.loads(response.text)

if response.status_code == 200:

    
    for indice in response_json['services']:
        
        print('el bus es:  ' + indice['id'])
        print('status : ' + indice['status_description'])
        if indice['valid'] == True:
            for i in indice['buses']:
                print('patente : ' + i['id'])
                print('de : ' + str(i['min_arrival_time'])+' minutos')
                print('a : ' + str(i['max_arrival_time'])+' minutos')


                
            
        #print('distancia: ' + indice['buses']['meters_distance'])



else: print(response_json)