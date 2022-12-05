import React, { Component } from "react";
import { render } from "react-dom";
import ResponsiveAppBar from "./ResponseiveAppBar";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <div>
          <ResponsiveAppBar />
        </div>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);