var nav = document.querySelector("#nav");
const open = document.querySelector("#open");
var close = document.querySelector("#close");

open.addEventListener("click", () => {
    nav.classList.add("visible")
})

close.addEventListener("click", () =>{
    nav.classList.remove("visible")
})