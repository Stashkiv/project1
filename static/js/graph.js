
 let randomVar = true;
 let a = 125;
 let yourMoney = 333;
 let countOfShare = 0;
 let displayCount = 0;

 var LOGIN = prompt("Login:","");

let url = 'http://127.0.0.1:5000/';

const xhr = new XMLHttpRequest();
xhr.open('GET',url)
xhr.responseType = 'json';
xhr.onload = function pr () {
    console.log(xhr.response);
    var obj = xhr.response;
    if (LOGIN == 'Arsen'){
        countOfShare =  Number(obj.countOfShare1);
        displayCount = Number(obj.countOfShare1);
        yourMoney = Number(obj.money1);
        document.getElementById("display-count").innerHTML = `Your count of this share:${displayCount}` ;
        document.getElementById("your-money").innerHTML = `Your money at that moment :${yourMoney.toFixed(4)}` ;
    }
    if (LOGIN == 'Sofia'){
        countOfShare =  Number(obj.countOfShare2);
        displayCount = Number(obj.countOfShare2);
        yourMoney = Number(obj.money2)
        document.getElementById("display-count").innerHTML = `Your count of this share:${displayCount}` ;
        document.getElementById("your-money").innerHTML = `Your money at that moment :${yourMoney.toFixed(4)}` ;
    }
}
xhr.send();
displayCount = Number(displayCount);

 document.getElementById("your-money").innerHTML = `Your money at that moment :${yourMoney.toFixed(4)}` ;
 document.getElementById("price-share").innerHTML = `Price share at that moment :${a.toFixed(4)}` ;
 document.getElementById("display-count").innerHTML = `Your count of this share:${displayCount}` ;
 setInterval(randomFunc,1500)
 function randomFunc(){
     a =  Math.random() * (125.5 - 124) + 124;
     document.getElementById("price-share").innerHTML = `Price share at that moment :${a.toFixed(4)}` ;

 }

 function buyShare(){
    let getCountShareBuy = document.getElementById('input-buy').value;
    getCountShareBuy = Number(getCountShareBuy);
    if (yourMoney > (a*getCountShareBuy)){
        yourMoney -= (a*getCountShareBuy);
        countOfShare+= getCountShareBuy;
        displayCount += getCountShareBuy;
        document.getElementById("your-money").innerHTML = `Your money at that moment :${yourMoney.toFixed(4)}` ;
        document.getElementById("display-count").innerHTML = `Your count of this share:${displayCount}` ;
    }

 }

 function sellShare(){
    let getCountShareSell = document.getElementById('input-sell').value;
    getCountShareSell = Number(getCountShareSell);
    if (getCountShareSell <= countOfShare)
    {
        yourMoney += a*countOfShare;
        countOfShare -= getCountShareSell;
        displayCount -= getCountShareSell;
        document.getElementById("your-money").innerHTML = `Your money at that moment :${yourMoney.toFixed(4)}` ;
        document.getElementById("display-count").innerHTML = `Your count of this share:${displayCount}` ;
    }
   
}




