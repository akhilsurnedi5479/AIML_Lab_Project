import config
import json



def get_flights(id):
    f = open('data.json')

    global data
    data= json.load(f)

    if id == 'best':
        get_flights_best()
    elif id == 'cheapest':
        get_flights_cheapest()
    elif id == 'fastest':
        get_flights_cheapest()
    else:
        get_flights_direct()
    f.close()


def get_flights_best():
    print(data['data']['buckets'][0])

    # Closing file


def get_flights_cheapest():

    print(data['data']['buckets'][1])

    # Closing file


def get_flights_fastest():


    print(data['data']['buckets'][2])

    # Closing file


def get_flights_direct():

    flights = data['data']['buckets'][3]['items']
    for flight in flights:
        #print(flight)
        print("Flight:",flight['legs'])
        print(flight['deeplink'])



get_flights('direct')
