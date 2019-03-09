const WorkerSwitch = (() => {
    return {
        disableElement: (parent_elem) => {
            let disable_panel = document.querySelectorAll('.worker-search-title');
            disable_panel.forEach((elem) => {
              elem.classList.remove('active');
              let target = elem.getAttribute('data-target');
              document.querySelector(target).classList.remove('show', 'active');
            });
            parent_elem.classList.add('active');
            let target_panel = parent_elem.getAttribute('data-target');
            document.querySelector(target_panel).classList.add('show', 'active');
        },
        clickOn: (titles, method) => {
            titles.forEach((elem) => {
                elem.onclick = (e) => {
                    e.preventDefault();
                    method(elem);
                }
            })
        }
    }
})();

export default WorkerSwitch;
