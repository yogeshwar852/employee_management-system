function validateForm() {
    var empName = document.forms["myForm"]["emp_name"].value;
    var MobNO = document.forms["myForm"]["mob_no"].value;
    var phoneno = /^\d{10}$/;
    var ch=/[a-zA-Z]/;
    var inpmail =document.forms["myForm"]["email"];
    
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
   // /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
   // ^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$
    var i=0;
    //document.getElementById("email1").innerHTML = inpmail.value;
    if (empName == "") {
       // alert("Name must be filled out");
       document.getElementById("uname").innerHTML = "Required";
        //return false;
    }
    else{
        document.getElementById("uname").innerHTML = "";
        //return true;
        i++;
    }
    //var y = document.forms["myForm"]["mob_no"].value;
    if (MobNO == "") {
        //alert("Name must be filled out");
        //alert("Required field");
        document.getElementById("mob_no").innerHTML = "Required";
        //return false;
        //y.focus();    
    }
    else if (ch.test(MobNO)) {
        //alert("Enter 10 numbers only");
        document.getElementById("mob_no").innerHTML = "Charactor Not allowed";
        //return false;
    }
    else if (phoneno.test(MobNO)){
        if (MobNO.length == 10) {
            //alert("HVVDJHvsk");
            document.getElementById("mob_no").innerHTML = "";
            //return true;
            i++;
        }
        
    }
    else 
    {

        //alert("Charctor not allowed in number");
        document.getElementById("mob_no").innerHTML = "Enter valid number";
        //return false;
    }
    if  (inpmail.value == "")  {
         document.getElementById("email1").innerHTML = "Required";
        //return false;
    }
    else {
        if(inpmail.value.match(mailformat)) {
            //alert("Barobar");    //The pop up alert for a valid email address
            document.myForm.email.focus();
            document.getElementById("email1").innerHTML = "";
            //return true;
            i++;
        }
        else
        {
            alert("You have entered an invalid email address!");
            document.getElementById("email1").innerHTML = "Enter Valid email";
                //The pop up alert for an invalid email address
            document.myForm.email.focus();
            //return false;
        }

    }
    if (i!=3) {
        return false
    }
}