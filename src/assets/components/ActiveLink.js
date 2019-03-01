const FOUNDED = 1;
const menuLinks = ['role_choice', 'accounts', 'features', 'contacts'];

function toggleActiveClass(className) {
    document.querySelector('.nav-link').classList.remove('active');
    document.querySelector(`.${className}`).classList.add('active');
}

const ActiveLink = (() => {
    const currentMenu = menuLinks.find(
        link => location.pathname.indexOf(link) == FOUNDED);
    toggleActiveClass(currentMenu);
})();

export default ActiveLink;
