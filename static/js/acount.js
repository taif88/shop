
let form = document.getElementById('login-form')
let email = form['email']
let password = form['password']
let error = document.querySelector('p')
form.onsubmit = (event) => {
    let rege = /[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+/
    let regp = /[A-Za-z0-9!@#$%^&*]{8,}/
    if (!email.value.match(rege)) {
        event.preventDefault()
        console.log(email.value)
        error.innerHTML = 'EMAIL NOT VALID'
        return false
    } else if (!password.value.match(regp)) {
        event.preventDefault()
        console.log(email.value)
        error.innerHTML = 'PASSWORD NOT VALID'
        return false
    }
    return true
}



