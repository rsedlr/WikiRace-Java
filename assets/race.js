var dataSav = [];

function autocomplete(data, new=true) {
  console.log(dataSav);
  dataSav = data;
  var box = document.getElementById("searchbox");
  var focus = -1;
  var val = box.value;
  // console.log(data[1]);
  if (new) closeAll();
  if (data.length > 0) {
    for (var i = 0; i < data[1].length; i++) {
      var b = document.createElement("div");
      b.innerHTML = "<strong>" + data[1][i].substr(0, val.length) + "</strong>";
      b.innerHTML += data[1][i].substr(val.length);
      b.innerHTML += "<input type='hidden' value='" + data[1][i] + "'>";
      b.addEventListener("click", function(e) {
          box.value = this.getElementsByTagName("input")[0].value;
          closeAll();
      });
      document.getElementById('autocomplete').appendChild(b);
    }
  }
}

function closeAll() {
  var auto = document.getElementById('autocomplete');
  while (auto.firstChild) auto.removeChild(auto.firstChild); // wipes board
}

$(document).ready(function () {

  var myScript = '';
  var box = document.getElementById('searchbox');

  box.onkeyup = function() {
    if (myScript !== '') document.body.removeChild(myScript) ;
    var query = document.getElementById('searchbox').value; // this variable stores whatever is in the input text box
    myScript = document.createElement('script'); // this is the script that will hold the data we're trying to get 
    myScript.src = 'http://en.wikipedia.org/w/api.php?action=opensearch&limit=10&format=json&callback=autocomplete&search=' + query; // this sets the src of the script equal to the url of the data
    document.body.appendChild(myScript);  // this attaches the script to the body of the page
  };
  box.onfocus = function() { console.log('focus') ; autocomplete(dataSav, false); }
  // box.addEventListener("focus", autocomplete(dataSav));

  document.addEventListener("click", function (e) {
    closeAll();
  });
});



function autoaslfk(box, arr) {
  var currentFocus;
  var a, b, i, val = this.value;
  closeAllLists();
  if (!val) { return false; }
  a = document.createElement("DIV");
  a.setAttribute("id", this.id + "autocomplete-list");
  a.setAttribute("class", "autocomplete-items");
  /*append the DIV element as a child of the autocomplete container:*/
  this.parentNode.appendChild(a);

  for (i = 0; i < arr.length; i++) {
    /*check if the item starts with the same letters as the text field value:*/
    if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
      b = document.createElement("DIV");
      b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
      b.innerHTML += arr[i].substr(val.length);
      b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
      b.addEventListener("click", function(e) {
          box.value = this.getElementsByTagName("input")[0].value;
          closeAllLists();
      });
      a.appendChild(b);
    }
  }
  /*execute a function presses a key on the keyboard:*/
  box.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });

  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }

  function closeAllLists(elmnt) {
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != box) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
}
