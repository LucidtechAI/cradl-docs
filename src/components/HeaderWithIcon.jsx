import React from "react";

const HeaderWithIcon = ({ children, icon }) => {
  return (
    <h1>
      {/* {icon && ( */}
      <img
        src={icon}
        alt=""
        style={{
          display: "inline-block",
          marginRight: "8px",
          verticalAlign: "middle",
        }}
      />
      {/* )} */}
      {children}
    </h1>
  );
};

export default HeaderWithIcon;
