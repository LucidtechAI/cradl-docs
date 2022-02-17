import React from 'react';


export default ({ title, text, width='300px'}) => (
  <div style={{ padding: '12px', display: 'flex', width: width }}>
    <div style={{ padding: '2px 2px 2px 2px' }} >
      <h3>{title}</h3>
      {typeof text == 'string' ? <p>{text}</p> : text.map((t) => {return <p>{t}</p>})}
    </div>
  </div>
)

