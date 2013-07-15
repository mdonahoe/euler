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

var powermod = function(x,y,n){
	var a = 1;
	for (var i=0;i<y;i++){
		a = a*x%n;
	}
	return a;
}

var d = [];
var N = 250;
var M = Math.pow(10,16);
for (var i=0;i<N;i++){d.push(0);}
for (var i=1;i<250251;i++){
	var x = powermod(i,i,N);
	var d2 = d.slice(0);
	for (var j=0;j<N;j++){
		var y = (x+j)%N;
		d2[y]=(d2[y]+d[j])%M; //too big, wont work
	}
	d2[x]+=1;
	d = d2.slice(0);
	if (i%1000==0) alert(i+':'+d[0]);
}
alert(d[0]);
alert(d);