var startLink = '', 
    endLink = '', 
    myScript = '';

function autocomplete(data) {
  var box = document.activeElement;
  var val = box.value;
  closeAll();
  if (data.length > 0) {
    for (var i = 0; i < data[1].length; i++) {
      var b = document.createElement("div");
      b.innerHTML = "<strong>" + data[1][i].substr(0, val.length) + "</strong>";
      b.innerHTML += data[1][i].substr(val.length);
      b.innerHTML += "<input type='hidden' value='" + data[1][i] + "'>";
      b.innerHTML += "<span style='display: none'>" + data[3][i] + "</span>";
      b.addEventListener("click", function(e) {
          box.value = this.getElementsByTagName("input")[0].value;
          closeAll();
          if (box.id == 'startBox') {
            startLink = this.getElementsByTagName("span")[0].innerHTML;
          } else if (box.id == 'endBox') {
            endLink = this.getElementsByTagName("span")[0].innerHTML;
          }
      });
      document.getElementById(box.id + '-autocomplete').appendChild(b);
    }
  }
}

function closeAll() {
  var auto = document.getElementsByClassName('autocomplete');
  for (var i=0; i < auto.length; i++) {
    while (auto[i].firstChild) auto[i].removeChild(auto[i].firstChild);
  }
}

function getSearchData(query) {
  if (myScript !== '') document.body.removeChild(myScript) ;
  myScript = document.createElement('script'); // this is the script that will hold the data we're trying to get 
  myScript.src = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=' + query + '&namespace=&limit=10&suggest=true&callback=autocomplete'; // http://en.wikipedia.org/w/api.php?action=opensearch&limit=10&format=json&callback=autocomplete&search=
  document.body.appendChild(myScript);  // this attaches the script to the body of the page
};

function search() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // do something
      console.log('submitted links');
    }
  };
  xhttp.open("POST", `/search`, true);
  xhttp.send([startLink, endLink]);
}


$(document).ready(function () {
  var startBox = document.getElementById('startBox');
  startBox.addEventListener("keyup", () => getSearchData(startBox.value));
  startBox.addEventListener("focus", () => getSearchData(startBox.value));
  var endBox = document.getElementById('endBox');
  endBox.addEventListener("keyup", () => getSearchData(endBox.value));
  endBox.addEventListener("focus",  () => getSearchData(endBox.value)); // loop this

  document.addEventListener("click", function (e) {
    if (!$('input').is(':focus')) closeAll();
  });
});





// function autoaslfk(box, arr) {
//   var currentFocus;
//   var a, b, i, val = this.value;
//   closeAllLists();
//   if (!val) { return false; }
//   a = document.createElement("DIV");
//   a.setAttribute("id", this.id + "autocomplete-list");
//   a.setAttribute("class", "autocomplete-items");
//   /*append the DIV element as a child of the autocomplete container:*/
//   this.parentNode.appendChild(a);

//   for (i = 0; i < arr.length; i++) {
//     /*check if the item starts with the same letters as the text field value:*/
//     if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
//       b = document.createElement("DIV");
//       b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
//       b.innerHTML += arr[i].substr(val.length);
//       b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
//       b.addEventListener("click", function(e) {
//           box.value = this.getElementsByTagName("input")[0].value;
//           closeAllLists();
//       });
//       a.appendChild(b);
//     }
//   }

//   box.addEventListener("keydown", function(e) {
//       var x = document.getElementById(this.id + "autocomplete-list");
//       if (x) x = x.getElementsByTagName("div");
//       if (e.keyCode == 40) {
//         /*If the arrow DOWN key is pressed */
//         currentFocus++;
//         /*and and make the current item more visible:*/
//         addActive(x);
//       } else if (e.keyCode == 38) { //up
//         /*If the arrow UP key is pressed */
//         currentFocus--;
//         /*and and make the current item more visible:*/
//         addActive(x);
//       } else if (e.keyCode == 13) {
//         /*If the ENTER key is pressed, prevent the form from being submitted,*/
//         e.preventDefault();
//         if (currentFocus > -1) {
//           /*and simulate a click on the "active" item:*/
//           if (x) x[currentFocus].click();
//         }
//       }
//   });

//   function addActive(x) {
//     /*a function to classify an item as "active":*/
//     if (!x) return false;
//     /*start by removing the "active" class on all items:*/
//     removeActive(x);
//     if (currentFocus >= x.length) currentFocus = 0;
//     if (currentFocus < 0) currentFocus = (x.length - 1);
//     /*add class "autocomplete-active":*/
//     x[currentFocus].classList.add("autocomplete-active");
//   }
//   function removeActive(x) {
//     /*a function to remove the "active" class from all autocomplete items:*/
//     for (var i = 0; i < x.length; i++) {
//       x[i].classList.remove("autocomplete-active");
//     }
//   }

//   function closeAllLists(elmnt) {
//     var x = document.getElementsByClassName("autocomplete-items");
//     for (var i = 0; i < x.length; i++) {
//       if (elmnt != x[i] && elmnt != box) {
//         x[i].parentNode.removeChild(x[i]);
//       }
//     }
//   }
// }
