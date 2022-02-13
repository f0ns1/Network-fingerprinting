function openNav() {
  document.getElementById("bar").style.width = "250px";
}

function closeNav() {
  document.getElementById("bar").style.width = "0";
}



function changeScan() {
  hidden_all()
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
    var object =["Network-scan","Port-scan","OS-detection","FW-detection","Banner-grabbing","DNS-detection","HTTP-header","IPV6-Scan"]
    for (x in object){
        var ele = document.getElementById(object[x]+"_explain");
        if(ele){
            ele.style.display = "none";
        }
        var exe = document.getElementById(object[x]+"_execute");
        if(exe){
            exe.style.display = "none";
        }
    }
}
