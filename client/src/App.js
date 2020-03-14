import React from 'react';
import { Switch, Route, } from 'react-router-dom'
import * as actions from './store/actions/auth';
import { MDBCol, MDBIcon } from "mdbreact";
import { connect } from 'react-redux'
import './App.css';


import Navigation from './component/navigation/navigation-component'
import Homepage from './pages/homepage/hompage';
import SignIn from './component/signInAndSignup/signIn-component'
import SignUp from './component/signInAndSignup/singup-component';


class App extends React.Component {
  componentDidMount() {
    this.props.onTryAutoSignup();
  }
  render() {
    return (
      <div>
        <Navigation {...this.props} />
        <Switch {...this.props}>
          <Route exact path="/" component={Homepage}></Route>
          <Route exact path="/account/login" component={SignIn}></Route>
          <Route exact path="/account/register" component={SignUp}></Route>
          {/* <Route exact path="/signin" component={SignInAndSignUp}></Route>  */}

        </Switch>

      </div >


    )
  }
}
const mapStateToProps = state => {
  return {
    isAuthenticated: state.token !== null
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onTryAutoSignup: () => dispatch(actions.authCheckState())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);