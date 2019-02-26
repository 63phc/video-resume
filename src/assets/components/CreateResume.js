import $ from 'jquery';

const CreateResume = ((createID = $('#create_resume')) => {
    $(document).ready(function(){
      const host = $(location).attr('host');
      const button_edu_add = $(".edu-add");
      const button_skill_add = $(".skill-add");
      const button_job_add = $(".job-add");
      function* generateSequence(start, end) {
        for (let i = start; i <= end; i++) yield i;
      }
      $(button_edu_add).click(() => {
        if ($(".edu-form").children().length == 0) {
          let csrf_token = $('[name="csrfmiddlewaretoken"]').val();
          let url = 'http://' + host + '/dashboard/worker/education/create/' + "0" + '/' + "0"
          let data = {'tag': 'create'};
          $.ajax({
              url: url,
              method: 'POST',
              headers: {"X-CSRFToken": csrf_token},
              data: data,
              success: function(data) {
                $(".edu-form").append('<hr><form class="edu-create-form">' + data['response'] + '<button type="submit" class="btn btn-primary edu-create-add mt-2">Add this education</button><hr>');
              },
              error: function() {
                  console.log("А response is not received");
              }
          });
        } else {
          $(".edu-form").empty()
        }
       })
     var gen_id_edu = generateSequence(0, 50)
     $(".edu-form").submit((e) => {
        e.preventDefault();
        let id = gen_id_edu.next()['value']
        let csrf_token = $('[name="csrfmiddlewaretoken"]').val();
        let url = 'http://' + host + '/dashboard/worker/education/create/' + "0" + '/' + "0"
        let data = {};
        data['period_edu'] = $('#id_period_edu').val();
        data['name_institution'] = $('#id_name_institution').val();
        data['faculty'] = $('#id_faculty').val();
        data['form_study'] = $('#id_form_study').val();
        data['tag'] = 'add'
        $.ajax({
          url: url,
          method: 'POST',
          headers: {"X-CSRFToken": csrf_token},
          data: data,
          success: function(data) {
            $(".edu-form").empty()
            $(".edu-list").append('<div class="form-check"><label class="form-check-label" for="id_education_' + id + '"><input type="checkbox" class="form-check-input" name="education" value="' + data['id'] + '" id="id_education_' + id + '" checked="">' + data['name_institution'] + '</label></div>')
          },
          error: function() {
            console.log("А response is not received");
          }
        })
      })
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