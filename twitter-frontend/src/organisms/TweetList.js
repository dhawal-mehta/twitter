import Tweet from '../molecules/Tweet'
import React, {useEffect, useState} from 'react'
import { tweetsList } from '../XHR/lookup'

 
export default function TweetList(props){
    const[tweetsInit, setTweetsInit] = useState([])
    const[tweets, setTweets] = useState([])

    const [nextUrl, setNextUrl] = useState(null)
    // const [previousUrl, setPreviousUrl] = useState(null)

    let {newTweets, setNewTweets, username } = props
    console.log(newTweets, setNewTweets, username ,"**************8")


    const handleDidRetweet = (newTweet) => {
    
      setNewTweets([newTweet].concat(newTweets))
    
    }

    useEffect(() => {
      console.log("in use Effect ",props.newTweets,  tweetsInit.length)

      let finalLength = props.newTweets.length  + tweetsInit.length
      // console.log("in use Effect ", finalLength,props.newTweets.length, props.newTweets,  tweetsInit.length)
      console.log("in use Effect ", tweetsInit)

      if ( finalLength > tweets.length){
        console.log(" setting tweets ")
        setTweets( [...props.newTweets].concat(tweetsInit) )
      }

    }, [props, tweetsInit, tweets])


    // function tweetListCallback(xhrResponse){
    //   console.log("******",xhrResponse, ...xhrResponse["results"]  )
    //   setTweets( [...tweets].concat(...xhrResponse.results) ) 
    //   setNextUrl( xhrResponse.next )
    //   console.log("here are tweets" ,tweets )
    // }
    
    function loadTweetListCallback(xhrResponse){
      console.log("#####")
      console.log(xhrResponse , xhrResponse["results"] )
      // setTweets([...tweets].concat(xhrResponse.results) )
      // setNextUrl( xhrResponse.next )    
      // console.log(tweets)
    }
  

    useEffect(() => {
      tweetsList("GET", "tweets/", setTweetsInit, username)
    }, [username])

    const handleLoadNext = (event) => {
      event.preventDefault()
      if (nextUrl !== null){ 
        tweetsList( "GET", nextUrl.substring(nextUrl.indexOf("api/") +4), loadTweetListCallback, username )
      }
    }

    return (
      <>
        { console.log("tweets", tweets) }
        {
          
          tweets.map( (item, index) => <Tweet tweet={item} handleDidRetweet={handleDidRetweet} key={index}  className="my-5 py-5 border bg-white" />)
        }
 
        {/* { nextUrl !== null && <button onClick={ handleLoadNext } className="btn btn-outline-primary">Next</button> }       */}
      </>
    );

  }
