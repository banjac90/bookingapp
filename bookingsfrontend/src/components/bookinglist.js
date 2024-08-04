import React, {useState, useMemo} from "react";
import BokingItem from "./bookingitem";
import "./css/bookings.css";
/*
 * BookingList component
 * This component renders a list of bookings
*/

const BookingList = ({ bookings }) => {
    const [sortConfig, setSortConfig] = useState(null);

    /* We have default sort, but when user click on check in it will sort chek_in column.
    *  We user useMemo to avoid sorting on every render, only when bookings or sortConfig changes
    *  That is pretty efficient, because we can have a lot of bookings
    */
    const sortedBookings = useMemo( () => {
        let sortableBookings = [...bookings];
        if (sortConfig !== null) {
            sortableBookings.sort((a, b) => {
                if (a[sortConfig.key] < b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? -1 : 1;
                }
                if (a[sortConfig.key] > b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? 1 : -1;
                }
                return 0;                
            });        
        }
        return sortableBookings;
    }, [bookings, sortConfig]);

    /*
    * requestSort function for button click
    */
    const requestSort = (key) => {
        let direction = 'ascending';
        if (sortConfig && sortConfig.key === key && sortConfig.direction === 'ascending') {
            direction = 'descending';
        }	
        setSortConfig({key, direction});
        /*console.log(`Sorting by ${key} in ${direction} order`); use this only for debbuging and checking state*/
    };

    const getClassNamesForCss = (name) => {
        /* Function for changing buttons class, so we can change it css */
        if (!sortConfig) {
            return;
        }
        return sortConfig.key === name ? sortConfig.direction : undefined;
    };

    return (
        <table className="bookings-table">
            <thead>
                <tr>                    
                    <th>Flat Name</th>
                    <th>ID</th>
                    <th>
                        <button type="button" onClick={() => requestSort('check_in')} className={getClassNamesForCss('check_in')}>
                            Check-in
                        </button>
                    </th>
                    <th>Check-out</th>
                    <th>Previous booking ID</th>
                </tr>
            </thead>
            <tbody>
                {sortedBookings.map((booking) => (
                    <BokingItem key={booking.id} booking={booking} />  
                ))}              
            </tbody>            
        </table>        
    );
}

export default BookingList;
