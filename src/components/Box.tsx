import React from 'react'
import styles from './Box.module.css';

import { ArrowRight } from 'react-feather';


export const Box = ({ title, text, icon, onClick, children, background, border, clickable, padding='12px', width='300px'}) => (
  <div className={styles.box} style={{
      padding: padding,
      width: width,
      border: border,
      background: background,
      cursor: clickable ? 'pointer' : 'auto'
      }} onClick={onClick}>
    { icon }

    <div style={{ padding: '2px 12px 16px 12px' }} >
      <h3>{title}</h3>
      { text && <p>{text}</p>}
      { children }
    </div>
  </div>
);

export const TextBox =({ title, text, icon, width='300px'}) => (
  <div className={styles.textBox} style={{width: width}}>
    { icon }

    <div style={{ padding: '2px 2px 2px 2px' }} >
      <h3>{title}</h3>
      {typeof text == 'string' ? <p>{text}</p> : text.map((t) => {return <p>{t}</p>})}
    </div>
  </div>
);

export const BoxAction = ({text, href, icon}) => (
    <a className={styles.boxAction} href={href}>
        <span className={styles.boxActionText}>{text}</span>
        <ArrowRight />
    </a>
);

export default Box;