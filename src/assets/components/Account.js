import $ from 'jquery';

const Account = ((accountID = $('#account_type')) => {
    $(document).ready(function(){
        let pathname = $(location).attr('pathname');
        let for_account = pathname.split('/').reverse()
        let account = $("#account_type").val(for_account[1]);
    })
})();

export default Account;