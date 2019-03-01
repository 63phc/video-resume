const FOUNDED = 1;
const menuLinks = ['role_choice', 'accounts', 'features', 'contacts'];

function toggleActiveClass(class_name) {
    document.querySelector('.nav-link').classList.remove("active");
    document.querySelector('.' + class_name).classList.add('active');
}

const ActiveLink = (() => {
    const current_menu = menuLinks.find(
        link => location.pathname.indexOf(link) == FOUNDED);
    toggleActiveClass(current_menu);
})();

export default ActiveLink;
