const btnLogin = document.querySelector('.btn-login');
const btnOpenModalReg = document.querySelector('#open-modal-reg');
const modals = document.querySelectorAll('.modal');
const modalLogin = document.querySelector('#modal-login');
const modalRegistr = document.querySelector('#modal-registr');

btnLogin.addEventListener('click', () => {
    modalLogin.classList.remove('hide');
    modalLogin.classList.add('show');
});

modals.forEach(modal => {
    modal.addEventListener('click', (e) => {
        const targetModal = e.target.closest(".modal__content");
        if(!targetModal) {
            modal.classList.add('hide');
            modal.classList.remove('show');
        }
    });
})

btnOpenModalReg.addEventListener('click', (e) => {
    modalLogin.classList.add('hide');
    modalLogin.classList.remove('show');

    modalRegistr.classList.remove('hide');
    modalRegistr.classList.add('show');
});
