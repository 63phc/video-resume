const Account = (() => {
    return {
        setAttribute: (accountId, path) => {
            accountId.setAttribute('value', path.split('/').reverse()[1]);
        }
    }
})();

export default Account;

window.addEventListener('load', () => {
    if (document.querySelector('#account_type')) {
        const accountId = document.querySelector('#account_type');
        Account.setAttribute(accountId, document.location.pathname);
    }
})
