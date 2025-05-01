let images = ["https://content.paulreiffer.com/wp-content/uploads/2013/08/Fine-Art-Limited-Edition-Print-Wall-Corporate-Decoration-Interior-Design-Paul-Reiffer-Photographer-Photography-High-End-Landscape-Cityscape-Buy-Rock-Of-Ages-Bryce-Canyon.jpg", "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_675,q_75,w_1200/v1/clients/swat/TitleSlide_03eb7c9a-bac5-4fbe-a2a5-b85bb82a6349.jpg"]

function more(){
    document.getElementById("firstButtons").style.backgroundColor="#4189C0"
    document.getElementById("firstButtons").style.color="#FFFFFF"
    document.getElementById("firstButtons").style.border="2px solid #004326"
  if(document.getElementById("paraTwo").style.display != "flex"){
      document.getElementById("paraTwo").style.display = "flex"
      document.getElementById("firstButtons").innerHTML = "Less About Bryce Canyon"
  }else{
      document.getElementById("paraTwo").style.display = "none"
      document.getElementById("firstButtons").innerHTML = "More About Bryce Canyon"
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

function broken(){
    document.getElementById("bigTitle").innerHTML = "eao yBcnynCr"
    document.getElementById("first").innerHTML = "fancNr iw.ao tso a sisUedoy e soravhtaaeiorcd c tyenonkntota C ohi f.rlasn ofnfaytaeeahdmeyohii dn mhTaorhtgsro mttdfof al koe mem moprnr alkPuraairisBltarnlio. nhcon r kntedgI mhboy o"
    document.getElementById("second").innerHTML = "hn ecyuepc liatrsasTece sryokorohari hudfos e Tg e eintaxiigenpvkel r h tsaei nenpoTvrotosaa Tucdtam t dapogrsoahrsgny h eea"
    document.getElementById("extra").innerHTML = "p ernot cv chno u. cneetnmdems toBr s e iissyu eoyge tihcue s ietsnae aleLeyyoyw ra now ieoayd0 o o bhhl C ok nfmenaershahcalgvTln.li oo,ll hl,nioeis on n8lrghgsrrcew0 bf i oa slemant lu yamu manaW d n nifa doaoe5rdco nahydgrreln rgeyoeh i B tl hv ekknunbEi e rrfehre1oDeee nosnsbBbtu2oo.mstieattoh'csebu,f nk upsnuyaeoafmr aonae skbo cnmnolirbt de au.ymtr wrco nFpwc,ny.tB isT,yan creytCi aCcarlnch c1aaloohrreiyaiyoradnhrfzhzrosla e9o ea lHl nndtlrabt u2rps Aia roo t ro m , ieaSe efs khm rew,ami o ti rnrfsr n Tun edu.erimIr aeylhi"
}