const WorkerSwitchLink = (() => {
    return {
        disableElement: (parent) => {
            let panels = document.querySelectorAll('.worker-search-title');

            panels.forEach((elem) => {
              elem.classList.remove('active');
              let target = elem.getAttribute('data-target');
              document.querySelector(target).classList.remove('show', 'active');
            });

            parent.classList.add('active');

            let target_panel = parent.getAttribute('data-target');
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

export default WorkerSwitchLink;
