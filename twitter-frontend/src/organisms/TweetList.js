import Tweet from '../molecules/Tweet'
import React, {useEffect, useState} from 'react'
import { tweetsList } from '../XHR/lookup'

 
export default function TweetList(props){
    const[tweetsInit, setTweetsInit] = useState([])
    const[tweets, setTweets] = useState([])
    
    const [nextUrl, setNextUrl] = useState(null)
    const [previousUrl, setPreviousUrl] = useState(null)

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

    function tweetListCallback(xhrResponse){
      // console.log(xhrResponse )
      setTweets( xhrResponse.results )
      setNextUrl( xhrResponse.next )
      setPreviousUrl( xhrResponse.previous )

    }
  
    useEffect(() => {
      
      tweetsList("GET", "tweets/", tweetListCallback, username)
      
    }, [username])

    
    return (
      <>
        {
          tweets.map( (item, index) => <Tweet tweet={item} handleDidRetweet={handleDidRetweet} key={index}  className="my-5 py-5 border bg-white"/>)
        }

        { nextUrl !== null && <button class="btn btn-outline-primary">Next</button> }
      </>
    );

  }



  