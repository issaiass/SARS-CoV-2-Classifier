var ById = x => document.getElementById(x);

function browseImg() {

  ById("catchimg").click();

}

function catchImg(input) {
  var reader = new FileReader();


  reader.readAsDataURL(input.files[0]);

  ById("lblfilename").innerHTML = input.files[0].name;

  reader.onload = function(e) {
    ById("dispimg").src = e.target.result;
    ById("dispimg").className = ""
  };

}


function Diagnose() {
  var uploadFiles = ById("catchimg").files;
  var xhr = new XMLHttpRequest();
  var loc = window.location;
  var fileData = new FormData();

    
  ById("btndiagnose").innerHTML = "Just a moment...";
 
  xhr.open("POST", `${loc.href}predict`,true);
  
  xhr.onerror = function() {
    console.log(xhr.responseText);
  };

  xhr.onload = function(e) {
    if (this.readyState === 4) {
      var response = JSON.parse(e.target.response);
      ById("lblcovid").innerHTML  = "COVID  Confidence: ".concat(response.predictions[0].covid.toFixed(4));
      ById("lblnormal").innerHTML = "NORMAL Confidence: ".concat(response.predictions[0].normal.toFixed(4));
    }
    ById("btndiagnose").innerHTML = "Diagnose";
  };

  fileData.append("image", uploadFiles[0]);
  xhr.send(fileData);
}
