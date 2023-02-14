const closeWork = document.querySelector('.close');
const openWork = document.querySelector('.open');
const work =  document.getElementById("div-work");


function openDiv() {
    work.style.height = "100%";
    openWork.style.height = '0';
    closeWork.style.height = '100%';
}
  
function closeDiv() {
   work.style.height = "0";
    closeWork.style.height = '0';
    openWork.style.height = '100%';
}