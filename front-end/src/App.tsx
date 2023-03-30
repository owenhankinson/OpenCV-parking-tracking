import { Row } from "antd";
import React from "react";
import "./App.css";
import ParkingLot from "./parkingSpace/parkingSpace";

const App = () => {
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
