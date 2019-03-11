const UpdateResume = ((updateID = document.getElementById('#update_resume')) => {
    window.onload = function(){
        if (document.querySelector('#resume_pk')) {
            const host = location.host;
            const educations = document.querySelectorAll('[name = education]');
            const button_edu_update = document.querySelectorAll('.edu-update');
            const button_edu_add = document.querySelector('.edu-add-update');
            const button_edu_delete = document.querySelectorAll('.edu-delete');
            const skills = document.querySelectorAll('[name = skill]');
            const button_skill_update = document.querySelectorAll('.skill-update');
            const button_skill_add = document.querySelector('.skill-add-update');
            const button_skill_delete = document.querySelectorAll('.skill-delete');
            const jobs = document.querySelectorAll('[name = job]');
            const button_job_update = document.querySelectorAll('.job-update');
            const button_job_add = document.querySelector('.job-add-update');
            const button_job_delete = document.querySelectorAll('.job-delete');
            const worker_pk = document.querySelector('#worker_pk').value;
            const resume_pk = document.querySelector('#resume_pk').value;
            function urlEduUpdate(pk) {
                return 'http://' + host + '/dashboard/worker/education/update/' + pk + '/' + resume_pk + '/' + worker_pk
            };
            function urlEduDelete(pk) {
                return 'http://' + host + '/dashboard/worker/education/delete/' + pk + '/' + resume_pk + '/' + worker_pk
            };
            function urlSkillUpdate(pk) {
                return 'http://' + host + '/dashboard/worker/skill/update/' + pk + '/' + resume_pk + '/' + worker_pk
            };
            function urlSkillDelete(pk) {
                return 'http://' + host + '/dashboard/worker/skill/delete/' + pk + '/' + resume_pk + '/' + worker_pk
            };
            function urlJobUpdate(pk) {
                return 'http://' + host + '/dashboard/worker/job/update/' + pk + '/' + resume_pk + '/' + worker_pk
            };
            function urlJobDelete(pk) {
                return 'http://' + host + '/dashboard/worker/job/delete/' + pk + '/' + resume_pk + '/' + worker_pk
            };
            function sendRequest(array, button_list, elem_class, url_func) {
                array.forEach((element, index) => {
                    let pk = element.value;
                    let elem = button_list.item(index)
                    elem.classList.add(elem_class + pk)
                    elem.onclick = () => {
                      document.location.href = url_func(pk)
                    };
            })
            };
            sendRequest(educations, button_edu_update, 'edu-update', urlEduUpdate)
            if (button_edu_add) {
                button_edu_add.onclick = () => {
                    document.location.href = 'http://' + host + '/dashboard/worker/education/create/' + resume_pk + '/' + worker_pk
                };
            };
            sendRequest(educations, button_edu_delete, 'edu-delete', urlEduDelete)
            sendRequest(skills, button_skill_update, 'skill-update', urlSkillUpdate)
            if (button_skill_add) {
                button_skill_add.onclick = () => {
                    document.location.href = 'http://' + host + '/dashboard/worker/skill/create/' + resume_pk + '/' + worker_pk
                };
            };
            sendRequest(skills, button_skill_delete, 'skill-delete', urlSkillDelete)
            sendRequest(jobs, button_job_update, 'job-update', urlJobUpdate)
            if (button_job_add) {
                button_job_add.onclick = () => {
                    document.location.href = 'http://' + host + '/dashboard/worker/job/create/' + resume_pk + '/' + worker_pk
                };
            };
            sendRequest(jobs, button_job_delete, 'job-delete', urlJobDelete)
        }
    }
})();

export default UpdateResume;