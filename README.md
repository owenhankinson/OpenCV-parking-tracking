# OpenCV-parking-tracking
An application for TMU students to see realtime (~30 second accuracy) "Rockstar" parking availibility.

## Workflow
The information which the front-end will run off of, will be aquired from a raspberry pi server that is hooked up to a camera. 

1. Every 30 seconds in a day, the raspberry Pi will be taking pictures and collecting them (2880 pictures a day ~1.4 GB at 1080p)
2. The PI server will wait until it recieves a request, then it will take the most recent photo taken, and run the CV algorithm held in `api.py`
3. The request will return a json object of a list of Cars in spaces:
  ```
  json {
    cars {
      [
        location: # whatever space the car is in
        color: # perhaps we can use this for a fun front-end feature. 
      ],
      [
        location: # whatever space the car is in
        color: # perhaps we can use this for a fun front-end feature. 
      ],
    },
  }
  ```
4. Front-end takes this information and displays to the user with a little graphic. 


## Things to think about;
1. If two users log on at once - will it request the same thing twice?
2. If a user stays active, does the webserver refetch the camera data
 -- we should probably add a last updated part of the front-end.
