import React from 'react';
import { Switch, Route } from 'react-router-dom'
import { MDBCol, MDBIcon } from "mdbreact";
import './App.css';


import Navigation from './component/navigation/navigation-component'
import Homepage from './pages/homepage/hompage';
import SignIn from './component/signInAndSignup/signIn-component'
import SignUp from './component/signInAndSignup/singup-component';


class App extends React.Component {
  render() {
    return (
      <div>
        <Navigation />
        <Switch>
          <Route exact path="/" component={Homepage}></Route>
          <Route exact path="/signin" component={SignIn}></Route>
          <Route exact path="/signup" component={SignUp}></Route>
          {/* <Route exact path="/signin" component={SignInAndSignUp}></Route>  */}

        </Switch>

      </div>


    )
  }
}
export default App;
