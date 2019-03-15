import axios from 'axios';


const WorkerAnswer = (() => {
    const div_form = document.querySelector('.div-answer-form')
    const csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    function getUrl() {
        const host = location.host;
        return 'http://' + host + '/dashboard/worker/questions/detail/answer/'
    };
    return {
        getForm: (add_button, get_func) => {
            add_button.onclick = (e) => {
                if (div_form.children.length == 0) {
                    e.preventDefault();
                    let params = new URLSearchParams();
                    params.append('tag', 'create');
                    axios({
                        method: 'post',
                        headers: {
                        'X-CSRFToken': csrf_token,
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With': 'XMLHttpRequest'
                        },
                        url: getUrl(),
                        data: params
                    })
                    .then(function (response) {
                        let sub_form = document.createElement('form');
                        sub_form.className = 'answer-form'
                        sub_form.name = 'answer-form'
                        sub_form.innerHTML = '<tr><th><label for="id_answer">Answer:</label></th><td><textarea name="answer" cols="40" rows="10" class="form-control" id="id_answer"></textarea></td></tr><button type="button" class="btn btn-primary answer-create-add mt-2">Add this answer</button><div id="error"></div>'
                        div_form.appendChild(sub_form);
                        get_func(sub_form)

                    })
                    .catch(function (error) {
                        console.log('А response is not received');
                    });
                } else {
                    let div_temp = document.querySelector('.answer-form');
                    div_form.removeChild(div_temp);
                };
            }
        },
        sendForm:(sub_form) => {
            const send_button = document.querySelector('.answer-create-add')
            send_button.onclick = (e) => {
                e.preventDefault();
                let text = document.getElementById('id_answer');
                if (text.value == '') {
                    return
                }
                let params_send = new URLSearchParams();
                const answer_pk = document.querySelector('.id_answer')
                params_send.append('question_id', answer_pk.value);
                params_send.append('answer', text.value);
                params_send.append('tag', 'add');
                axios({
                        method: 'post',
                        headers: {
                        'X-CSRFToken': csrf_token,
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With': 'XMLHttpRequest'
                        },
                        url: getUrl(),
                        data: params_send
                })
                .then(function (response) {
                    console.log('goooooooood!!!!!!')
                    div_form.removeChild(sub_form);
                    let answer = document.querySelector('.answer-block');
                    answer.innerHTML = '';
                    answer.innerHTML = '<p class="mb-3">' + response['data']['response'] + '</p>'
                })
                .catch(function (error) {
                    console.log('А response is not received');
                });
            }
        }
    }
})();

export default WorkerAnswer;
