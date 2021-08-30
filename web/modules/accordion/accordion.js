const btnAccordion = document.querySelectorAll(".accordion")

for ( let i = 0; i < btnAccordion .length; i++) {
    btnAccordion [i].addEventListener("click", function() {
        this.classList.toggle("accordion--active");
        let panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}
