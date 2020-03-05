import React from 'react';
import { MDBCol, MDBIcon } from "mdbreact";
import './App.css';

import Homepage from './pages/homepage/hompage'


import Navigation from './component/navigation/navigation-component'
import Product from './component/product/product-component';

class App extends React.Component {
  render() {
    return (

      <div>
        <Navigation />
        <Product />

      </div>


    )
  }
}
export default App;
