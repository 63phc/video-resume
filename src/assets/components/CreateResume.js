import axios from 'axios';


const CreateResume = ((createID =document.getElementById('#create_resume')) => {
    document.addEventListener("DOMContentLoaded", function(event) {
        if (document.querySelector('.edu-add')) {
            const host = location.host;
            const button_edu = document.querySelector('.edu-add');
            const button_skill = document.querySelector('.skill-add');
            const button_job = document.querySelector('.job-add');
            const form_ed = document.querySelector('.edu-form');
            const form_sk = document.querySelector('.skill-form');
            const form_jo = document.querySelector('.job-form');

            function getUrl(destination) {
                return 'http://' + host + '/dashboard/worker/' + destination + '/create/' + '0' + '/' + '0'
            };
            function* generateSequence(start, end) {
                for (let i = start; i <= end; i++) yield i;
            };
            function createTitle(div, form, sub_form, destination) {
                let gen_id = generateSequence(0, 500);
                let but_study = document.querySelector('.' + destination + '-create-add');
                but_study.onclick = (e) => {
                    e.preventDefault;
                    let id = gen_id.next()['value'];
                    let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
                    let params_submit = new URLSearchParams();
                    let list_input = sub_form.getElementsByTagName('input');
                    Array.from(list_input).forEach((elem) => {
                        params_submit.append(elem.name, elem.value)
                    })
                    let list_area = sub_form.getElementsByTagName('textarea');
                    if (list_area) {
                        Array.from(list_area).forEach((elem) => {
                            params_submit.append(elem.name, elem.value)
                        });
                }
                params_submit.append('tag', 'add');
                axios({
                    method: 'post',
                    headers: {
                    'X-CSRFToken': csrf_token,
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest'
                    },
                    url: getUrl(destination),
                    data: params_submit
                })
                .then(function (response) {
                    form.removeChild(div);
                    let list = document.querySelector('.' + destination + '-list')
                    let list_child = document.createElement('div');
                    list_child.className = 'form-check'
                    if (destination == 'education') {
                        name = 'name_institution'
                    } else if (destination == 'skill') {
                        name = 'name'
                    } else if (destination == 'job') {
                        name = 'name_company'
                    }
                    list_child.innerHTML = '<label class="form-check-label" for="id_' + destination + '_' + id + '"><input type="checkbox" class="form-check-input" name="' + destination + '" value="' + response['data']['id'] + '" id="id_' + destination + '_' + id + '" checked="">' + response['data'][name] + '</label>'
                    list.appendChild(list_child);
                })
                .catch(function (error) {
                    console.log('А response is not received')
                });
                };
            }
            function getForm(button, form, destination, get_func){
              button.onclick = () => {
                  if (form.children.length == 0) {
                        let div = document.createElement('div');
                        div.className = destination + '-form-create'
                        form.appendChild(div)
                        let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
                        let params = new URLSearchParams();
                        params.append('tag', 'create');
                        axios({
                            method: 'post',
                            headers: {
                            'X-CSRFToken': csrf_token,
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'X-Requested-With': 'XMLHttpRequest'
                            },
                            url: getUrl(destination),
                            data: params
                        })
                        .then(function (response) {
                            let create_form = document.querySelector('.' + destination + '-form-create')
                            let sub_form = document.createElement('form');
                            sub_form.className = destination + '-form-create-second'
                            sub_form.innerHTML = '<hr>' + response['data']['response'] + '<button type="button" class="btn btn-primary ' + destination + '-create-add mt-2">Add this ' + destination + '</button><hr>'
                            create_form.appendChild(sub_form);
                            get_func(div, form, sub_form, destination)
                          })
                          .catch(function (error) {
                            console.log('А response is not received')
                          });
                    } else {
                        let div_temp = document.querySelector('.' + destination + '-form-create')
                        form.removeChild(div_temp);
                    };
              };
            }
            getForm(button_edu, form_ed, 'education', createTitle)
            getForm(button_skill, form_sk, 'skill', createTitle)
            getForm(button_job, form_jo, 'job', createTitle)
        }
    })
})();

export default CreateResume;
