import React, {useState} from 'react'
import { tweetDetail } from "../XHR/lookup";

export default function ViewBtn(props){

    const { tweet } = props
    const className = props.className ? props.className : "btn btn-primary" 
    
    function handleViewClick(e){
        e.preventDefault()
        window.location.href=`/${tweet.id}`
    }
    
    return ( <button className={className} onClick={handleViewClick}> View </button> )
}