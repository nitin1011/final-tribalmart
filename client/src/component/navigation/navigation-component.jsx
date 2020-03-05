import React from "react";
import { MDBCol, MDBIcon } from "mdbreact";
import "./navigation-component.css";
import Search from "../search-box/search-component";

const Navigation = () => {
  return (
    <div className="navbar fixed-top navbar-expand-lg navbar-light white scrolling-navbar">
      <div className="container">
        <a className="navbar-brand waves-effect">
          <strong className="blue-text">LOGO</strong>
        </a>

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
              <a className="nav-link waves-effect" href="#">
                Home
                <span className="sr-only">(current)</span>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link waves-effect" href="" target="_blank">
                Shop
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link waves-effect" href="">
                Contact Us
              </a>
            </li>
          </ul>

          <Search />

          <ul className="navbar-nav nav-flex-icons">
            <li className="nav-item">
              <a className="nav-link waves-effect">
                <span className="badge red z-depth-1 mr-1"> 1 </span>
                <i className="fas fa-shopping-cart"></i>
                <span className="clearfix d-none d-sm-inline-block">
                  {" "}
                  Cart{" "}
                </span>
              </a>
            </li>

            <li className="nav-item">
              <a
                href=""
                className="nav-link border border-light rounded waves-effect"
                target="_blank"
              >
                LOGIN
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Navigation;
