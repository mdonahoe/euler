var fisherYates = function ( myArray ) {
  var i = myArray.length;
  if ( i == 0 ) return false;
  while ( --i ) {
     var j = Math.floor( Math.random() * ( i + 1 ) );
     var tempi = myArray[i];
     var tempj = myArray[j];
     myArray[i] = tempj;
     myArray[j] = tempi;
   }
}
Number.prototype.mod = function(n) {
	return ((this%n)+n)%n;
}
var goto = function(y) { return function(x){ return y;}};
var noop = function(x){ return x;};

var chance = (function(){
	var nextrail = function(x){
		if (x<5) return 5;
		if (x<15) return 15;
		if (x<25) return 25;
		if (x<35) return 35;
		return 5;
	};
	var nextutil = function(x){
		if (x<12) return 12;
		if (x<28) return 28;
		return 12;
	};
	var backthree = function(x){ return (x-3).mod(40);}; 
	
	var cards = [
		noop,noop,noop,noop,noop,noop,
		goto(0),goto(10),goto(11),
		goto(24),goto(39),goto(5),
		nextrail,nextrail,nextutil,
		backthree
	];
	fisherYates(cards);
	return function(x){
		var c = cards.shift();
		var y = c(x);
		cards.push(c);
		return y;
	};
})();

var chest = (function(){
	
	var cards = [
		noop,noop,noop,noop,
		noop,noop,noop,noop,
		noop,noop,noop,noop,
		noop,noop,
		goto(0),goto(10)
	];
	fisherYates(cards);
	return function(x){
		var c = cards.shift();
		var y = c(x);
		cards.push(c);
		return y;
	};
})();

var dice = function(){
	return Math.floor(Math.random()*4)+1;
};
var map = function(xs,f) {
	var ys = [];
	for (var i in xs){
		ys.push(f(xs[i]));
	}
	return ys;
};
var range = function(N){
	var xs = [];
	for (var i=0;i<N;i++){ 
		xs.push(i);
	}
	return xs;
};
var sum = function(xs){ var s = 0; for (var i in xs){s+=xs[i];}; return s;};
var enumerate= function(xs){ var ys = []; for (var i in xs){ ys.push([i,xs[i]]);}; return ys;};

var roll = (function(){
	var doubles = 0;
	return function(x){
		var d1 = dice();
		var d2 = dice();
		if (d1==d2){
			doubles++;
		} else {
			doubles=0;
		}
		if (doubles==3){
			doubles = 0;
			return 10;
		}
		return (x+d1+d2).mod(40);
	};
})();
GO = JAIL = FP = RR = noop;
G2J = goto(10);
var board = [
	GO,noop,chest,noop,noop,RR,noop,chance,noop,noop,
	JAIL,noop,noop,noop,noop,RR,noop,chest,noop,noop,
	FP,noop,chance,noop,noop,RR,noop,noop,noop,noop,
	G2J,noop,noop,chest,noop,RR,chance,noop,noop,noop
];
var board2 = [
	noop,noop,noop,noop,noop,
	noop,noop,noop,noop,noop,
	noop,noop,noop,noop,noop,
	noop,noop,noop,noop,noop,
	noop,noop,noop,noop,noop,
	noop,noop,noop,noop,noop,
	noop,noop,noop,noop,noop,
	noop,noop,noop,noop,noop
];

var test = function(N){
	var stop = [];
	for (var i=0;i<40;i++){stop.push(0);}

	var x = 0;
	while (N--){
		x = roll(x);
		x = board[x](x);
		stop[x]++;
	}
	return stop;
}
var game = test(1000000);
var sorted = map(enumerate(game).sort(function(a,b){return b[1]-a[1];}),function(x){return x[0];});
alert(sorted.slice(0,3).join(''));