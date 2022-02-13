function network_scan_execute(){
    var x = document.getElementById("Network-scan_form").elements;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/networkscan");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("Network-scan_response").innerHTML =
            this.responseText;
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value}
    xmlhttp.send(JSON.stringify(obj1));
}

function port_scan_execute(){
    var x = document.getElementById("Port-scan_form").elements;
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/networkscan");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("Port-scan_response").innerHTML =
            this.responseText;
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value}
    xmlhttp.send(JSON.stringify(obj1));

}

function ipv6_scan_execute(){
    alert("ipv6")
    var x = document.getElementById("IPV6-Scan_form").elements;
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/ipv6scan");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("IPV6-Scan_response").innerHTML =
            JSON.stringify(this.responseText);
            alert(this.responseText)
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value, timeout : x[2].value}
    xmlhttp.send(JSON.stringify(obj1));
}

function http_header_execute(){
    var x = document.getElementById("HTTP-header_form").elements;
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/httpheader");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("HTTP-header_response").innerHTML =
            this.responseText;
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value, path : x[2].value }
    xmlhttp.send(JSON.stringify(obj1));

}

function dns_detection_execute(){
    var x = document.getElementById("DNS-detection_form").elements;
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/dnsdetection");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("DNS-detection_response").innerHTML =
            this.responseText;
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value, dns_ip : x[2].value}
    xmlhttp.send(JSON.stringify(obj1));

}

function banner_grabbing_execute(){
    var x = document.getElementById("Banner-grabbing_form").elements;
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/bannergrabbing");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("Banner-grabbing_response").innerHTML =
            this.responseText;
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value, ports : x[2].value}
    alert(obj1)
    xmlhttp.send(JSON.stringify(obj1));

}

function fw_detection_execute(){
    var x = document.getElementById("FW-detection_form").elements;
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/fwdetection");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("FW-detection_response").innerHTML =
            this.responseText;
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value, ports: x[2].value}
    xmlhttp.send(JSON.stringify(obj1));

}

function os_detection_execute(){
    var x = document.getElementById("OS-detection_form").elements;
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.open("POST", "http://127.0.0.1:8000/api/operations/networkscan");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 201) {
            document.getElementById("OS-detection_response").innerHTML =
            this.responseText;
       }
    }
    var obj1 = { operation : x[0].value, target_ip : x[1].value}
    xmlhttp.send(JSON.stringify(obj1));

}
