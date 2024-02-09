var button = document.getElementById("switch");
var html = document.querySelector("html");

value = localStorage.getItem("selectedTheme");

if (value == "dark"){
    dark();
} if (value == "light"){
    light();
} else {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        dark();
    } else {
        light();
    }
}

button.onclick = function(){
    if (html.getAttribute('data-theme') == "dark") {
        light();
    } else {
        dark();
    }
}

function dark(){
    button.classList.replace("fi-rr-moon", "fi-rr-brightness");
    localStorage.setItem("selectedTheme", "dark");
    html.setAttribute('data-theme', "dark");
}

function light(){
    button.classList.replace("fi-rr-brightness", "fi-rr-moon");
    localStorage.setItem("selectedTheme", "light");
    html.setAttribute('data-theme', "light");
}