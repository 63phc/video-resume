const FOUNDED = 1;
const menuLinks = ['role_choice', 'accounts', 'features', 'contacts'];

function setActiveClass(class_name) {
    document.querySelector('.nav-link').classList.remove("active");
    document.querySelector('.' + class_name).classList.add('active');
}

const ActiveLink = (() => {
    const current_menu = menuLinks.filter(function(link) {
        return location.pathname.indexOf(link) == FOUNDED
    })[0];
    setActiveClass(current_menu)
})();

export default ActiveLink;
