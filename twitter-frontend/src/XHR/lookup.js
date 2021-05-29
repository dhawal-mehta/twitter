function lookup(apimethod, endpoint,callBck ,data=null){
    let jsonData 
    // console.log(data, "data")
    if (data){
        jsonData = JSON.stringify(data)
    }

    const xhr = new XMLHttpRequest()
    const method = apimethod  
    const url = `http://localhost:8000/api/${endpoint}`
    xhr.responseType = "json"   
    xhr.open(method, url)    
    

    if (method === "POST"){
        xhr.setRequestHeader("content-type", "application/json")
        xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")  
        const csrftoken = getCookie("csrftoken")        
        // console.log(csrftoken) 
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
    }



    xhr.onload = function(){
      const res = xhr.response

      if (xhr.status === 200){
        //   console.log("xhr response", xhr.response)
          callBck(xhr.response)
      }
      else if(xhr.status === 201){
        // console.log("xhr response", xhr.response)
        callBck(xhr.response)
      }
      else{
          alert("An error occured")
      }

    }

    xhr.send(jsonData)
} 


export function tweetsList(apimethod, endpoint, tweetsCbk, username){
    
    if (username){
        endpoint += `?username=${username}`
    }
        
    lookup(apimethod, endpoint, tweetsCbk)
}

export function tweetDetail(apimethod, endpoint, tweetsCbk, tweetId){
    
    // if (tweetId){
    //     endpoint += `${tweetId}/`
    // }
        
    lookup(apimethod, endpoint + `${tweetId}/`, tweetsCbk)
}

export function tweetCreate(apimethod, endpoint, tweetsCbk, data){
    lookup(apimethod, endpoint, tweetsCbk, data)
}

export function tweetLike(apimethod, endpoint, tweetLikeCbk, data){
    lookup(apimethod, endpoint, tweetLikeCbk, data)
}

export function tweetRetweet(apimethod, endpoint, tweetLikeCbk, data){
    lookup(apimethod, endpoint, tweetLikeCbk, data)
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}