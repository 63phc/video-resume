const FOUNDED = 1;
const menuLinks = ['role_choice', 'accounts', 'features', 'contacts'];

function setActiveClass(class_name) {
    document.querySelector('.nav-link').classList.remove("active");
    document.querySelector('.' + class_name).classList.add('active');
}

const ActiveLink = (() => {
    for (const item of menuLinks) {
        if (location.pathname.indexOf(item) == FOUNDED) {
            setActiveClass(item)
        }
    }
})();

export default ActiveLink;
