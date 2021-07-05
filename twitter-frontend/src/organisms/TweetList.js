import Tweet from '../molecules/Tweet'
import React, {useEffect, useState} from 'react'
import {tweetsList } from '../XHR/lookup'

 
export default function TweetList(props){
    const[tweetsInit, setTweetsInit] = useState([])
    const [nextUrl, setNextUrl] = useState(null)
    const[tweets, setTweets] = useState([])

    let {newTweets, setNewTweets, username } = props

    const handleDidRetweet = (newTweet) => {
      setNewTweets([newTweet].concat(newTweets))
    }
    
    useEffect(() => {
      const finalLength = props.newTweets.length + tweetsInit.length
      if ( finalLength > tweets.length){
        setTweets([...props.newTweets].concat(tweetsInit))
      }
    }, [props, tweetsInit, tweets])

    function setTweetsInitCallback(response){
      setTweetsInit(response.results)
      setNextUrl(response.next)
    }

    function setTweetsCallback(response){
      const newTweets = [...tweets].concat(response.results)
      setTweetsInit(newTweets)
      setTweets(newTweets)
      setNextUrl(response.next)
    }
  
    useEffect(()=>{
      tweetsList("GET", "tweets/", setTweetsInitCallback, username)
    }, [username])

    function handleLoadMore(e){
      e.preventDefault()
      if (nextUrl !== null){
        tweetsList("GET", nextUrl.substring(nextUrl.indexOf("api/") + 4) ,setTweetsCallback, username)
      }
    }
    return (
      <>
        {
          tweets.map( (item, index) => <Tweet tweet={item} handleDidRetweet={handleDidRetweet} key={index}  className="my-5 py-5 border bg-white"/>)
        }
        {
          nextUrl !== null && 
          <button onClick={handleLoadMore} className="btn btn-outline-primary">Load More</button>
        }
      </>
    );

  }



  