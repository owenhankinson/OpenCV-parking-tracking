import axios from "axios";
import React from "react";


// returned from the flask backend. 
export interface Car {
    location: number
    color: string
}

interface ResponseData {
    cars: Car[]
}

export function getParkingData() {
    // this is where the call will come from for the car data
    Promise
    var res = axios.post(
        '/car-data'
    ).then(res => {

    })
}