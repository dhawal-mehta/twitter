import Tweet from '../molecules/Tweet'
import React, {useEffect, useState} from 'react'
import {tweetsList, tweetCreate } from '../XHR/lookup'


  
function TweetList(props){
    const[tweetsInit, setTweetsInit] = useState([])
    const[tweets, setTweets] = useState([])

    // console.log(props.newTweet, "new Tweet from props")

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
    return (
      <>
        {
          tweets.map( (item, index) => <Tweet tweet={item} key={index} className="my-5 py-5 border bg-white"/>)
        }
      </>
    );
  
  }

export function TweetsComponent(props){
    
    const [newTweets, setNewTweet] = useState([])

    const textAreaRef = React.createRef()

    const handleSubmit = (e) => {

        e.preventDefault()

        function callBck(response){
          setNewTweet([response].concat(newTweets))
        }

        tweetCreate('POST', "tweets/create/",callBck  ,{content:textAreaRef.current.value})

        textAreaRef.current.value = ''

    }
    
    return <div className={props.className}>
            <div className="col-12 mb-3 mt-3">

              <form onSubmit={handleSubmit} >
                  <textarea ref={textAreaRef} required={true} className='form-control' name="tweet"></textarea>
                  <button type='submit' className="btn btn-primary my-3">Tweet</button>
              </form>
              
              <TweetList newTweets={newTweets}/>

            </div>
          </div>

}