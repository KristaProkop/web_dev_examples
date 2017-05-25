
/*--------------------------------------------------
---------------DECK---------------------------------------------------------------------------------*/


function DeckConstructor(){
    this.makeDeck();
    this.reset = function() {
        this.makeDeck();
    }
}

DeckConstructor.prototype.makeDeck = function() {
    var suits = ["hearts", "spades", "diamonds", "clubs"]
    var ranks = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]

    function Card (rank, suit) {
        this.rank = rank;
        this.suit = suit;
    };

    this.deck = new Array(52);

    var i, j;
    for (i = 0; i < suits.length; i++) {
        for (j = 0; j < ranks.length; j++) {
            this.deck[i*ranks.length + j] = new Card(ranks[j], suits[i]);
        }
    }
    console.log(this)
    return this;
}

DeckConstructor.prototype.shuffle = function() {
    for (let i = this.deck.length; i; i--) {
        let j = Math.floor(Math.random() * i);
        [this.deck[i - 1], this.deck[j]] = [this.deck[j], this.deck[i - 1]];
    }
    console.log(this.deck);
    return this.deck;
}

DeckConstructor.prototype.dealCard = function() {
    var card;
    let i = Math.floor(Math.random() * (51 - 0)) + 0;
    card = this.deck[i];
    this.deck.splice(i, 1);
    console.log("Dealing card ", card);
    return card;
}


/*--------------------------------------------------
---------------PLAYER---------------------------------------------------------------------------------*/

function PlayerConstructor(name) {
    this.name = name;
    this.hand = [];
    this.dealHand();
}

PlayerConstructor.prototype.dealCard = function() {
    var card = deck.dealCard();
    this.hand.push(card);

    return this;
}

PlayerConstructor.prototype.dealHand = function() {
    for ( i=0; i < 2; i++ ) {
        this.dealCard();
    }
    return this;
}

PlayerConstructor.prototype.discardCard = function(card) {
    deck.deck.push(this.hand[card])
    this.hand.splice(card, 1)
    return this;
}

/*--------------------------------------------------
---------------HTML FUNCTIONS---------------------------------------------------------------------------------*/

var sum = 0;
var dealerHand = Math.floor(Math.random() * (21 - 14)) + 14;    

function startGame() {
    deck = new DeckConstructor();
}


function addScore(rank) {
    var points;
    if (rank == "k" || rank == "q" || rank == "j" || rank == "a") {
        points = 10;
    } else {
        points = Number(rank);
    }
    sum += points;
}


function playNow () {
    var el = document.querySelector('div');
    player = new PlayerConstructor();
    for (i=0; i < player.hand.length; i++) {
        var suit = (player.hand[i]['suit']);
        var rank = (player.hand[i]['rank']);
        addScore(rank);
        var src = suit[0]+rank;
        el.innerHTML += '<img id='+src+' src="cards-png/'+src+'.png"</img>';
    }
}


function reset(result) {
    var el = document.querySelector('div');
    var aside = document.querySelector('aside');
    sum = 0;
    el.innerHTML = "";
    aside.innerHTML = '';
}



function dealCard() {
    var div = document.querySelector('div');
    var aside = document.querySelector('aside');
    player.dealCard();
    var suit = (player.hand[player.hand.length-1]['suit']);
    var rank = (player.hand[player.hand.length-1]['rank']);

    var src = suit[0]+rank;
    div.innerHTML += '<img id='+src+' src="cards-png/'+src+'.png"</img>';
    addScore(rank); 
    if (sum == 21) {
        aside.innerHTML += '<h2>BLACKJACK</h2>'
    } if (sum > 21) {
        aside.innerHTML += '<h2>YOU LOSE</h2>'
    } 
    console.log(sum);
    return player.hand;
}

// deck = new DeckConstructor();
// player1 = new PlayerConstructor('bob');
// player1.dealCard().dealCard().dealCard();
// console.log("Player1 hand: ", player1.hand);
// player2 = new PlayerConstructor('mary')
// console.log("Player2 hand: ", player2.hand);
// player2.discardCard(0);
// console.log("Player2 hand after discard: ", player2.hand);
// player1.discardCard(0);
// console.log("Player1 hand after discard: ",player1.hand);
// console.log("Current deck ",deck.deck)




