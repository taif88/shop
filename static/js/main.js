let categories = document.getElementById("cate")
let mega = document.getElementById("mega-menu")


categories.onclick = (e) => {
    if (mega.style.display === "none") {
        mega.style.display = "block"
    } else {
        mega.style.display = "none"
    }
}
