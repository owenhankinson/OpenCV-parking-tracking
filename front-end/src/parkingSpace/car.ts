import React from "react";


// returned from the flask backend. 
export interface Car {
    location: number
    color: string
}

export function getParkingData() {
    // this is where the call will come from for the car data
}