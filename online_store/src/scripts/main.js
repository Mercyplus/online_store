const btnLogin = document.querySelector('.btn-login');
const modalLogin = document.querySelector('#modal-login');

btnLogin.addEventListener('click', () => {
    modalLogin.classList.remove('hide');
    modalLogin.classList.add('show');
});

modalLogin.addEventListener('click', (e) => {
    const targetModal = e.target.closest(".modal__content");
    if(!targetModal) {
        modalLogin.classList.add('hide');
        modalLogin.classList.remove('show');
    }
});
