import requests
import json

ACCESS_ID ='9xKgBsSEnApnNhGYgrpFp'
SECRET_KEY='z9VMTOpFSyWe7hNRn1w3xVHpxUGZO0WPWq9kirKj'
API_END_POINT='http://api.aerisapi.com/'

sunlightMountain = requests.get(API_END_POINT+'winter/snowdepth/48.41108,-114.33763?client_id='+ ACCESS_ID +'&client_secret='+SECRET_KEY)
sunlightMountainJSON = sunlightMountain.json()

print('Snow depth in centimeters : ' + str(sunlightMountainJSON.get('response',{}).get('periods')[0].get('snowDepthCM')))
print('Snow depth in inches : ' + str(sunlightMountainJSON.get('response',{}).get('periods')[0].get('snowDepthIN')))
