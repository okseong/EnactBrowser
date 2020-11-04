// 'square' 함수 생성
function square(x) {
	return x * x;
}
var square = function(x) {
 return x * x;
}

// 'square' 함수 실행
console.log(square(3)) 		// 9
console.log(square(-1))		// 1

// 'p', 'q' 객체 생성
var p = {x: 0, y: 0};
var q = {x: 3, y: 4};

// 'dist' 함수 생성
function dist(p, q) {
	var dx = q.x - p.x;
	var dy = q.y - p.y;
	return Math.sqrt(dx*dx, dy*dy);
}
var dist = function(p, q) {
	var dx = q.x - p.x;
	var dy = q.y - p.y;
	return Math.sqrt(dx*dx, dy*dy);
}

// 'dist' 함수 실행
console.log(dist(p, q))		// 5

// 전역변수, 지역변수
var a = 'global';
function f() {
	var a = 'local';
	console.log(a);		// local
}
f();
console.log(a);			// global

// 메서드 : 객체의 프로퍼티 중에서 함수 객체의 참조를 값으로 갖고 있는 프로퍼티
var circle = {
	center: { x:0, y;0 },
	radius: 3,
	area: function() {
		return Math.PI * this.radius * this.radius;
		// this 는 현재 객체(circle)를 가리킴
	}
}
console.log(circle.area())	// 9 * 3.141592...
circle.radius = 2
console.log(circle.area())	// 4 * 3.141592...