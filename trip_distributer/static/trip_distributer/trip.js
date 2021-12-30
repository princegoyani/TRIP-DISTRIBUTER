function endtrip(event , trip_id){

    if (confirm("ARE YOU SURE TO END TRIP !") == true){
        location.reload()
        fetch("/endtrip" , {
            method:"POST",
            body: JSON.stringify({
                trip_id:trip_id
            })
        })
    }
}

function delete_trip(event, trip_id ){
    if (confirm("ARE YOU SURE TO DELETE TRIP !") == true){
    console.log(trip_id)
    fetch("/delete_trip" , {
        method:"POST",
        body: JSON.stringify({
            trip_id: trip_id
        })
    })
    window.location.href = "/"
    }
}



function remove_spend(event , spending_id){
    const element = event.target
    if (element.id == "remove_spend"){

    fetch("/remove_spend" , {
        method:"POST",
        body: JSON.stringify({
            spend_id:spending_id
        })
    })

    element.parentElement.remove()
    location.reload()
    location.reload()
}

}



function add_spend_(event , trip_id){
    event.preventDefault();

    desciption = document.querySelector('#form_spend').querySelector("#spend_descriptions").value
    spend = document.querySelector('#form_spend').querySelector("#spend_amount").value

    fetch("/spend" , {
        method:"POST",
        body: JSON.stringify({
            trip_id: trip_id,
            desciption : desciption,
            spend : spend
        })
    })
    .then(response => response.json())
    .then(body => { 
        username = body["user"]
        date_time = body["date_time"]
        console.log(body)

        document.querySelector("#spend_history").innerHTML = `<li> ${username} has spend ${spend} on ${desciption}      ${date_time}` + document.querySelector("#spend_history").innerHTML
    })
    console.log("spend_Added")
    document.querySelector('#form_spend').querySelector("#spend_descriptions").value = ""
    document.querySelector('#form_spend').querySelector("#spend_amount").value =""
    location.reload()

}