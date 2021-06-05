import React, {useEffect, useState} from 'react'
import { tweetDetail } from '../XHR/lookup'
import Tweet from '../molecules/Tweet'

export default function TweetsDetailComponent(props){
    console.log(" in detail ")
    const {tweetId} = props
    const [tweet, setTweet] = useState(null)
    const [didlookup, setDidLookup] = useState(false)
  
    const handleBackendLookup = (response)=> {
      setTweet(response)
      // console.log(response, "from Tweet Detail")
    }
  
    useEffect(() => {
      if (didlookup === false){
        tweetDetail('GET', 'tweets/',handleBackendLookup, tweetId)
        setDidLookup(true)  
      }
    }, [tweetId, didlookup, setDidLookup])
  
    return tweet === null ? null : <Tweet tweet={tweet} className={props.className} />
  }