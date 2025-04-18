"use strict";
function openTab(evt, tabName) {
    const alltabs = document.querySelectorAll(".tabcontent");
    const allButtons = document.querySelectorAll(".tablink");
    alltabs.forEach(tab => {
        tab.classList.remove("active");
    });
    allButtons.forEach(tab => {
        tab.classList.remove("active");
    });
    const selectTab = document.getElementById(tabName);
    if (selectTab) {
        selectTab.classList.add("active");
    }
    ;
    const target = evt.currentTarget;
    target.classList.add("active");
}
document.addEventListener("DOMContentLoaded", () => {
    const tabButtons = document.querySelectorAll(".tablink");
    tabButtons.forEach(btn => {
        var _a, _b;
        const targetTab = (_b = (_a = btn.getAttribute("onclick")) === null || _a === void 0 ? void 0 : _a.match(/openTab\(event,\s*'(.+?)'\)/)) === null || _b === void 0 ? void 0 : _b[1];
        if (targetTab) {
            btn.addEventListener("click", (e) => openTab(e, targetTab));
        }
    });
    const defaultTab = document.getElementById("createAccount");
    const firstButton = document.querySelector(".tablinks");
    if (defaultTab && firstButton) {
        defaultTab.classList.add("active");
        firstButton.classList.add("active");
    }
});
