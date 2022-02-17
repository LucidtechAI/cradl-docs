import React from 'react';


export default ({ text, width='300px'}) => (
  <div style={{ padding: '12px', display: 'flex', width: width }}>
    <div style={{ padding: '2px 2px 2px 2px' }} >
      {Object.keys(text).map((item, i) => {
        return (
          <div>
            <h3>{item}</h3>
            <p>{text[item]}</p>
          </div>
        )
      })}
    </div>
  </div>
)