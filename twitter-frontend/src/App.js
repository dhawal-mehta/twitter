import './App.css';
import { Homepage } from './pages/HomePage'

// const tweetDetailEl = document.querySelectorAll('tweet-detail')

function App(props) {
  // console.log(props)
  return (
    <div className="App">

      <Homepage {...props} />
      
      
    </div>
  );
}

export default App;
