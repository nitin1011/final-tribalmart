import React from "react";
import { MDBCol, MDBIcon, MDBBtn } from "mdbreact";
import { Link, withRouter } from "react-router-dom";
import "./navigation-component.css";
import Search from "../search-box/search-component";
import { connect } from "react-redux";
import * as actions from "../../store/actions/auth";

const Navigation = props => {
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

        <div
          className="collapse navbar-collapse options"
          id="navbarSupportedContent"
        >
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
              <Link className="nav-link waves-effect option" to="/contactus">
                Contact Us
              </Link>
            </li>
          </ul>

          <Search />

          <ul className="navbar-nav nav-flex-icons">
            <li className="nav-item">
              <Link className="nav-link waves-effect option" to="/cart">
                <span className="badge red z-depth-1 mr-1"> 1 </span>
                <i className="fas fa-shopping-cart"></i>
                <span className="clearfix d-none d-sm-inline-block">
                  {" "}
                  Cart{" "}
                </span>
              </Link>
            </li>

            {props.isAuthenticated ? (
              <li className="nav-item">
                <MDBBtn
                  className="nav-link border border-light rounded waves-effect option"
                  onClick={this.props.logout}
                >
                  Logout
                </MDBBtn>
              </li>
            ) : (
              <li className="nav-item">
                <Link
                  className="nav-link border border-light rounded waves-effect option"
                  to="/account/login"
                >
                  LOGIN
                </Link>
              </li>
            )}
          </ul>
        </div>
      </div>
    </div>
  );
};

const mapDispatchToProps = dispatch => {
  return {
    logout: () => dispatch(actions.logout())
  };
};

export default withRouter(connect(null, mapDispatchToProps)(Navigation));
