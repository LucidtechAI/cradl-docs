import React from 'react'
import styles from './box.module.css'

export const Box = ({ title, text, icon}) => (
  <div className={styles.boxContainer}>
    <img src={icon} alt="Icon" />
    <div className={styles.boxContent}>
      <h2>{title}</h2>
      <p>{text}</p>
    </div>
  </div>
)

export const BoxContainer = (props) => (
  <div className={styles.listContainer} {...props} />
)
