contactError = document.getElementById("contact-error-tag");
contactError.style.display = "none";

function sendMessage() {

    let email = document.getElementById("email-input").value;
    let name = document.getElementById("name-input").value;
    let subject = document.getElementById("subject-input").value;
    let message = document.getElementById("message-area").value;

    emailValidity = isValidEmail(email);

    if(email && name && subject && message && emailValidity) {

        contactError.style.display = "none";

        $.ajax({
            type: "POST",
            contentType: 'application/json',
            url: "/contact",
            data: JSON.stringify({
                'email': email,
                'name': name,
                'subject': subject,
                'message': message
            }),
            success: function(result) {
                document.getElementById("email-input").value = "";
                document.getElementById("name-input").value = "";
                document.getElementById("subject-input").value = "";
                document.getElementById("message-area").value = "";

                alert('Message sent successfully.');
            }
        });

    } else if(email && name && subject && message) { // if email is invalid

        contactError.style.display = "block";
        contactError.innerHTML = "Please enter a valid email address.";

    } else { // if fields have been left empty but email is valid

        contactError.style.display = "block";
        contactError.innerHTML = "You may have left one or more fields empty.";
        
    }

}

function isValidEmail(address) { // gets validity of email address using regex

    let reg = /\S+@\S+\.\S+/;

    return reg.test(address);

}