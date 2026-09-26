let data = null
js = (result) => result.json()
fetch('/api/explore')
    .then(js)
    .then((re) => {
        data = re
        urlprams = new URLSearchParams(window.location.search)
        const search = urlprams.get('search')
        const cat = urlprams.get('category')
        console.log(data)
        if (search) {
            Object.values(data).filter((ele) => {
                return ele['productcat'] === cat && ele['productname'].toUpperCase().includes(search.toUpperCase());
            }).forEach((ele) => {
                let element = document.createElement('div')
                element.classList.add('product')
                element.innerHTML = `<img src="/static/proim.jpg" alt="">
                    <h4 class="product-title">${ele["productname"]}</h4>
                    <p>${ele["productdis"]}</p>
                    <p>${ele["productpri"]}$</p>
                    <a href="/product?id=${ele["productid"]}">more</a>`
                const con = document.getElementById('s')
                con.appendChild(element)
            })
        } else if (cat) {
            Object.values(data).filter((ele) => {
                return ele['productcat'] === cat;
            }).forEach((ele) => {
                let element = document.createElement('div')
                element.classList.add('product')
                element.innerHTML = `<img src="/static/proim.jpg" alt="">
                        <h4 class="product-title">${ele["productname"]}</h4>
                        <p>${ele["productdis"]}</p>
                        <p>${ele["productpri"]}$</p>
                        <a href="/product?id=${ele["productid"]}">more</a>`
                const con = document.getElementById('s')
                con.appendChild(element)
            })
        } else {
            Object.values(data).forEach((ele) => {
                let element = document.createElement('div')
                element.classList.add('product')
                element.innerHTML = `<img src="/static/proim.jpg" alt="">
                        <h4 class="product-title">${ele["productname"]}</h4>
                        <p>${ele["productdis"]}</p>
                        <p>${ele["productpri"]}$</p>
                        <a href="/product?id=${ele["productid"]}">more</a>`
                const con = document.getElementById('s')
                con.appendChild(element)
            })
        }

    })
    .catch((re) => console.error('error p'))
let cate = []
data = null
fetch('/api/main')
    .then(js)
    .then((re) => {
        data = re
        Object.values(data).forEach((ele) => {
            if (!cate.includes(ele['productcat'])) {
                cate.push(ele['productcat'])
                const con = document.getElementById('content')
                const div = document.createElement("div")
                div.classList.add('category')
                const cat = con.appendChild(div)
                cat.innerHTML = `<h3>${ele['productcat']}</h3>
            <a href="/explore?category=${ele['productcat']}">more</a>
            <div class="category-content" id=${ele['productcat']}></div>`
            }
        })
    }).catch((ele) => {
        console.error("cata")
    })

data = null
js = (result) => result.json()
fetch('/api/main')
    .then(js)
    .then((re) => {
        data = re
        for (let i = 0; i < cate.length; i++) {
            Object.values(data).filter((ele) => {
                return ele.productcat === cate[i]
            }).forEach((ele) => {
                const cat = document.getElementById(cate[i])
                const div = document.createElement("div")
                div.classList.add('product')
                const pro = cat.appendChild(div)
                pro.innerHTML = `<img src="/static/proim.jpg" alt="">
                        <h4 class="product-title">${ele["productname"]}</h4>
                        <p>${ele["productdis"]}</p>
                        <p>${ele["productpri"]}$</p>
                        <a href="/product?id=${ele["productid"]}">more</a>`

            })

        }
    })
    .catch((re) => console.error('error p'))



