const FOUNDED = 1;
const menuLinks = ['role_choice', 'accounts', 'features', 'contacts'];

function toggleActiveClass(className) {
    document.querySelector('.nav-link').classList.remove('active');
    document.querySelector(`.${className}`).classList.add('active');
}

const ActiveLink = (() => {
    const currenUrl = location.pathname;
    let currentMenu = '';
    if (currenUrl == '/') currentMenu = 'main_page';
    else currentMenu = menuLinks.find(
        link => currenUrl.indexOf(link) == FOUNDED);
    toggleActiveClass(currentMenu);
})();

export default ActiveLink;
