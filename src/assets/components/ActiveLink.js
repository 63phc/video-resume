const FOUNDED = 1;
const menuLinks = ['role_choice', 'accounts', 'features', 'contacts'];

function toggleActiveClass(className) {
    document.querySelector('.nav-link').classList.remove('active');
    document.querySelector(`.${className}`).classList.add('active');
}

function getCurrentMenu() {
    const currenUrl = location.pathname;
    let currentMenu = '';
    if (currenUrl == '/') currentMenu = 'main_page';
    else currentMenu = menuLinks.find(
        link => currenUrl.indexOf(link) == FOUNDED);
    return currentMenu;
}

const ActiveLink = (() => {
    toggleActiveClass(getCurrentMenu());
})();

export default ActiveLink;
