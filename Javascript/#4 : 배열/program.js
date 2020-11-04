// 'a' 라는 빈 배열 생성
var a = [];

// 배열에 값 할당
a[1] = 11;
a[2] = 22;
a[5] = 55;
console.log(a);		// [empty, 11, 22, empty x 2, 55]

// 배열은 객체를 흉내낸것
a[10] = 1010;
console.log(a[10]);	// 1010
console.log(a['10']);	// 1010

// 배열의 'length' 프로퍼티는 배열 요소의 최대 인덱스 값+1 을 가지고 있음
console.log(a.length);	// 11
a[100] = 100100;
console.log(a.length);	// 101

// 'b' 라는 배열 생성
var b = [1, 2];

// push 메서드
b.push(['D']);
console.log(b);		// [1, 2, Array(1)]
console.log(b[2]);	// D

// delete 메서드
delete b[1];
console.log(b);		// [1, empty, Array(1)]
console.log(b[1]);	// undefined

