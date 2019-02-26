import $ from 'jquery';

const UpdateResume = ((updateID = $('#update_resume')) => {
    $(document).ready(function(){
      const host = $(location).attr('host');
      const educations_pk = $("[name = education]");
      const button_edu_update = $(".edu-update");
      const button_edu_add = $(".edu-add-update");
      const button_edu_delete = $(".edu-delete");
      const skills_pk = $("[name = skill]");
      const button_skill_update = $(".skill-update");
      const button_skill_add = $(".skill-add-update");
      const button_skill_delete = $(".skill-delete");
      const jobs_pk = $("[name = job]");
      const button_job_update = $(".job-update");
      const button_job_add = $(".job-add-update");
      const button_job_delete = $(".job-delete");
      const worker_pk = $("#worker_pk").val();
      const resume_pk = $("#resume_pk").val();
      $.each(educations_pk,function(index, element) {
        let edu_pk = element.value;
        $(button_edu_update[index]).addClass("edu-update" + edu_pk).click(() => {
          document.location.href = 'http://' + host + '/dashboard/worker/education/update/' + edu_pk + '/' + resume_pk + '/' + worker_pk
        })
      })
      $(button_edu_add).click(() => {
         document.location.href = 'http://' + host + '/dashboard/worker/education/create/' + resume_pk + '/' + worker_pk
       })
      $.each(educations_pk,function(index, element) {
        let edu_pk = element.value;
        $(button_edu_delete[index]).addClass("edu-delete" + edu_pk).click(() => {
          document.location.href = 'http://' + host + '/dashboard/worker/education/delete/' + edu_pk + '/' + resume_pk + '/' + worker_pk
        })
      })
      $.each(skills_pk,function(index, element) {
        let sk_pk = element.value;
        $(button_skill_update[index]).addClass("skill-update" + sk_pk).click(() => {
          document.location.href = 'http://' + host + '/dashboard/worker/skill/update/' + sk_pk + '/' + resume_pk + '/' + worker_pk
        })
      })
      $(button_skill_add).click(() => {
         document.location.href = 'http://' + host + '/dashboard/worker/skill/create/' + resume_pk + '/' + worker_pk
       })
      $.each(skills_pk,function(index, element) {
        let sk_pk = element.value;
        $(button_skill_delete[index]).addClass("skill-delete" + sk_pk).click(() => {
          document.location.href = 'http://' + host + '/dashboard/worker/skill/delete/' + sk_pk + '/' + resume_pk + '/' + worker_pk
        })
      })
      $.each(jobs_pk,function(index, element) {
        let jo_pk = element.value;
        $(button_job_update[index]).addClass("job-update" + jo_pk).click(() => {
          document.location.href = 'http://' + host + '/dashboard/worker/job/update/' + jo_pk + '/' + resume_pk + '/' + worker_pk
        })
      })
      $(button_job_add).click(() => {
         document.location.href = 'http://' + host + '/dashboard/worker/job/create/' + resume_pk + '/' + worker_pk
       })
      $.each(jobs_pk,function(index, element) {
        let jo_pk = element.value;
        $(button_job_delete[index]).addClass("job-delete" + jo_pk).click(() => {
          document.location.href = 'http://' + host + '/dashboard/worker/job/delete/' + jo_pk + '/' + resume_pk + '/' + worker_pk
        })
      })
    })
})();

export default UpdateResume;