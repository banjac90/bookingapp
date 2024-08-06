import React from 'react';
import './css/pagination.css';

const Pagination = ({ currentPage, totalPages, onChangePage }) => {
    const renderPageNumbers = () => {
        const pageNumbers = [];
        for (let i=1; i <= totalPages; i++){
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
            {renderPageNumbers()}
        </div>
    );
}

export default Pagination;