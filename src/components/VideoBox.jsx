import React from 'react'
import styles from './Box.module.css';

export const VideoBox = ({ title, text, icon, onClick, children, background, border, clickable, padding='12px', width='300px'}) => (
    <div 
    className={styles.box}
    style={{
        padding: padding,
        width: width,
        border: border,
        // background: 'background',
        cursor: clickable ? 'pointer' : 'auto'
        }} onClick={onClick}>
      { icon }
  
      <div className='flex flex-col justify-between' style={{ padding: '2px 12px 16px 12px' }} >
      <div>
        <h3>{title}</h3>
        { text && <p>{text}</p>}
        { children }
      </div>
         <video width="100%" height="240" controls>
            <source src="" type="video/mp4" />
        </video>
      </div>
    </div>
  );