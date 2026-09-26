but = document.getElementById('addcart')
urlprams = new URLSearchParams(window.location.search)
let id = urlprams.get('id')
but.onclick = () => {
    window.location.href = `/addcart?id=${id}`
}

let star = document.getElementById("wishlist")
window.onload = async () => {
    const prams = new URLSearchParams(window.location.search)
    await fetch(`/api/wishlist?id=${prams.get("id")}`)
        .then(re => re.json())
        .then(re => {
            console.log(re)
            if (re["inwishlist"]) {
                star.classList.remove("fa-regular")
                star.classList.add("fa-solid")
            }
        })
}
star.onclick = async () => {
    star.classList.remove("fa-regular")
    star.classList.add("fa-solid")
    let prams = new URLSearchParams('search')
    let pram = prams.get('id')
    let wishlistTmplate = { "wishlist": "True", "productid": id }
    const toServer = JSON.stringify(wishlistTmplate)
    try {
        const response = await fetch("api/wishlist", {
            method: "POST",
            headers: {
                "content-type": "application/json"
            },
            body: toServer
        })
        console.log(1)
    } catch (error) {
        console.error("Error sending wishlist request:", error);
    }
}
