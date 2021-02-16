var yearFull = 0;
pass = 1337;
var found = false;
while (!found) {
    //console.log(yearFull);
    pass = 1337;
    var year = new Date(yearFull, 11, 17).getYear();
    console.log(year);
    for (i = 1; i <= year; i++) {
        pass += year * i * year;
    }
    if(pass == 318338237039211050000) {
        console.log(`Year: ${year}`); //158847
        console.log(`YearFull: ${yearFull}`); //160747
        console.log(pass);
        found = true;
    }
    yearFull += 1;
}
// 404 page not found