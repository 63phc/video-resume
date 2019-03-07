const FOUNDED = 1;
const menuLinks = ['role_choice', 'accounts', 'features', 'contacts'];

function toggleActiveClass(className) {
    document.querySelector('.nav-link').classList.remove('active');
    document.querySelector(`.${className}`).classList.add('active');
}

function getCurrentMenu(currenUrl) {
    if (currenUrl == '/')
        return 'main_page';

    return menuLinks.find(link => currenUrl.indexOf(link) == FOUNDED);
}

const ActiveLink = (() => {
    toggleActiveClass(getCurrentMenu(location.pathname));
})();

export default ActiveLink;
