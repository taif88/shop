data = null
fetch("/api/cart")
    .then((re) => re.json()).then((re) => {
        data = re
        console.log(data)
        Object.values(data).forEach((ele) => {
            const tbody = document.getElementById('cart-content')
            const tr = document.createElement('tr')
            tbody.appendChild(tr)
            tr.innerHTML = `<td>
                        <img src="./static/proim.jpg" alt="">
                        <span>${ele.pron}</span>
                    </td>
                    <td>
                        ${ele.propri}$
                    </td>`
        })
    }).catch((e) => console.error("cart"))