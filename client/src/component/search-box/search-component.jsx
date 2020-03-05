import React from "react";
import { MDBCol, MDBIcon } from "mdbreact";

const SearchPage = () => {
  return (
    <MDBCol md="4">
      <form className="form-inline ">
        <MDBIcon icon="search" />
        <input
          className="form-control form-control-sm ml-3 w-75"
          type="text"
          placeholder="Search"
          aria-label="Search"
        />
      </form>
    </MDBCol>
  );
};

export default SearchPage;
