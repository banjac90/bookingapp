import React from "react";

/*
 * BookingItem component
 * This component renders a single booking
 * Because React works as it does, we create a new component for each booking
 * instead of rendering all bookings in a single component this is more efficient
 * if we would have a large number of bookings and want to filter them
 */

const BookingItem = ({ booking }) => {
    return(
        <tr>            
            <td>{booking.flat_name}</td>
            <td>{booking.id}</td>
            <td>{booking.check_in}</td>
            <td>{booking.check_out}</td>
            <td>{booking.previous_booking_id}</td>
        </tr>
    );
}

export default BookingItem;

