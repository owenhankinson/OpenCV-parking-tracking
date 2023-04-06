import { Row } from "antd";
import React, { useState } from "react";
import "./App.css";
import { Car, getParkingData } from "./parkingSpace/car";
import ParkingLot from "./parkingSpace/parkingSpace";

const App = () => {
const [cars, setCars] = useState<Car[] | undefined>(undefined)

  const getCarData = () => {
    // call to api 
    getParkingData()
  }
  return (
    <div className="App-wrapper">
      <header className="title">Hotchkiss</header>
      <Row>
        <ParkingLot 
          // input car data from API call
        />
      </Row>
    </div>
  );
};

export default App;
