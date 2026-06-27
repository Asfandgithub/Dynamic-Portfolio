// ====================
// Dark Mode
// ====================

const themeBtn = document.getElementById("themeBtn");

themeBtn.onclick = function(){

    document.body.classList.toggle("dark");

};


// ====================
// Contact Form
// ====================

const form = document.getElementById("contactForm");

form.addEventListener("submit", function(event){

    event.preventDefault();

    alert("Your message has been sent successfully!");

    form.reset();

});


// ====================
// Welcome Message
// ====================

console.log("Portfolio Website Loaded Successfully");