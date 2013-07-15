var sqadd = function(x){
	var s = 0;
	while (x){
		var d = x%10;
		s+=d*d;
		x = Math.floor(x/10);
	}
	return s;
}

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

var test = function(N){
	while (1){
		N = sqadd(N);
		if (N==1){ return 0;}
		if (N==89){ return 1;}
	}
}
var s=0;
for (var i=1;i<10000000;i++){s+=test(i);}
alert(s);