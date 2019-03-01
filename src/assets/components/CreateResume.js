import axios from 'axios';


const CreateResume = ((createID =document.getElementById('#create_resume')) => {
      document.addEventListener("DOMContentLoaded", function(event) {
      const host = location.host;
      const button_edu = document.querySelector('.edu-add');
      const button_skill = document.querySelector('.skill-add');
      const button_job = document.querySelector('.job-add');
      const edu_url = 'http://' + host + '/dashboard/worker/education/create/' + '0' + '/' + '0';
      const skill_url = 'http://' + host + '/dashboard/worker/skill/create/' + '0' + '/' + '0'
      const job_url = 'http://' + host + '/dashboard/worker/job/create/' + "0" + '/' + "0"
      function* generateSequence(start, end) {
        for (let i = start; i <= end; i++) yield i;
      };
      button_edu.onclick = () => {
      const form_ed = document.querySelector('.edu-form')
      if (form_ed.children.length == 0) {
            const div = document.createElement('div');
            div.className = 'edu-form-create'
            form_ed.appendChild(div)
            let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
            let params_edu_create = new URLSearchParams();
            params_edu_create.append('tag', 'create');
            axios({
                method: 'post',
                headers: {
                'X-CSRFToken': csrf_token,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest'
                },
                url: edu_url,
                data: params_edu_create
            })
            .then(function (response) {
                const create_form_ed = document.querySelector('.edu-form-create')
                let sub_form = document.createElement('form');
                sub_form.className = 'edu-form-create-second'
                sub_form.innerHTML = '<hr>' + response['data']['response'] + '<button type="button" class="btn btn-primary edu-create-add mt-2">Add this education</button><hr>'
                create_form_ed.appendChild(sub_form);
                let gen_id_edu = generateSequence(0, 50);
                let edu_but_study = document.querySelector('.edu-create-add');
                edu_but_study.onclick = (e) => {
                    e.preventDefault;
                    let id = gen_id_edu.next()['value'];
                    let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
                    const id_period_edu = document.querySelector('#id_period_edu')
                    const id_name_institution = document.querySelector('#id_name_institution')
                    const id_faculty = document.querySelector('#id_faculty')
                    const id_form_study = document.querySelector('#id_form_study')
                    let params_edu_submit = new URLSearchParams();
                    params_edu_submit.append('period_edu', id_period_edu.value);
                    params_edu_submit.append('name_institution', id_name_institution.value);
                    params_edu_submit.append('faculty', id_faculty.value);
                    params_edu_submit.append('form_study', id_form_study.value);
                    params_edu_submit.append('tag', 'add');
                    axios({
                        method: 'post',
                        headers: {
                        'X-CSRFToken': csrf_token,
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With': 'XMLHttpRequest'
                        },
                        url: edu_url,
                        data: params_edu_submit
                    })
                    .then(function (response) {
                        form_ed.removeChild(div);
                        let edu_list = document.querySelector('.edu-list')
                        let edu_list_child = document.createElement('div');
                        edu_list_child.className = 'form-check'
                        edu_list_child.innerHTML = '<label class="form-check-label" for="id_education_' + id + '"><input type="checkbox" class="form-check-input" name="education" value="' + response['data']['id'] + '" id="id_education_' + id + '" checked="">' + response['data']['name_institution'] + '</label>'
                        edu_list.appendChild(edu_list_child);
                    })
                    .catch(function (error) {
                        console.log('А response is not received')
                    });
                    };
              })
              .catch(function (error) {
                console.log('А response is not received')
              });
        } else {
            let div = document.querySelector('.edu-form-create')
            form_ed.removeChild(div);
        };
      };
      button_skill.onclick = () => {
      const form_sk = document.querySelector('.skill-form')
      if (form_sk.children.length == 0) {
            const div = document.createElement('div');
            div.className = 'skill-form-create'
            form_sk.appendChild(div)
            let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
            let params_skill_create = new URLSearchParams();
            params_skill_create.append('tag', 'create');
            axios({
                method: 'post',
                headers: {
                'X-CSRFToken': csrf_token,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest'
                },
                url: skill_url,
                data: params_skill_create
            })
            .then(function (response) {
                const create_form_sk = document.querySelector('.skill-form-create')
                let sub_form = document.createElement('form');
                sub_form.className = 'skill-form-create-second'
                sub_form.innerHTML = '<hr>' + response['data']['response'] + '<button type="button" class="btn btn-primary skill-create-add mt-2">Add this skill</button><hr>'
                create_form_sk.appendChild(sub_form);
                let gen_id_skill = generateSequence(0, 50);
                let skill_but_study = document.querySelector('.skill-create-add');
                skill_but_study.onclick = (e) => {
                    e.preventDefault;
                    let id = gen_id_skill.next()['value'];
                    let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
                    const id_name_skill = document.querySelector('#id_name')
                    let params_skill_submit = new URLSearchParams();
                    params_skill_submit.append('name', id_name_skill.value);
                    params_skill_submit.append('tag', 'add');
                    axios({
                        method: 'post',
                        headers: {
                        'X-CSRFToken': csrf_token,
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With': 'XMLHttpRequest'
                        },
                        url: skill_url,
                        data: params_skill_submit
                    })
                    .then(function (response) {
                        form_sk.removeChild(div);
                        let skill_list = document.querySelector('.skill-list')
                        let skill_list_child = document.createElement('div');
                        skill_list_child.className = 'form-check'
                        skill_list_child.innerHTML = '<label class="form-check-label" for="id_skill_' + id + '"><input type="checkbox" class="form-check-input" name="skill" value="' + response['data']['id'] + '" id="id_skill_' + id + '" checked="">' + response['data']['name'] + '</label></div>'
                        skill_list.appendChild(skill_list_child);
                    })
                    .catch(function (error) {
                        console.log('А response is not received')
                    });
                    };
              })
              .catch(function (error) {
                console.log('А response is not received')
              });
        } else {
            let div = document.querySelector('.skill-form-create')
            form_sk.removeChild(div);
        };
      };
      button_job.onclick = () => {
      const form_jo = document.querySelector('.job-form')
      if (form_jo.children.length == 0) {
            const div = document.createElement('div');
            div.className = 'job-form-create'
            form_jo.appendChild(div)
            let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
            let params_job_create = new URLSearchParams();
            params_job_create.append('tag', 'create');
            axios({
                method: 'post',
                headers: {
                'X-CSRFToken': csrf_token,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest'
                },
                url: job_url,
                data: params_job_create
            })
            .then(function (response) {
                const create_form_jo = document.querySelector('.job-form-create')
                let sub_form = document.createElement('form');
                sub_form.className = 'job-form-create-second'
                sub_form.innerHTML = '<hr>' + response['data']['response'] + '<button type="button" class="btn btn-primary job-create-add mt-2">Add this job</button><hr>'
                create_form_jo.appendChild(sub_form);
                let gen_id_job = generateSequence(0, 50);
                let job_but_study = document.querySelector('.job-create-add');
                job_but_study.onclick = (e) => {
                    e.preventDefault;
                    let id = gen_id_job.next()['value'];
                    let csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
                    const id_period_work = document.querySelector('#id_period_work')
                    const id_position = document.querySelector('#id_position')
                    const id_name_company = document.querySelector('#id_name_company')
                    let params_job_submit = new URLSearchParams();
                    params_job_submit.append('period_work', id_period_work.value);
                    params_job_submit.append('position', id_position.value);
                    params_job_submit.append('name_company', id_name_company.value);
                    params_job_submit.append('tag', 'add');
                    axios({
                        method: 'post',
                        headers: {
                        'X-CSRFToken': csrf_token,
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With': 'XMLHttpRequest'
                        },
                        url: job_url,
                        data: params_job_submit
                    })
                    .then(function (response) {
                        form_jo.removeChild(div);
                        let job_list = document.querySelector('.job-list')
                        let job_list_child = document.createElement('div');
                        job_list_child.className = 'form-check'
                        job_list_child.innerHTML = '<label class="form-check-label" for="id_job_' + id + '"><input type="checkbox" class="form-check-input" name="job" value="' + response['data']['id'] + '" id="id_job_' + id + '" checked="">' + response['data']['name_company'] + '</label></div>'
                        job_list.appendChild(job_list_child);
                    })
                    .catch(function (error) {
                        console.log('А response is not received')
                    });
                    };
              })
              .catch(function (error) {
                console.log('А response is not received')
              });
        } else {
            let div = document.querySelector('.job-form-create')
            form_jo.removeChild(div);
        };
      };
    })
})();

export default CreateResume;
