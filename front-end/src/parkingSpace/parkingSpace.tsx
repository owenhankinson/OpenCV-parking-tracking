import React from "react";
import { Car } from "./car";
import "./style.css";

interface Props {
  Car?: Car[]; // there might be a car, or might not
}

// parking space holds the information of a single parking space. These
// will be used in a string on the front end to display all the parking
// spaces.
export default function ParkingLot(props: Props) {
  return (
    // put in logic - that we can define the whole layout of the parking
    // lot and also input cars at a specific space
    <div className="parking-space">
    </div>
  );
}
