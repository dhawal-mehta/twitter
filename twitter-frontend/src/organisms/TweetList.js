import Tweet from '../molecules/Tweet'
import React, {useEffect, useState} from 'react'
import {tweetsList, tweetCreate } from '../XHR/lookup'

 
function TweetList(props){
    const[tweetsInit, setTweetsInit] = useState([])
    const[tweets, setTweets] = useState([])

    let {newTweets, setNewTweets } = props

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
      tweetsList("GET", "tweets/", setTweetsInit)
    }
  
    useEffect(getTweets, [])

    // console.log("nomal call")
    console.log(tweets, "rendering tweets from tweet list")
    return (
      <>
        {
          tweets.map( (item, index) => <Tweet tweet={item} handleDidRetweet={handleDidRetweet} key={index}  className="my-5 py-5 border bg-white"/>)
        }
      </>
    );
  
  }



export function TweetsComponent(props){
    
    const [newTweets, setNewTweets] = useState([])

    const textAreaRef = React.createRef()
    
    function createTweetCallBck(response){
      // console.log(response, "response form tweetComponent")
      setNewTweets([response].concat(newTweets))
      // console.log(newTweets, "after insert")
    }

    const handleSubmit = (e) => {

        e.preventDefault()

        tweetCreate('POST', "tweets/create/",createTweetCallBck , {content:textAreaRef.current.value, likes:0})

        textAreaRef.current.value = ''

    }

    
    return <div className={props.className}>
            <div className="col-12 mb-3 mt-3">

              <form onSubmit={handleSubmit} >
                  <textarea ref={textAreaRef} required={true} className='form-control' name="tweet"></textarea>
                  <button type='submit' className="btn btn-primary my-3">Tweet</button>
              </form>
              
              <TweetList newTweets={newTweets}  setNewTweets={setNewTweets} />

            </div>
          </div>

}