import React from "react";
import { MDBInput } from "mdbreact";

const InputPage = ({ handleChange, ...otherprops }) => {
  return (
    <MDBInput className="form-input" onChange={handleChange} {...otherprops} />
  );
};

export default InputPage;
