function openNav() {
  document.getElementById("bar").style.width = "250px";
}

function closeNav() {
  document.getElementById("bar").style.width = "0";
}

function network_scan_execute(){
    var x = document.getElementById("Network-scan_form").elements;
    for (i=0; i < x.length; i++ ){
        alert("values "+x[i].value)
    }
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/networkscan");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("Network-scan_response").innerHTML =
            this.responseText;
            alert(xmlhttp.text)
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value}
    alert(obj1)
    xmlhttp.send(JSON.stringify(obj1));

}

function changeScan() {
  var x = document.getElementById("scanSelect").value;
  document.getElementById("scanType").innerHTML = "You selected: " + x;
  if(x != ""){
    var ele = document.getElementById("actions");
    if( ele.style.display == "none"){
        ele.style.display = "block"
    }
  }
}

function showExplain() {
  var x = document.getElementById("scanSelect").value;
  hidden_all();
  var ele = document.getElementById(x+"_explain");
  if( ele.style.display == "none"){
    ele.style.display = "block";
  }
}

function showExecute() {
  var x = document.getElementById("scanSelect").value;
  hidden_all()
  var ele = document.getElementById(x+"_execute");
  if( ele.style.display == "none"){
    ele.style.display = "block";
  }
}
function hidden_all(){
    var x = document.getElementById("scanSelect").value;
    var ele = document.getElementById(x+"_explain");
    ele.style.display = "none";
    var exe = document.getElementById(x+"_execute");
    exe.style.display = "none";
}
function hidden(){
    var ele = document.getElementById("toggleText");
    var text = document.getElementById("displayText");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "show";
    }
    else {
        ele.style.display = "block";
        text.innerHTML = "hide";
    }
}