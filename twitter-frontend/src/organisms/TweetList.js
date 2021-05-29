import Tweet from '../molecules/Tweet'
import React, {useEffect, useState} from 'react'
import {tweetsList } from '../XHR/lookup'

 
export default function TweetList(props){
    const[tweetsInit, setTweetsInit] = useState([])
    const[tweets, setTweets] = useState([])

    let {newTweets, setNewTweets, username } = props

    const handleDidRetweet = (newTweet) => {
    
      setNewTweets([newTweet].concat(newTweets))
    
    }
    

    useEffect(() => {
      const finalLength = props.newTweets.length + tweetsInit.length
      
      // console.log(finalLength, tweets, tweetsInit)

      if ( finalLength > tweets.length){
        setTweets([...props.newTweets].concat(tweetsInit))
      }

    }, [props, tweetsInit, tweets])

    function getTweets(){
      tweetsList("GET", "tweets/", setTweetsInit, username)
    }
  
    useEffect(getTweets, [username])

    // console.log("nomal call")
    // console.log(tweets, "rendering tweets from tweet list")
    return (
      <>
        {
          tweets.map( (item, index) => <Tweet tweet={item} handleDidRetweet={handleDidRetweet} key={index}  className="my-5 py-5 border bg-white"/>)
        }
      </>
    );

  }



  