
import './App.css';
import React from "react";
import Bookings from './components/bookings';


function App() {
  return (
    <div className="App" >
      <header>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
      </header>  
      <body>        
        <h1>Booking Reservations</h1> 
        <Bookings />
      </body>        
    </div>
  );
}

export default App;
