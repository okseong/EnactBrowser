// 연산 1
console.log(7 / 2);		// 3.5
console.log(15 % 4);	// 3
console.log(5 % 1.5);	// 0.5

console.log(1234 + 'coins')		// 1234coins(string)
console.log('first' + 'second') // firstsecond

console.log(0 / 0)		// NaN
console.log("one" * 1)	// NaN
console.log(1 + undefined)	// NaN

console.log(true + true)	// 2
console.log(1 + null)		// 1

// 연산 2
var a = 10
console.log(--a);	// 9
console.log(a++);	// 9
console.log(-a);	// -10

// 문자열 연산
var str = 'asdf';
console.log(str);		// asdf
console.log(str[0]);	// a
console.log(str[str.length-1]);	// f
var n = 999;
console.log(n.toString());	// 999

// 연산 3
console.log(null == undefined);	// true
console.log(1 == '1');			// true
console.log('0xff' == 255);		// true
console.log(true == 1);			// true
console.log(true == '1');		// true
console.log([2] == 2);			// true

// 연산 4
var str = 'abc';
console.log(typeof(str));		// string
console.log(typeof(1));			// number
console.log(typeof(true));		// boolean
function f() {};
console.log(typeof(f));					// function
console.log(typeof([1, 2]));	// object
console.log(typeof({x: 3}));	// object

// eval
var a = 9;
eval('a++;');
console.log(a);		// 10
var cmd = 'function f(a) { return a * a * a; }; console.log(f(a));'
eval(cmd);			// 1000
