/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
function fact(n) {
  if (n <= 1) {
      return 1;
  }
  else {
      return n * fact(n - 1);
  }
}
function fib(n) {
  if (n == 0) {
      return 0;
  }
  else if (n <= 2) {
      return 1;
  }
  else {
      return fib(n - 1) + fib(n - 2);
  }
}

function gcd(a, b) {
  if (a == b) {
    return a;
  }
  var small = Math.max(a, b) / 2;
  var ans  = 1;
  for (let i = 1; i <= small; i++) {
      if (a % i == 0 && b % i == 0) {
          ans = i;
      }
  }
  return ans;

}
var div1 = document.getElementById('div1');
var div2 = document.getElementById('div2');
var div3 = document.getElementById('div3');
var g  = document.getElementById('gcd');
var fi  = document.getElementById('fib');
var fa  = document.getElementById('fact');
g.addEventListener('click', function() {div1.innerHTML = gcd(Math.floor(Math.random() * 100), Math.floor(Math.random() * 100))});
fi.addEventListener('click', function() {div2.innerHTML = fib(Math.random() * 10)});
fa.addEventListener('click', function() {div3.innerHTML = fact(Math.random() * 10)})

//insert your implementations here for...
// FIB
// FAC
// GCD
//element.remove(), element.InnerHTML
//element.appendChild(<ELEMENT>)
//element.addEventListener(<EVENT>, <FUNCTION>)