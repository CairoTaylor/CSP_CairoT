let images = ["https://content.paulreiffer.com/wp-content/uploads/2013/08/Fine-Art-Limited-Edition-Print-Wall-Corporate-Decoration-Interior-Design-Paul-Reiffer-Photographer-Photography-High-End-Landscape-Cityscape-Buy-Rock-Of-Ages-Bryce-Canyon.jpg", "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_675,q_75,w_1200/v1/clients/swat/TitleSlide_03eb7c9a-bac5-4fbe-a2a5-b85bb82a6349.jpg"]

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

function swpi(){
    document.getElementById("topImage").src="https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_675,q_75,w_1200/v1/clients/swat/TitleSlide_03eb7c9a-bac5-4fbe-a2a5-b85bb82a6349.jpg"
}

function swip(){
    document.getElementById("topImage").src="https://content.paulreiffer.com/wp-content/uploads/2013/08/Fine-Art-Limited-Edition-Print-Wall-Corporate-Decoration-Interior-Design-Paul-Reiffer-Photographer-Photography-High-End-Landscape-Cityscape-Buy-Rock-Of-Ages-Bryce-Canyon.jpg"
}