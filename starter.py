from google.transit import gtfs_realtime_pb2
import requests


API_KEY = 'A602sj4sf6eZUmKtqxITuFwtLh65KUhv'
API_URL = f"https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key={API_KEY}"

def get_data():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(API_URL)
    feed.ParseFromString(response.content)
    vehicle_info = {}
    count = 0
    # print(len(list(feed.entity)))
    for entity in feed.entity:
        dic = {}
        vehicle_id = entity.vehicle.vehicle.id
        dic['lat'] = entity.vehicle.position.latitude
        dic['long'] = entity.vehicle.position.longitude
        dic['trip_id'] = entity.vehicle.trip.trip_id
        dic['route_id'] = entity.vehicle.trip.route_id
        dic['time_stamp'] = entity.vehicle.timestamp
        dic['start_time'] = entity.vehicle.trip.start_time
        vehicle_info[vehicle_id] = dic
        # if count == 0:
        #     print(entity)
        count += 1
    # print(count)
    return vehicle_info

# get_data()