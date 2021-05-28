import './App.css';
import Homepage from './pages/HomePage'
// import React from 'react';

// const e = React.createElement

function App(props) {
  // console.log(props)
  return (
    <div className="App">

      <Homepage {...props} />
      
    </div>
  );
}

export default App;
