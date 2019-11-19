var slider1 = document.getElementById("range1");
var output1 = document.getElementById("range1_value");
output1.innerHTML = slider1.value;

function servo1() {
output1.innerHTML = slider1.value;
var xhttp1 = new XMLHttpRequest();
xhttp1.onreadystatechange = function servo1() {
  if (this.readyState == 4 && this.status == 200) {

  }
};
xhttp1.open("GET", "http://raspberrypi:8181/set_servo1?speed=" + slider1.value, true);
xhttp1.send();
}

var slider2 = document.getElementById("range2");
var output2 = document.getElementById("range2_value");
output2.innerHTML = slider2.value;

function servo2() {
output2.innerHTML = slider2.value;
var xhttp2 = new XMLHttpRequest();
xhttp2.onreadystatechange = function servo2() {
  if (this.readyState == 4 && this.status == 200) {
  }
};
xhttp2.open("GET", "http://raspberrypi:8181/set_servo2?speed=" + slider2.value, true);
xhttp2.send();
}

var slider3 = document.getElementById("range3");
var output3 = document.getElementById("range3_value");
output3.innerHTML = slider3.value;
function servo3() {
  output3.innerHTML = slider3.value;
  var xhttp3 = new XMLHttpRequest();
  xhttp3.onreadystatechange = function servo3() {
    if (this.readyState == 4 && this.status == 200) {
    }
  };
  xhttp3.open("GET", "http://raspberrypi:8181/set_servo3?speed=" + slider3.value, true);
  xhttp3.send();
}

var slider4 = document.getElementById("range4");
var output4 = document.getElementById("range4_value");
output4.innerHTML = slider4.value;
function servo4() {
  output4.innerHTML = slider4.value; var xhttp4 = new XMLHttpRequest();
  xhttp4.onreadystatechange = function servo4() {
    if (this.readyState == 4 && this.status == 200) {
    }
  };
  xhttp4.open("GET", "http://raspberrypi:8181/set_servo4?speed=" + slider4.value, true);
  xhttp4.send();
}

var slider5 = document.getElementById("range5");
var output5 = document.getElementById("range5_value");
output5.innerHTML = slider5.value;
