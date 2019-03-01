import $ from 'jquery';
import axios from 'axios';


const CreateResume = ((createID =document.getElementById('#create_resume')) => {
      document.addEventListener("DOMContentLoaded", function(event) {
      const host = location.host;
      const button_edu = document.querySelector('.edu-add');
      const button_skill_add = $(".skill-add");
      const button_job_add = $(".job-add");
      const edu_url = 'http://' + host + '/dashboard/worker/education/create/' + '0' + '/' + '0';
      function* generateSequence(start, end) {
        for (let i = start; i <= end; i++) yield i;
      };
      button_edu.onclick = () => {
      const form = document.querySelector('.edu-form')
      if (form.children.length == 0) {
            const div = document.createElement('div');
            div.className = 'edu-form-create'
            form.appendChild(div)
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
                const create_form = document.querySelector('.edu-form-create')
                let sub_form = document.createElement('form');  // form
                sub_form.className = 'edu-form-create-second'                               // submit button
                sub_form.innerHTML = '<hr>' + response['data']['response'] + '<button type="button" class="btn btn-primary edu-create-add mt-2">Add this education</button><hr>'
                create_form.appendChild(sub_form);
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
                    // id_period_edu.validity.valid - validation true false
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
                        form.removeChild(div);
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
            form.removeChild(div);
        };
      };
      $(button_skill_add).click(() => {
        if ($(".skill-form").children().length == 0) {
          let csrf_token = $('[name="csrfmiddlewaretoken"]').val();
          let url = 'http://' + host + '/dashboard/worker/skill/create/' + "0" + '/' + "0"
          let data = {'tag': 'create'};
          $.ajax({
              url: url,
              method: 'POST',
              headers: {"X-CSRFToken": csrf_token},
              data: data,
              success: function(data) {
                $(".skill-form").append('<hr><form class="skill-create-form">' + data['response'] + '<button type="submit" class="btn btn-primary skill-create-add mt-2">Add this skill</button><hr>');
              },
              error: function() {
                  console.log("А response is not received");
              }
          });
        } else {
          $(".skill-form").empty()
        }
       })
       let gen_id_skill = generateSequence(0, 50)
       $(".skill-form").submit((e) => {
        e.preventDefault();
        let id = gen_id_skill.next()['value']
        let csrf_token = $('[name="csrfmiddlewaretoken"]').val();
        let url = 'http://' + host + '/dashboard/worker/skill/create/' + "0" + '/' + "0"
        let data = {};
        data['name'] = $('#id_name').val();
        data['tag'] = 'add'
        $.ajax({
          url: url,
          method: 'POST',
          headers: {"X-CSRFToken": csrf_token},
          data: data,
          success: function(data) {
            $(".skill-form").empty()
            $(".skill-list").append('<div class="form-check"><label class="form-check-label" for="id_skill_' + id + '"><input type="checkbox" class="form-check-input" name="skill" value="' + data['id'] + '" id="id_skill_' + id + '" checked="">' + data['name'] + '</label></div>')
          },
          error: function() {
            console.log("А response is not received");
          }
        })
      })
      $(button_job_add).click(() => {
        if ($(".job-form").children().length == 0) {
          let csrf_token = $('[name="csrfmiddlewaretoken"]').val();
          let url = 'http://' + host + '/dashboard/worker/job/create/' + "0" + '/' + "0"
          let data = {'tag': 'create'};
          $.ajax({
              url: url,
              method: 'POST',
              headers: {"X-CSRFToken": csrf_token},
              data: data,
              success: function(data) {
                $(".job-form").append('<hr><form class="job-create-form">' + data['response'] + '<button type="submit" class="btn btn-primary job-create-add mt-2">Add this job</button><hr>');
              },
              error: function() {
                  console.log("А response is not received");
              }
          });
        } else {
          $(".job-form").empty()
        }
       })
       let gen_id_job = generateSequence(0, 50)
       $(".job-form").submit((e) => {
        e.preventDefault();
        let id = gen_id_job.next()['value']
        let csrf_token = $('[name="csrfmiddlewaretoken"]').val();
        let url = 'http://' + host + '/dashboard/worker/job/create/' + "0" + '/' + "0"
        let data = {};
        data['period_work'] = $('#id_period_work').val();
        data['position'] = $('#id_position').val();
        data['name_company'] = $('#id_name_company').val();
        data['tag'] = 'add'
        $.ajax({
          url: url,
          method: 'POST',
          headers: {"X-CSRFToken": csrf_token},
          data: data,
          success: function(data) {
            $(".job-form").empty()
            $(".job-list").append('<div class="form-check"><label class="form-check-label" for="id_job_' + id + '"><input type="checkbox" class="form-check-input" name="job" value="' + data['id'] + '" id="id_job_' + id + '" checked="">' + data['name_company'] + '</label></div>')
          },
          error: function() {
            console.log("А response is not received");
          }
        })
      })
    })
})();

export default CreateResume;
