import React, {useState} from 'react'
import { tweetCreate} from '../XHR/lookup'

import TweetList from '../organisms/TweetList'

export  function Homepage(props){

    const [newTweets, setNewTweets] = useState([])

    const canTweet = props.canTweet === "false" ? false : true
    
    // console.log(canTweet, props.canTweet)

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
              { canTweet &&
                <form onSubmit={handleSubmit} >
                    <textarea ref={textAreaRef} required={true} className='form-control' name="tweet"></textarea>
                    <button type='submit' className="btn btn-primary my-3">Tweet</button>
                </form>
              } 
              <TweetList newTweets={newTweets}  setNewTweets={setNewTweets} {...props} />
            </div>
          </div>
}

