import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { KeywordScreen } from "./screens/keywords.screen";

function App() {
  return (
    <Router>
      <Route exact path='/keyword-selection' component={KeywordScreen} />
    </Router>
  );
}

export default App;
