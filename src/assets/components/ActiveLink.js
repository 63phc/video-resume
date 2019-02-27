const FOUNDED = 1;
let menu_links = ['role_choice', 'accounts', 'features', 'contacts'];

function set_active_class_to (class_name) {
    document.querySelector('nav-link').removeClass('active');
    document.querySelector('.' + class_name).addClass('active');
}

const ActiveLink = (() => {
    document.addEventListener('DOMContentLoaded', function () {
        for (const item of menu_links) {
            if (location.pathname.indexOf(item) == FOUNDED) {
                set_active_class_to(item)
            }
        }
    })
})();

export default ActiveLink;
