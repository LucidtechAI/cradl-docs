import React from "react";

const HeaderWithIcon = ({ icon, copy }) => {
  return (
    <h1>
      {/* {icon && ( */}
      <img
        src={icon}
        alt=""
        style={{
          display: "inline",
          marginRight: "8px",
          verticalAlign: "middle",
        }}
      />
      {/* )} */}
      <span>{copy}</span>
    </h1>
  );
};

export default HeaderWithIcon;
