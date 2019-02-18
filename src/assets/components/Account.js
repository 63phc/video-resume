import $ from 'jquery';

const Account = ((accountID = $('#account_type')) => {
    $(document).ready(function(){
        var pathname = $(location).attr('pathname');
        var for_account = pathname.split('/').reverse()
        var account = $("#account_type").val(for_account[1]);
        console.log(account.val())
    })
})();

export default Account;