 import Tweet from '../molecules/Tweet'
 import React, {useEffect, useState} from 'react'

function loadTweets(tweetsCbk){
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    const url = "http://localhost:8000/api/tweets/"
    const responseType = "json"
  
    xhr.responseType = responseType
    xhr.open(method, url)
   
    xhr.onload = function(){
      const res = xhr.response
      // console.log(res) 
      tweetsCbk(res)
      // return  xhr.response
    }
    
    xhr.send()
  } 
  
  
export default function TweetList(props){
    const[tweets, setTweets] = useState([])
  
    const getTweets =  () => {
      // laodTweets()
      loadTweets(setTweets)
      // setTweets(tweetItems)
    }
  
    useEffect(getTweets, [])
  
    return (
      <>
        {
          tweets.map( (item, index) => <Tweet tweet={item} key={index} className="my-5 py-5 border bg-white"/>)
        }
      </>
    );
  
  }