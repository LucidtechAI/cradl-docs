import React from 'react'


export default ({ title, text, icon, width='300px'}) => (
  <div style={{
    padding: '12px',
    display: 'flex',
    backgroundColor: '#222',
    border: '1px solid #444',
    borderRadius: '5px',
    width: width
  }}>
    <img src={icon} alt="Icon" height="30px" />
    <div style={{ padding: '2px 12px 16px 12px' }} >
      <h2>{title}</h2>
      {typeof text == 'string' ? <p>{text}</p> : text.map((t) => {return <p>{t}</p>})}
    </div>
  </div>
)