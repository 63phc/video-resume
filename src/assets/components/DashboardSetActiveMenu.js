const DashboardSetActiveMenu = (() => {

    const currentPage = location.href;
    const allAs = document.querySelectorAll('.sub-link');
    const allAsLength = allAs.length;

    for (let i = 0; i < allAsLength; i++) {
      if (allAs[i].href === currentPage ) {
        allAs[i].classList.add('active');
      }
      else {
          allAs[i].classList.remove('active')
      }
    }
    return () => false;
})();

export default DashboardSetActiveMenu;