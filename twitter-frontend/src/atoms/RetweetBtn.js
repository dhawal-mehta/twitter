import React, {useState} from 'react'
import { tweetRetweet } from "../XHR/lookup";

export default function RetweetBtn(props){

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
          
        tweetRetweet("POST", "tweets/action/", retweetCallback, data) 
    }
    


    return ( <button className={className} onClick={ handleRetweetClick }> Retweet </button> )
}