const SwitchLang = (() => {
    return {
        setLang: (lang, form) => {
            lang.onchange = () => {
                form.submit()
            }
        }
    }
})();

export default SwitchLang;