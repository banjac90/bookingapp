import axios from 'axios';
import React, { useState, useEffect } from 'react';
import BookingList from './bookinglist';
import Pagination from './pagination';
/*
 * Bookings component
 * This component fetches the bookings from the API and renders them using the BookingList component
*/

const Bookings = () => {
    const [bookings, setBookings] = useState([]);
    const [ordering, setOrdering] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const rowsPerPage = 10;
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/bookings/', {
            params: {ordering: ordering}
        }).then((response) => {
            setBookings(response.data);
        }).catch((error) => {
            console.error(error);
        });
    }, [ordering]);

    const handleSort = (field) => {
        setOrdering(ordering === field ? `-${field}` : field);
    };

    const handlePageChange = (page) => {
        setCurrentPage(page);
    }

    const indexOfLastBooking = currentPage * rowsPerPage;
    const indexOfFirstBooking = indexOfLastBooking - rowsPerPage; 
    const currentBookings = bookings.slice(indexOfFirstBooking, indexOfLastBooking); /* current bookings to render */
    const totalPages = Math.ceil(bookings.length / rowsPerPage);

    return (
        <div className='Contanier'>
            <h2>Bookings</h2> 
            <div className='bookings'>        
                <BookingList bookings={currentBookings} ordering = {ordering} onSort = {handleSort} />     
            </div>
            <Pagination currentPage = {currentPage} totalPages = {totalPages} onChangePage = {handlePageChange} />
        </div>
    );
};

export default Bookings;