// so lange, bis checkSumme wieder bei 0 is
var checkSumme = 248410397744610;
var count2 = 0;
var pwArray = new Array();

while(checkSumme > 0){
    count2 = checkSumme % 17;
    checkSumme -= count2;
    checkSumme /= 17;
    count2 --; //index im Alphabet
    var buchstabe = String.fromCharCode(97 + count2)// 'a' entspricht 97
    pwArray.push(buchstabe);
    count2 = 0; //reset
}

//Fertiges Passwort auslesen
pwArray = pwArray.reverse();
var passwort = pwArray.join("");
console.log(passwort);