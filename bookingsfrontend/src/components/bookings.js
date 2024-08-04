import axios from 'axios';
import React, { useState, useEffect } from 'react';
import BookingList from './bookinglist';
/*
 * Bookings component
 * This component fetches the bookings from the API and renders them using the BookingList component
*/

const Bookings = () => {
    const [bookings, setBookings] = useState([]);
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/bookings/').then((response) => {
            setBookings(response.data);
        }).catch((error) => {
            console.error(error);
        });
    }, []);

    return (
        <div className='Contanier'>
            <h2>Bookings</h2> 
            <div className='bookings'>        
                <BookingList bookings={bookings} />     
            </div>       
        </div>
    );
};

export default Bookings;