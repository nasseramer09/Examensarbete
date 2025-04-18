function openTab(evt: MouseEvent, tabName:string):void{

    const alltabs = document.querySelectorAll<HTMLButtonElement>(".tabcontent");
    const allButtons = document.querySelectorAll<HTMLButtonElement>(".tablink");

    alltabs.forEach(tab=>{
        tab.classList.remove("active");
    });

    allButtons.forEach(tab=>{
        tab.classList.remove("active");
    });

    const selectTab= document.getElementById(tabName);
    if(selectTab){
        selectTab.classList.add("active")
    };

    const target = evt.currentTarget as HTMLButtonElement;
    target.classList.add("active")

    
}

document.addEventListener("DOMContentLoaded", ()=>{

    const tabButtons = document.querySelectorAll<HTMLButtonElement>(".tablink");
    
    tabButtons.forEach(btn => {
        const targetTab = btn.getAttribute("onclick")?.match(/openTab\(event,\s*'(.+?)'\)/)?.[1];
        if (targetTab){
            btn.addEventListener("click", (e) => openTab(e, targetTab));
        }
    });
    const defaultTab = document.getElementById("createAccount");
    const firstButton = document.querySelector(".tablinks") as HTMLButtonElement;
    if(defaultTab && firstButton){
        defaultTab.classList.add("active");
        firstButton.classList.add("active");
    }
})