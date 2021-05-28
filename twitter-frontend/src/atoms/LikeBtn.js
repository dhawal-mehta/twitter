import React, {useState} from 'react'
import { tweetLike} from "../XHR/lookup";

export default function LikeBtn(props){
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
