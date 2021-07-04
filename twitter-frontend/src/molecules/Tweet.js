import React, {useState, useEffect} from 'react'
import RetweetBtn from "../atoms/RetweetBtn"
import LikeBtn from "../atoms/LikeBtn"
import ViewBtn from "../atoms/ViewBtn"


export function ParentTweet(props){
    const {tweet, handleDidRetweet} = props
    
    return tweet.parent ? <div className='row mb-3'>
      <div className='col-11 mx-auto p-3 border rounded'>
        <p className="mb-0 text-muted small">Retweet</p>
        <Tweet isRetweet tweet={ tweet.parent } handleDidRetweet={handleDidRetweet} hideButtons={true} />       
      </div>
    </div> : null
}

  
export default function Tweet(props){
    const {tweet, handleDidRetweet} = props

    // console.log( props.hideButtons )

    const className = props.className ? props.className : "col-10 mx-auto col-md-6" 

    return (
    <div className={className}>
      {/* { console.log(tweet , "###### ") } */}
        { tweet.parent && 
          <>
            Retweet by {tweet.user}
          </> 
        }
        <div>
          {/* <strong>
            { tweet.user.first_name } {" "}
            { tweet.user.last_name } {" "}
          </strong> */}
          
          <span className="text-muted"> @{ tweet.user.username }</span>

        </div>
        <div >
            <p> { tweet.content } </p>
            {/* { tweet.parent && tweet.parent.content &&
              <ParentTweet tweet={tweet} handleDidRetweet={handleDidRetweet}/>
            } */}

          { props.hideButtons !== true && 
              <>
              <LikeBtn tweet={tweet} className="btn btn-primary" />
              <RetweetBtn tweet={tweet} handleDidRetweet={handleDidRetweet} className="btn btn-primary ml-5" />
              </>
          }
          <ViewBtn tweet={tweet} className="btn btn-outline-primary ml-5" />
        </div>

    </div> ) 
} 
  