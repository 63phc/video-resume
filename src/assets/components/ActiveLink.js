const ActiveLink = (() => {
    const menuLinks = ['role_choice', 'features', 'contacts', 'login', 'dashboard', 'register'];
    function union_field(arr1, arr2) {
        return arr1.filter(function(i){return arr2.includes(i);});
    };
    return {
        toggleActiveClass: (className) => {
            document.querySelector('.nav-link').classList.remove('active');
            document.querySelector(`.${className}`).classList.add('active');
        },
        getCurrentMenu: (currenUrl) => {
            if (currenUrl == '/')
                return ['main_page'];
            let link_for = currenUrl.split('/')
            let value = union_field(link_for, menuLinks)[0];
            if (value == 'register')
                return ['role_choice']
            return value
        }
    }
  
})();

export default ActiveLink;
