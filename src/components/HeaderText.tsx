import React from 'react';


export default ({ title, text, width = '300px' }) => (
    <div>
        <h3>{title}</h3>
        <p>{text}</p>
    </div>
);