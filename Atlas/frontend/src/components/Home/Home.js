import React, { Component } from 'react';
import './style.css';


class Home extends Component {
  render() {
    return (

      <div className="Home">
        <header className="Home-header">
          <h1 className="Home-title">Enhance The Culture</h1>
          <h1 className="Home-title">Together.</h1>
        </header>
        <footer className="Home-footer">
          <a href="#cultural-heritages">See More</a>
        </footer>
      </div>
    );
  }
}

export default Home;