import React from 'react';
import styles from './HeaderText.module.css';


export default ({ title, text, icon, width = '300px' }) => (
  <div className={styles.container}>
      <div className={styles.header}>
          { icon && <img src={icon} /> }
          <h3>{title}</h3></div>
      <p>{text}</p>
  </div>
);