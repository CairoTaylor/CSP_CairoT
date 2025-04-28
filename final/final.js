function more(){
    document.getElementById("firstButtons").style.backgroundColor="#4189C0"
    document.getElementById("firstButtons").style.color="#FFFFFF"
    document.getElementById("firstButtons").style.border="2px solid #004326"
  if(document.getElementById("paraTwo").style.display != "flex"){
      document.getElementById("paraTwo").style.display = "flex"
      document.getElementById("firstButton").innerHTML = "Less About Bryce Canyon"
  }else{
      document.getElementById("paraTwo").style.display = "none"
      document.getElementById("firstButton").innerHTML = "More About Bryce Canyon"
  }
}

function highlight(){
    document.getElementById("firstButtons").style.backgroundColor="#AA5939"
    document.getElementById("firstButtons").style.color="#FFD1AA"
    document.getElementById("firstButtons").style.border="2px solid #611C00"
}

function normal(){
    document.getElementById("firstButtons").style.backgroundColor="#FFD1AA"
    document.getElementById("firstButtons").style.color="#AA5939"
    document.getElementById("firstButtons").style.border="2px solid #611C00"
}