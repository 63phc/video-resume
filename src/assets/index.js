import './scss/main.scss';

import Account from './components/Account';
import CreateResume from './components/CreateResume';
import UpdateResume from './components/UpdateResume';
import ActiveLink from './components/ActiveLink';
import DashboardSetActiveMenu from './components/DashboardSetActiveMenu';
import WorkerSwitchLink from './components/WorkerSwitchLink';
import WorkerAnswer from './components/WorkerAnswer';
import { tns } from "tiny-slider/src/tiny-slider"


window.addEventListener('load', () => {
    // Account
    if (document.querySelector('#account_type')) {
        const accountId = document.querySelector('#account_type');
        Account.setAttribute(accountId, document.location.pathname);
    }
    // Sliders
    if (document.querySelector('.resume-slider')) {
        var slider = tns({
            container: '.resume-slider',
            items: 2,
            slideBy: 'page',
            autoplay: false,
            controls: true,
            controlsText: ['<', '>'],
            controlsPosition: 'bottom',
            nav: false,
        });
    }
    if (document.querySelector('.vacancy-slider')) {
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

    // ActiveLink
    const class_name = ActiveLink.getCurrentMenu(document.location.pathname);
    if (class_name) {
        ActiveLink.toggleActiveClass(class_name);
    }

    // DashboardSetActiveMenu
    if (document.querySelector('#sub_menu')) {
         DashboardSetActiveMenu();
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
