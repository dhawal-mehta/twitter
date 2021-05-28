import React, {useState} from 'react'
import { tweetLike } from "../XHR/lookup";

// function handleLikeClick(tweet, setLikes){
    // const { type } = props
    // console.log(likes)
    // function tweetLikeCallback(){
    // setLikes(tweet.likes + 1)
    // }
    // const data = {"action":"like", "id":tweet.id}
    // tweetLike("POST", "/api/tweets/action/", tweetLikeCallback, data)
    // console.log( tweet.likes )
// }

// function handleRetweetClick(tweet){

//     console.log("test", tweet)
// }

function LikeBtn(props){
    let {tweet} = props

    const [like, setLike] = useState(tweet.likes?tweet.likes:0)
    
    // console.log("creating like button for ", tweet,tweet.likes ,like)
    // const [clicked, setcliked] = useState(tweet.userLike === true? true :false)

    const className = props.className ? props.className : "btn btn-primary" 
    
    const handleLikeClick = () => {
            const data = {"action": "like", "id": tweet.id}

            function tweetLikeCallback (response){
                tweet.likes = response.likes                
                setLike( response.likes )
            }
            
            tweetLike("POST", "tweets/action/", tweetLikeCallback, data)
    }

    return ( <button className={className} onClick={ handleLikeClick } > { tweet.likes } likes </button> )
}

function RetweetBtn(props){

    const { tweet, handleDidRetweet } = props
    const className = props.className ? props.className : "btn btn-primary" 
    
    function handleRetweetClick(){
        const data = {"action": "retweet", "id": tweet.id}

        function retweetCallback (response){
            // tweet.likes = response.likes                
            // setLike( response.likes )
            handleDidRetweet(response)
            // console.log(response, "from handle RetweetClick", handleDidRetweet)
        }
          
        tweetLike("POST", "tweets/action/", retweetCallback, data) 
    }
    


    return ( <button className={className} onClick={ handleRetweetClick }> Retweet </button> )
}

export function ParentTweet(props){
    const {tweet, handleDidRetweet} = props
    
    return tweet.parent ? <div className='row mb-3'>
      <div className='col-11 mx-auto p-3 border rounded'>
        <p className="mb-0 text-muted small">Retweet</p>
        <Tweet tweet={ tweet.parent } handleDidRetweet={handleDidRetweet} hideButtons={true} />       
      </div>
    </div> : null
}

  
export default function Tweet(props){
    const {tweet, handleDidRetweet} = props
    // console.log( props.hideButtons )

    const className = props.className ? props.className : "col-10 mx-auto col-md-6" 

    return (
    <div className={className}>
        
        <div>           
            <p> {tweet.id} - { tweet.content } </p>
            <ParentTweet tweet={tweet} handleDidRetweet={handleDidRetweet}/>
        </div>
       
       { props.hideButtons !== true && 
        <>
            <LikeBtn tweet={tweet} className="btn btn-primary" />
            <RetweetBtn tweet={tweet} handleDidRetweet={handleDidRetweet} className="btn btn-primary ml-5" />
       </>}

    </div> ) 
} 
  