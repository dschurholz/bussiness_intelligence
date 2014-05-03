function deg2rad (angle) {
  // http://kevin.vanzonneveld.net
  // +   original by: Enrique Gonzalez
  // +     improved by: Thomas Grainger (http://graingert.co.uk)
  // *     example 1: deg2rad(45);
  // *     returns 1: 0.7853981633974483
  return angle * .017453292519943295; // (angle / 180) * Math.PI;
}

function rad2deg (angle) {
  // http://kevin.vanzonneveld.net
  // +   original by: Enrique Gonzalez
  // +      improved by: Brett Zamir (http://brett-zamir.me)
  // *     example 1: rad2deg(3.141592653589793);
  // *     returns 1: 180
  return angle * 57.29577951308232; // angle / Math.PI * 180
}

function getBoundingBox(lat_degrees, lon_degrees, distance_in_miles) {

    radius = 3963.1; // of earth in miles

    // bearings 
   due_north = 0;
    due_south = 180;
    due_east = 90;
    due_west = 270;

    // convert latitude and longitude into radians 
    lat_r = deg2rad(lat_degrees);
    lon_r = deg2rad(lon_degrees);
    
    // find the northmost, southmost, eastmost and westmost corners distance_in_miles away
    // original formula from
    // http://www.movable-type.co.uk/scripts/latlong.html

    northmost  = Math.asin(Math.sin(lat_r) * Math.cos(distance_in_miles/radius) + Math.cos(lat_r) * Math.sin (distance_in_miles/radius) * Math.cos(due_north));
    southmost  = Math.asin(Math.sin(lat_r) * Math.cos(distance_in_miles/radius) + Math.cos(lat_r) * Math.sin (distance_in_miles/radius) * Math.cos(due_south));
    
    eastmost = lon_r + Math.atan2(Math.sin(due_east)*Math.sin(distance_in_miles/radius)*Math.cos(lat_r),Math.cos(distance_in_miles/radius)-Math.sin(lat_r)*Math.sin(lat_r));
    westmost = lon_r + Math.atan2(Math.sin(due_west)*Math.sin(distance_in_miles/radius)*Math.cos(lat_r),Math.cos(distance_in_miles/radius)-Math.sin(lat_r)*Math.sin(lat_r));
        
        
    northmost = rad2deg(northmost);
    southmost = rad2deg(southmost);
    eastmost = rad2deg(eastmost);
    westmost = rad2deg(westmost);
     
    // sort the lat and long so that we can use them for a between query        
    if (northmost > southmost) { 
        lat1 = southmost;
        lat2 = northmost;
    
    } else {
        lat1 = northmost;
        lat2 = southmost;
    }


    if (eastmost > westmost) { 
        lon1 = westmost;
        lon2 = eastmost;
    
    } else {
        lon1 = eastmost;
        lon2 = westmost;
    }
    
    return { southWest : { lat : lat1, lng : lon1},
             northEast : { lat : lat2, lng : lon2} };
}

var bounds = getBoundingBox(-16.483498, -73.015137, 150);
console.log(bounds); 
console.log(bounds.northEast.lat - bounds.southWest.lat, bounds.northEast.lng - bounds.southWest.lng);
