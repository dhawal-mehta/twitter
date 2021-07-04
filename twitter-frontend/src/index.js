import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import TweetDetail from './organisms/TweetDetail'

const tweetsEl = document.getElementById('root')
const tweetDetailEl = document.querySelectorAll('.tweet-detail')


const e = React.createElement

console.log(tweetDetailEl)

tweetDetailEl.forEach( container => {
  ReactDOM.render(
  <>
    {e(TweetDetail, container.dataset)}
  </>,
  container
  )
})

if (tweetsEl){
  ReactDOM.render(
    <React.StrictMode>
      {/* // <NewApp /> */}
      { e(App, tweetsEl.dataset) }
    </React.StrictMode>,
    document.getElementById('root')
  );
}


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
