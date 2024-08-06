import React, {useState, useMemo} from "react";
import BokingItem from "./bookingitem";
import "./css/bookings.css";
/*
 * BookingList component
 * This component renders a list of bookings
*/

const BookingList = ({ bookings, ordering, onSort }) => {

    const getClassNamesForCss = (name) => {
        /* Function for changing buttons class, so we can change it css */
        if (!ordering) {
            return;
        }
        return ordering === name ? "ascending" : ordering === `-${name}` ? "descending" : "";
    };

    return (
        <table className="bookings-table">
            <thead>
                <tr>                    
                    <th>Flat Name</th>
                    <th>ID</th>
                    <th>
                        <button type="button" onClick={() => onSort('check_in')} className={getClassNamesForCss('check_in')}>
                            Check-in
                        </button>
                    </th>
                    <th>Check-out</th>
                    <th>Previous booking ID</th>
                </tr>
            </thead>
            <tbody>
                {bookings.map((booking) => (
                    <BokingItem key={booking.id} booking={booking} />  
                ))}              
            </tbody>            
        </table>        
    );
}

export default BookingList;
