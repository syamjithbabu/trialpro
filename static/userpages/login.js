function login(){
    var username=document.getElementById("username1").value
    var passw=document.getElementById("pw").value
    
    if(username==""){
        document.getElementById("un1").innerHTML="Please Enter Username"
        document.getElementById("un1").style.color="red"
        document.getElementById("username1").style.border="1px solid red"
        return false
    }
    else{
        document.getElementById("un1").innerHTML=""
        document.getElementById("un1").style.color=""
        document.getElementById("username1").style.border=""
    }

    if(passw==""){
        document.getElementById("pw1").innerHTML="Please Enter Password"
        document.getElementById("pw1").style.color="red"
        document.getElementById("pw").style.border="1px solid red"
        return false
    }
    else{
        document.getElementById("pw1").innerHTML=""
        document.getElementById("pw1").style.color=""
        document.getElementById("pw").style.border=""
    }
}