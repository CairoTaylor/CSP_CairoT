function more(){
    if(document.getElementById("paraTwo").style.display != "flex"){
        document.getElementById("paraTwo").style.display = "flex"
    document.getElementById("firstButton").innerHTML = "Less About Bryce Canyon"
    }else{
        document.getElementById("paraTwo").style.display = "none"
    document.getElementById("firstButton").innerHTML = "More About Bryce Canyon"
    }
  }