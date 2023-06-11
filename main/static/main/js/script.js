const openPopUp = document.getElementsByClassName('sign-in')[0]
const closePopUp = document.getElementsByClassName('pop_up_close')[0]

const popUp = document.getElementsByClassName('pop_up')[0]

openPopUp.addEventListener('click', (event) => {
    event.preventDefault();
})

openPopUp.addEventListener('click', function(){
    popUp.classList.add('active')
})

closePopUp.addEventListener('click', () => {
    popUp.classList.remove('active')
})
