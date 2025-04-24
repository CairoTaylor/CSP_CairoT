function more(){
  if(document.getElementById("extra").style.display != "flex"){
      document.getElementById("extra").style.display = "flex"
  document.getElementById("shw").innerHTML = "show less"
  }else{
      document.getElementById("extra").style.display = "none"
  document.getElementById("shw").innerHTML = "show more"
  }
}