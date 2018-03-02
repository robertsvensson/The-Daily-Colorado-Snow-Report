var ACCESS_ID ='9xKgBsSEnApnNhGYgrpFp';
var SECRET_KEY='z9VMTOpFSyWe7hNRn1w3xVHpxUGZO0WPWq9kirKj';
var API_END_POINT='https://api.aerisapi.com/';

var req = new XMLHttpRequest();

req.open("GET",API_END_POINT+'winter/snowdepth/48.41108,-114.33763?client_id='+ ACCESS_ID +'&client_secret='+SECRET_KEY,false);
req.send(null);

var obj = JSON.parse(req.response);
console.log(obj.response.periods[0].snowDepthIN)
