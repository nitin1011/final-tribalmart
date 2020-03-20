import React from "react";
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import axios from "axios";
import FormInput from "../form-input/form-input-component";
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
import { Spin } from "antd";
import { authAxios } from "../../utils";
// import { Icon } from "antd";

import "./sign-component.css";
import * as actions from "../../store/actions/auth";

// const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;
class SignIn extends React.Component {
  constructor(props) {
    super();

    this.state = {
      email: "",
      password: ""
    };
  }

  componentDidMount() {
    axios.get(authAxios);
  }

  handleSubmit = async event => {
    event.preventDefault();
    const { email, password } = this.state;

    try {
      await this.props.onAuth(email, password);
      this.setState({ email: "", password: "" });
    } catch (err) {
      console.log(err);
    }
    this.props.history.push("/");
  };

  handleChange = event => {
    const { value, name } = event.target;
    this.setState({ [name]: value });
  };

  render() {
    let errorMessage = null;
    if (this.props.error) {
      errorMessage = <p>{this.props.error.message}</p>;
    }
    return (
      <MDBContainer className="form">
        {/* {errorMessage} */}
        {this.props.loading ? (
          <Spin />
        ) : (
          <MDBRow>
            <MDBCol md="9">
              <MDBCard className="card-item">
                <MDBCardBody className="mx-4">
                  <div className="text-center">
                    <h3 className="dark-grey-text mb-5">
                      <strong>Sign in</strong>
                    </h3>
                  </div>
                  <form onSubmit={this.handleSubmit}>
                    <FormInput
                      name="email"
                      label="Your email"
                      icon="envelope"
                      handleChange={this.handleChange}
                      value={this.state.email}
                      group
                      type="email"
                      validate
                      error="wrong"
                      success="right"
                    />
                    <FormInput
                      name="password"
                      label="Your password"
                      icon="lock"
                      value={this.state.password}
                      handleChange={this.handleChange}
                      group
                      type="password"
                      validate
                      containerClass="mb-0"
                    />
                    <p className="font-small blue-text d-flex justify-content-end pb-3">
                      Forgot
                      <a href="/#" className="blue-text ml-1">
                        Password?
                      </a>
                    </p>
                    <div className="text-center mb-3">
                      <MDBBtn
                        type="submit"
                        // onClick={}
                        color="blue"
                        rounded
                        className="btn-block z-depth-1a white-text"
                      >
                        Sign in
                      </MDBBtn>
                    </div>
                  </form>
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
                    <Link
                      className="blue-text ml-1 option"
                      to="/account/register "
                    >
                      Sign Up
                    </Link>
                  </p>
                </MDBModalFooter>
              </MDBCard>
            </MDBCol>
          </MDBRow>
        )}
      </MDBContainer>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onAuth: (email, password) => dispatch(actions.authLogin(email, password))
  };
};

const mapStateToProps = state => {
  return {
    loading: state.loading,
    error: state.error
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignIn);
