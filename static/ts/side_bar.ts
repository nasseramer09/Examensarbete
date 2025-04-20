function toggleSideBar(): void {
    const sideBar = document.getElementById("sidebar");
    const mainContent = document.getElementById("main-content");
    const closedBtn = document.getElementById("closeBtn");

    if(sideBar && mainContent && closedBtn){
    const isClosed = sideBar.classList.contains("closed");

    if(isClosed){ 
        sideBar.classList.remove("closed");
        mainContent.classList.remove("closed");
        closedBtn.style.display =  "block";
    }else{
        sideBar.classList.add("closed");
        mainContent.classList.add("closed");
        closedBtn.style.display =  "none";
    }
}

console.log("toggled side bar")

}


document.addEventListener("DOMContentLoaded", ()=>{

    const hamburgerBtn = document.getElementById("hamburgerBtn");
    const closeBtn = document.getElementById("closeBtn");

    if(hamburgerBtn) hamburgerBtn.addEventListener("click", toggleSideBar)
    

    if(closeBtn)closeBtn.addEventListener("click", toggleSideBar)
    
})

