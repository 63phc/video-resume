import $ from 'jquery';

const Account = ((accountID = $('#account_type')) => {
    const pathname = $(location).attr('pathname').split('/').reverse();
    const account = $("#account_type").val(pathname[1]);
})();

export default Account;