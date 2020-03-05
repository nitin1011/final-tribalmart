import React from "react";
import { Link } from "react-router-dom";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBInput,
  MDBBtn,
  MDBIcon,
  MDBModalFooter
} from "mdbreact";
import "./sign-component.css";

const SignIn = () => {
  return (
    <MDBContainer className="form">
      <MDBRow>
        <MDBCol md="9">
          <MDBCard className="card-item">
            <MDBCardBody className="mx-4">
              <div className="text-center">
                <h3 className="dark-grey-text mb-5">
                  <strong>Sign in</strong>
                </h3>
              </div>
              <MDBInput
                label="Your email"
                icon="envelope"
                group
                type="email"
                validate
                error="wrong"
                success="right"
              />
              <MDBInput
                label="Your password"
                icon="lock"
                group
                type="password"
                validate
                containerClass="mb-0"
              />
              <p className="font-small blue-text d-flex justify-content-end pb-3">
                Forgot
                <a href="#!" className="blue-text ml-1">
                  Password?
                </a>
              </p>
              <div className="text-center mb-3">
                <MDBBtn
                  type="button"
                  color="blue"
                  rounded
                  className="btn-block z-depth-1a white-text"
                >
                  Sign in
                </MDBBtn>
              </div>
              <p className="font-small dark-grey-text text-right d-flex justify-content-center mb-3 pt-2">
                or Sign in with:
              </p>
              <div className="row my-3 d-flex justify-content-center">
                <MDBBtn
                  type="button"
                  color="white"
                  rounded
                  className="mr-md-3 z-depth-1a"
                >
                  <MDBIcon
                    fab
                    icon="facebook-f"
                    className="blue-text text-center"
                  />
                </MDBBtn>
                <MDBBtn
                  type="button"
                  color="white"
                  rounded
                  className="mr-md-3 z-depth-1a"
                >
                  <MDBIcon fab icon="twitter" className="blue-text" />
                </MDBBtn>
                <MDBBtn
                  type="button"
                  color="white"
                  rounded
                  className="z-depth-1a"
                >
                  <MDBIcon fab icon="google-plus-g" className="blue-text" />
                </MDBBtn>
              </div>
            </MDBCardBody>
            <MDBModalFooter className="mx-5 pt-3 mb-1">
              <p className="font-small grey-text d-flex justify-content-end">
                Not a member?
                <Link className="blue-text ml-1 option" to="/signup">
                  Sign Up
                </Link>
              </p>
            </MDBModalFooter>
          </MDBCard>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
};

export default SignIn;
