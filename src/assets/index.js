import './scss/main.scss';

import Account from './components/Account';
import CreateResume from './components/CreateResume';
import UpdateResume from './components/UpdateResume';
import ActiveLink from './components/ActiveLink';
import WorkerSwitchLink from './components/WorkerSwitchLink';
import WorkerAnswer from './components/WorkerAnswer';
import { tns } from "tiny-slider/src/tiny-slider"


window.addEventListener('load', () => {
    // Account
    if (document.querySelector('#account_type')) {
        const accountId = document.querySelector('#account_type');
        Account.setAttribute(accountId, document.location.pathname);
    }
    // ActiveLink
    if (document.location.pathname == '/') {
        var slider = tns({
            container: '.my-slider',
            items: 2,
            slideBy: 'page',
            autoplay: false,
            controls: true,
            controlsText: ['<', '>'],
            controlsPosition: 'bottom',
            nav: false,
        });
        var vacancy_slider = tns({
            container: '.vacancy-slider',
            items: 2,
            slideBy: 'page',
            autoplay: false,
            controls: true,
            controlsText: ['<', '>'],
            controlsPosition: 'bottom',
            nav: false,
        });
    }
    const class_name = ActiveLink.getCurrentMenu(document.location.pathname);
    if (class_name) {
        ActiveLink.toggleActiveClass(class_name);
    }
    // WorkerSwitchLink
    if (document.querySelector('.worker-search-title')) {
        const titles = document.querySelectorAll('.worker-search-title');
        WorkerSwitchLink.clickOn(titles, WorkerSwitchLink.disableElement);
    }
    // WorkerAnswer
    if (document.querySelector('.add-answer')) {
        const add_button = document.querySelector('.add-answer-button');
        WorkerAnswer.getForm(add_button, WorkerAnswer.sendForm);
    }
});
