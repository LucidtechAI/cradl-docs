import React from 'react'
import styles from './Box.module.css';

import { ArrowRight } from 'react-feather';


export const Box = ({ title, text, icon, children, background, border, padding='12px', width='300px'}) => (
  <div className={styles.box} style={{padding: padding, width: width, border: border, background: background}}>
    { icon }

    <div style={{ padding: '2px 12px 16px 12px' }} >
      <h3>{title}</h3>
      { text && <p>{text}</p>}
      { children }
    </div>
  </div>
);

export const SdkBox = ({ title, text, icon, width='300px'}) => (
    <div className={styles.box} style={{padding: '20px', width: width}}>
      <img src={icon} alt="Icon" height="30px" />
      <div style={{ padding: '2px 0px 0px 20px' }} >
        <h2>{title}</h2>
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