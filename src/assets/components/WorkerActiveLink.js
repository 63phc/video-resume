const WorkerActiveLink = (() => {
    return {
        DisableElement: (parent_elem) => {
            let disable_panel = document.querySelectorAll('.worker-search-title');
            disable_panel.forEach((elem) => {
              elem.classList.remove('active');
              let target = elem.getAttribute('data-target');
              document.querySelector(target).classList.remove('show', 'active');
            });
            parent_elem.classList.add('active');
            let target_panel = parent_elem.getAttribute('data-target');
            document.querySelector(target_panel).classList.add('show', 'active');
        }
    }
})();

export default WorkerLink;

document.addEventListener('load', () => {
  console.log('qwerty')
  const titles = document.querySelectorAll('.worker-search-title');
  if (document.querySelector('.worker-search-title')) {
    titles.forEach((elem) => {
      elem.onclick = (e) => {
          e.preventDefault;
          WorkerActiveLink.DisableElement(elem);
      }
    })
  }
})