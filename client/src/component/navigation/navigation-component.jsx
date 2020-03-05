import React from "react";
import { MDBCol, MDBIcon } from "mdbreact";
import { Link } from "react-router-dom";
import "./navigation-component.css";
import Search from "../search-box/search-component";

const Navigation = () => {
  return (
    <div className="navbar fixed-top navbar-expand-lg navbar-light white scrolling-navbar">
      <div className="container">
        <Link className="navbar-brand waves-effect logo" to="/">
          <strong className="blue-text">LOGO</strong>
        </Link>

        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="true"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <Link className="nav-link waves-effect option" to="/">
                Home
                <span className="sr-only">(current)</span>
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link waves-effect option" to="/shop">
                Shop
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link waves-effect option" to="contactus">
                Contact Us
              </Link>
            </li>
          </ul>

          <Search />

          <ul className="navbar-nav nav-flex-icons">
            <li className="nav-item">
              <Link className="nav-link waves-effect">
                <span className="badge red z-depth-1 mr-1"> 1 </span>
                <i className="fas fa-shopping-cart"></i>
                <span className="clearfix d-none d-sm-inline-block">
                  {" "}
                  Cart{" "}
                </span>
              </Link>
            </li>

            <li className="nav-item">
              <Link
                className="nav-link border border-light rounded waves-effect option"
                to="/signin"
              >
                LOGIN
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Navigation;
