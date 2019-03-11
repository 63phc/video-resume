const Account = (() => {
    return {
        setAttribute: (accountId, path) => {
            accountId.setAttribute('value', path.split('/').reverse()[1]);
        }
    }
})();

export default Account;
