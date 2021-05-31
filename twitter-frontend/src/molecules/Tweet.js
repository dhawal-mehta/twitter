import React, {useState} from 'react'
import RetweetBtn from "../atoms/RetweetBtn"
import LikeBtn from "../atoms/LikeBtn"


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
              { tweet.parent && tweet.parent.content &&
                <ParentTweet tweet={tweet} handleDidRetweet={handleDidRetweet}/>
              }
      </div>
       { props.hideButtons !== true && 
        <>
            <LikeBtn tweet={tweet} className="btn btn-primary" />
            <RetweetBtn tweet={tweet} handleDidRetweet={handleDidRetweet} className="btn btn-primary ml-5" />
       </> }

    </div> ) 
} 
  