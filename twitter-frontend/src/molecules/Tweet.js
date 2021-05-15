function LikeBtn(props){
    const {tweet} = props
    const className = props.className ? props.className : "btn btn-primary" 
    
    return ( <button className={className}> {tweet.likes} Likes </button> )
}
  
export default function Tweet(props){
    const {tweet} = props

   
    const className = props.className ? props.className : "col-10 mx-auto col-md-6" 

    return (
    <div className={className}>
       <p> {tweet.id} - { tweet.content } </p>
       <LikeBtn tweet={tweet} className="btn btn-primary" />
    </div> ) 
} 
  