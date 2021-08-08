const btnAccordion = document.querySelectorAll(".accordion__header")

for (let i = 0; i < btnAccordion.length; i++) {
    btnAccordion[i].addEventListener("click", () => {
        let panelAccordion = btnAccordion[i].nextSibling.nextSibling
        panelAccordion.classList.toggle("accordion__panel--open")
    })
}
