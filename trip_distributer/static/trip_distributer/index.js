

function trip_response(event , trip_id ){
    console.log(1)
    const element = event.target

    if (["accept","reject"].includes(element.id) ){
        console.log(2)
        console.log(trip_id)
        fetch("/add_user_to_trip" , {
            method: "POST",
            body: JSON.stringify({
                user_response : element.id,
                trip_id: trip_id 
            })
        })
        .then(response => response.json())
        .then(text => {
            if (element.id == "accept"){
            console.log(trip_id)
            trip_name = text["trip_name"];
            console.log(text)
            start_date = text["trip_start_date"]
            document.querySelector("#list_current_trip").innerHTML = `<li id="trip_name"><a href="/trip/${trip_id }">${ trip_name }</a> Start Date -> ${ start_date } </li>` + document.querySelector("#list_current_trip").innerHTML
            }
        })


        element.parentElement.remove()
        

    
    }


}