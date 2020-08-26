var jQueryScript = document.createElement('script');  
jQueryScript.setAttribute('src','https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js');
document.head.appendChild(jQueryScript);

walletaddress = ""
data2= {}
var mainstore = window.localStorage;
mainstore.setItem("wltaddr","0");

//key = 0 to check if loggedin or not


String.prototype.replaceAll = function(str1, str2, ignore) 
{
    return this.replace(new RegExp(str1.replace(/([\/\,\!\\\^\$\{\}\[\]\(\)\.\*\+\?\|\<\>\-\&])/g,"\\$&"),(ignore?"gi":"g")),(typeof(str2)=="string")?str2.replace(/\$/g,"$$$$"):str2);
} 
some = 0
setInterval(function(){ 
  if(some!=0){
    var gamevarstate =  data2["gameState"].replaceAll('"','*');
  console.log("Testing: "+JSON.stringify(gamevarstate));

  $.ajax({
    type: "POST",  
    url: "http://localhost:8000/setitem/",
    data: {"gameState" : JSON.stringify(gamevarstate),
            "wltaddr" : String(mainstore.getItem("wltaddr"))},
    success: function(){
      console.log("Success POST")
    },
    error: function(){
      console.log("POST failed")
    }
    });

  }
  some = 2
  
}, 20000);


  


function renderList(data) {
alert(data);
}


function bestScoreSave(){
  //code to save blockchain 
}

//to send to sqlite left

//etimer = gamestate
//ltime = getBestScore //on blockchain

window.fakeStorage = {
  

  //if else according to ids .... i.e from sqlite or blockchain
//position
  setItem: function (id, val) {
      //console.log("setting some value: "+String(val)+" with id:"+String(id));
      
      return data2[id] = String(val);
    
  },
 
  //best score fetching
  getItem: function (id) {
    if(String(id)=="gameState"){
      console.log(mainstore.getItem("wltaddr"));
        $.ajax({
          type: 'GET',
          async: false,
          url: "http://127.0.0.1:8000/getitem/",
          data: {"wltaddr" : String(mainstore.getItem("wltaddr"))},
          
          success:  function(data){
            var gamestatevar = String(data).replaceAll('*','"');
            console.log("getting data from server: "+gamestatevar.slice(1,-1));
            alert("geting from the server: "+gamestatevar.slice(1,-1));
            data2[id] = String(gamestatevar.slice(1,-1));
            
            console.log("getting some value: "+data2[id]+" with id:"+String(id) );
   
            }
            });

            return data2[id]
    }
    else{
      console.log("getting some value: "+data2[id]+" with id:"+String(id) );
      return data2.hasOwnProperty(id) ? data2[id] : undefined;
    }
    
  },

  removeItem: function (id) {
    $.ajax({
      type: 'GET',
      async: false,
      url: "http://127.0.0.1:8000/getitem/",
      data: {"wltaddr" : String(mainstore.getItem("wltaddr"))},
      
      success:  function(data){
        var gamestatevar = String(data).replaceAll('*','"');
        console.log("getting data from server: "+gamestatevar.slice(1,-1));
        alert("geting from the server: "+gamestatevar.slice(1,-1));
        data2[id] = String(gamestatevar.slice(1,-1));
        
        console.log("getting some value: "+data2[id]+" with id:"+String(id) );

        }
        });
    return delete data2[id];
  },

  clear: function () {
    return data2 = {};
  }
};

function LocalStorageManager() {
  this.bestScoreKey     = "bestScore";
  this.gameStateKey     = "gameState";

  var supported = this.localStorageSupported();
  this.storage = window.fakeStorage; //supported ? window.localStorage : 
}

LocalStorageManager.prototype.localStorageSupported = function () {
  var testKey = "test";

  try {
    var storage = window.localStorage;
    storage.setItem(testKey, "1");
    storage.removeItem(testKey);
    return true;
  } catch (error) {
    return false;
  }
};

// Best score getters/setters
LocalStorageManager.prototype.getBestScore = function () {
  return this.storage.getItem(this.bestScoreKey) || 0;
};

LocalStorageManager.prototype.setBestScore = function (score) {
  this.storage.setItem(this.bestScoreKey, score);
};

// Game state getters/setters and clearing
LocalStorageManager.prototype.getGameState = function () {
  var stateJSON = this.storage.getItem(this.gameStateKey);
  alert("state: "+stateJSON);
  return stateJSON ? JSON.parse(stateJSON) : null;
};

LocalStorageManager.prototype.setGameState = function (gameState) {
  this.storage.setItem(this.gameStateKey, JSON.stringify(gameState));
};

LocalStorageManager.prototype.clearGameState = function () {
  this.storage.removeItem(this.gameStateKey);
};

