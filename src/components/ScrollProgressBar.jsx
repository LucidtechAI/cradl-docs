import React, { useState, useEffect } from 'react';
import './ScrollProgressBar.css'; // Import CSS file for styling

const ScrollProgressBar = () => {
  const [scrollProgress, setScrollProgress] = useState(2);

  useEffect(() => {
    const handleScroll = () => {
      const windowHeight = window.innerHeight;
      const scrollHeight = document.documentElement.scrollHeight - windowHeight;
      const scrollTop = window.scrollY;
      let progress = (scrollTop / scrollHeight) * 100;
      if (progress <= 2 ) progress = 2;
      setScrollProgress(progress);
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className="scroll-progress-bar" style={{ width: `${scrollProgress}%` }}></div>
  );
};

export default ScrollProgressBar;
