import React from 'react';
import './css/pagination.css';

const Pagination = ({ currentPage, totalPages, onChangePage }) => {
    const maxPages = 10;
    const startPage = Math.floor((currentPage - 1) / maxPages) * maxPages + 1;
    const endPage = Math.min(startPage + maxPages - 1, totalPages);

    const renderPageNumbers = () => {
        const pageNumbers = [];
        for (let i=startPage; i <= endPage; i++){
            pageNumbers.push(
                <button  
                key={i} 
                onClick={() => onChangePage(i)} 
                className={i === currentPage ? 'active' : ''}
                >{i}</button> 
            );
        }
        return pageNumbers;
    };

    return (
        <div className="pagination">
        <button onClick={() => onChangePage(currentPage - 1)} disabled={currentPage === 1}>
            Previous
        </button>       
            {renderPageNumbers()}
        <button onClick={() => onChangePage(currentPage + 1)} disabled={currentPage === totalPages}>
            Next
        </button> 
        </div>
    );
}

export default Pagination;