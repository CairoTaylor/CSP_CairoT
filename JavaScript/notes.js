let images = ["https://media.tenor.com/vgJ_YNS41-IAAAAM/minecraft-movie-minecraft.gif", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNJhiHod_x1xBtLzU20Bb1dt9nAAaySrE28A&s"]
document=notes.html
function hello(){
    document.getElementById("title").style.color="blue"
    document.getElementById("title").innerHTML="I... am STEVE"
    return "I... am STEVE"
}

function change(){
    document.getElementById("image").style.height="500px"
    document.getElementById("image").src= images [count]
    if(count === 2){
        count = 0
    }else{
        count += 1
    }
}

function highlight(){
    document.getElementById("btn").style.backgroundColor="orange"
    document.getElementById("btn").style.color="white"    
}

function normal(){
    document.getElementById("btn").style.backgroundColor="lightGray"
    document.getElementById("btn").style.color="black"    
}

function show(){
    document.getElementById("image").style.display
}

pop();{
    window.alert("Genuinley don't touch it")
}

function hello(){
    let name = window.prompt("What is your name fool")
    document.getElementById("title").innerHTML = "hello " + name
}

function more(){
    if(document.getElementById("extra").style.display != "flex"){
        document.getElementById("extra").style.display = "flex"
    document.getElementById("shw").innerHTML = "show less"
    }else{
        document.getElementById("extra").style.display = "none"
    document.getElementById("shw").innerHTML = "show more"
    }
}