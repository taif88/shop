but = document.getElementById('addcart')
urlprams = new URLSearchParams(window.location.search)
let id = urlprams.get('id')
but.onclick = () => {
    window.location.href = `/addcart?id=${id}`
}
