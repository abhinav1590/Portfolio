document.addEventListener('DOMContentLoaded',function(event){
    var dataText = ["Experienced.","Energetic.","Motivated!","Resilient!"];
  
    function typeWriter(text, i, fnCallback) {
      if (i < (text.length)) {
       document.querySelector(".h2").innerHTML = '&lt;' + text.substring(0, i+1) +'<span aria-hidden="true"></span>' + '&gt;' ;
        setTimeout(function() {
          typeWriter(text, i + 1, fnCallback)
        }, 80);
      }
      else if (typeof fnCallback == 'function') {
        setTimeout(fnCallback, 700);
      }
    }
     function StartTextAnimation(i) {
       if (typeof dataText[i] == 'undefined'){
          setTimeout(function() {
            StartTextAnimation(0);
          }, 2000);
       }
      if (i < dataText[i].length) {
       typeWriter(dataText[i], 0, function(){
         StartTextAnimation(i + 1);
       });
      }
    }
    StartTextAnimation(0);
  });

const message = document.getElementById("messages");

setTimeout(function(){ 
   message.style.display = "none"; 
}, 3000)