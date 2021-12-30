
var user_toadd_list= []
document.addEventListener("DOMContentLoaded" , () => {
          
        console.log("user_toadd");
        if (document.querySelector("#add_user")){            
            
            document.querySelector("#add_user").addEventListener("submit" , (event) => {

                document.querySelector("#add_user").querySelector("#alert").innerHTML = ""
                document.querySelector("#add_user").querySelector("#alert").style.display = "none"
                    event.preventDefault()
                
                    user_toadd = document.querySelector("#user_toadd").value 
                    if ( !(user_toadd_list.includes(user_toadd))) {
                    console.log(user_toadd)

                    fetch("add_user", {
                        method : "post",
                        body : JSON.stringify({
                            user_toadd : user_toadd 
                        })
                    })
                    .then(response => response.json())
                    .then( request => {
                        console.log(request["post"])
                        if (request["post"] == "accepted"){
                            console.log("accepted")
                            document.querySelector("#user_toadd").value =  ""
                            user_toadd_list.push(user_toadd)
                            console.log(user_toadd_list)
                            add_user_inlist(user_toadd)
                        }
                        if (request["post"] == "no_such_user"){
                            console.log("Rejected")
                            document.querySelector("#add_user").querySelector("#alert").style.display = "Block"
                            document.querySelector("#add_user").querySelector("#alert").innerHTML = "NO SUCH USER"
                        }

                    })
                }
                else { 
                    document.querySelector("#add_user").querySelector("#alert").style.display = "Block"
                    document.querySelector("#add_user").querySelector("#alert").innerHTML = "ALREADY ADDED"
                }

                
            })}
         
            if (document.querySelector("#form_add_trip")){
                document.querySelector("#form_add_trip").addEventListener("submit" , (event)=>{
                    
                    trip_name = document.querySelector("#form_add_trip").querySelector("#trip_name").value

                    fetch("save_trip" , {
                        method : "POST",
                        body : JSON.stringify({
                            trip_name: trip_name,
                            user_torequest : user_toadd_list
                        })
                    })
                    

                })
            }



    })


function add_user_inlist(user){
    console.log(document.querySelector("#user_list"))
    document.querySelector("#user_tobeadded").querySelector("#user_list").innerHTML += `<div id="div_for_auser"> <li id="a_user_toadd">${user} <button id="remove_user" onclick= " return remove_user (event , '${user}') " >REMOVE</button></li></div>`
}

function remove_user(event , username ){
    console.log(`here`   )
    for (var i  = 0 ; i < user_toadd_list.length ; i++){
        console.log(user_toadd_list[i])
        if( user_toadd_list[i] == username ){
            console.log("removing")
            user_toadd_list.splice(i , 1);
            const element = event.target
            element.parentElement.remove()
        }
    }
    
}
