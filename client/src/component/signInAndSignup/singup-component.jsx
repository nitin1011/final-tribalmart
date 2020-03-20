import React from "react";
import { Link } from "react-router-dom";
import { connect } from "react-redux";
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
import { authSignup } from "../../store/actions/auth";

import * as actions from "../../store/actions/auth";
import "./sign-component.css";

class SignUp extends React.Component {
  constructor(props) {
    super();

    this.state = {
      username: "",
      email: "",
      mobile: "",
      password: "",
      password2: ""
    };
  }

  handleSubmit = async event => {
    event.preventDefault();
    const { username, email, mobile, password, password2 } = this.state;

    try {
      await this.props.onAuth(username, email, mobile, password, password2);
      this.setState({
        username: "",
        email: "",
        mobile: "",
        password: "",
        passowrd2: ""
      });
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
    return (
      <MDBContainer className="form">
        <MDBRow>
          <MDBCol md="9">
            <MDBCard className="card-item">
              <MDBCardBody className="mx-4">
                <div className="text-center">
                  <h3 className="dark-grey-text mb-5">
                    <strong>Sign Up</strong>
                  </h3>
                </div>
                <form onSubmit={this.handleSubmit}>
                  <FormInput
                    name="username"
                    label="Username"
                    icon="user"
                    handleChange={this.handleChange}
                    value={this.state.username}
                    group
                    type="text"
                    validate
                    error="wrong"
                    success="right"
                  />
                  <FormInput
                    name="email"
                    label="Your email"
                    icon="envelope"
                    handleChange={this.handleChange}
                    value={this.state.email}
                    group
                    type="text"
                    type="email"
                    validate
                    error="wrong"
                    success="right"
                  />
                  <FormInput
                    name="mobile"
                    label="Mobile"
                    icon="envelope"
                    handleChange={this.handleChange}
                    value={this.state.mobile}
                    group
                    type="text"
                    type="text"
                    validate
                    error="wrong"
                    success="right"
                  />
                  <FormInput
                    name="password"
                    label="Your password"
                    icon="lock"
                    handleChange={this.handleChange}
                    value={this.state.password}
                    group
                    type="password"
                    validate
                    containerClass="mb-0"
                  />
                  <FormInput
                    name="password2"
                    label="Confirm password"
                    icon="key"
                    handleChange={this.handleChange}
                    value={this.state.password2}
                    group
                    type="password"
                    validate
                    containerClass="mb-0"
                  />
                  <div className="text-center mb-3">
                    <MDBBtn
                      type="submit"
                      // onClick={}
                      color="blue"
                      rounded
                      className="btn-block z-depth-1a white-text"
                    >
                      Sign Up
                    </MDBBtn>
                  </div>
                </form>
              </MDBCardBody>
              <MDBModalFooter className="mx-5 pt-3 mb-1">
                <p className="font-small grey-text d-flex justify-content-end">
                  Already a member?
                  <Link className="blue-text ml-1 option" to="/signin">
                    Login here
                  </Link>
                </p>
              </MDBModalFooter>
            </MDBCard>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onAuth: (username, email, mobile, password1, password2) =>
      dispatch(
        actions.authSignup(username, email, mobile, password1, password2)
      )
  };
};

const mapStateToProps = state => {
  return {
    loading: state.loading,
    error: state.error
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignUp);
