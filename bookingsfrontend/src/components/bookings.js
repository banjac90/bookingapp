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
    const [totalPages, setTotalPages] = useState(1);
    const pageSize = 10;
    
    useEffect(() => {
        const url = currentPage === 1 ? 'http://localhost:8000/api/bookings/' : `http://localhost:8000/api/bookings/?page=${currentPage}`;
        fetchBookings(url, ordering);
    }, [currentPage, ordering]);

    const fetchBookings = (url, ordering) => {
        axios.get( url, { 
            params: {ordering: ordering }
        }).then((response) => {
            setBookings(response.data.results);
            setTotalPages(Math.ceil(response.data.count / pageSize));
        }).catch((error) => {
            console.error(error);
        });
    }

    const handleSort = (field) => {
        setOrdering(ordering === field ? `-${field}` : field);
    };

    const handlePageChange = (page) => {
        setCurrentPage(page);
    }


    return (
        <div className='Contanier'>
            <h2>Bookings</h2> 
            <div className='bookings'>        
                <BookingList bookings={bookings} ordering = {ordering} onSort = {handleSort} />     
            </div>
            <Pagination currentPage = {currentPage} totalPages = {totalPages} onChangePage = {handlePageChange} />
        </div>
    );
};

export default Bookings;