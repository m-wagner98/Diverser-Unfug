function checkPass( password ) { 
    var total = 0;
    var charlist   =  "abcdefghijklmnopqrstuvwxyz" ;
    for ( var i = 0; i < password.length; i++) {
        var countone =   password.charAt (i);
        var counttwo = ( charlist.indexOf(countone)); //  0 <= index <= 25
        counttwo++;  // also eig 1 <= index <= 26
        total *= 17;  
        total += counttwo;  
    }
        if (  total == 248410397744610 ) { 
            setTimeout  ("location.replace('index.php?password="+password+  "' )  ;  ", 0) } else  {  alert  ("Sorry, but the password was incorrect." ) ; 
        } 
    }