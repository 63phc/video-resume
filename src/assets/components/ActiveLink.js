const menuLinks = ['role_choice', 'features', 'contacts', 'login', 'dashboard', 'register'];

Array.prototype.diff = function(a) {
    return this.filter(function(i){return a.includes(i);});
};

const ActiveLink = (() => {
    return {
        toggleActiveClass: (className) => {
            document.querySelector('.nav-link').classList.remove('active');
            document.querySelector(`.${className}`).classList.add('active');
        },
        getCurrentMenu: (currenUrl) => {
            if (currenUrl == '/')
                return ['main_page'];
            let link_for = currenUrl.split('/')
            let value = link_for.diff(menuLinks);
            if (value == 'register')
                return ['role_choice']
            return value
        }
    }
  
})();

export default ActiveLink;
