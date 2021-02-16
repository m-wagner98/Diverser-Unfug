date = new Date();
year = date.getYear();
pass = 1337;
  
for(i = 1; i <= year; i++) {
  	pass += year * i * year;
}
		
if(pass == 318338237039211050000) {
    alert("Good job!");
    window.location.href = "http://challenges.enigmagroup.org/js/12/" + year + ".php";
} else {
    alert("Sorry, did you fail already?!");
    window.location.href = "http://www.enigmagroup.org/pages/challenges/";
}