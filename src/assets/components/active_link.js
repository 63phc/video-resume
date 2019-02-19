$(function() {
    if (location.pathname.indexOf("role_choice") != -1) {
        $('nav-link').removeClass('active')
        $('sign_in').addClass('active')
    } else if (location.pathname.indexOf("account/login") != -1) {
        $('nav-link').removeClass('active')
        $('login').addClass('active')
    } else if (location.pathname.indexOf("features") != -1) {
        $('nav-link').removeClass('active')
        $('features').addClass('active')
    } else if (location.pathname.indexOf("contacts") != -1) {
        $('nav-link').removeClass('active')
        $('contacts').addClass('active')
    }
});
