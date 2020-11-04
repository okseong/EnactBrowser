// 'suit', 'rank' 프로퍼티를 가지는 'card' 객체 생성
var card = { suit: '하트', rank: 'a' };

// 'card' 객체에서 'suit' 이라는 프로퍼티가 갖고 있는 값을 출력 
console.log(card.suit);		// 하트
console.log(card['suit']); 	// 하트

// 'card' 객체에서 'rank' 라는 프로퍼티가 갖고 있는 값을 출력
console.log(card.rank);		// a
console.log(card['rank']);	// a

// 'card' 객체 출력
console.log(card)		// {suit: "하트", rank: "a"}

// 프로퍼티를 가지고 있지 않은 'obj' 객체 생성
var obj = {};

// 'obj' 객체에 'a' 를 값으로 가지는 'A' 프로퍼티 추가
obj.A = 'a';
obj['A'] = 'a';

// 'obj' 객체에 [1, 2] 를 값으로 가지는 'B' 프로퍼티 추가
obj.B = [1, 2];
obj['B'] = [1, 2];

// 'obj' 객체 출력
console.log(obj);		// {A: "a", B: Array(2)}

// 프로퍼티 유무 확인
console.log('suit' in card)		// true
console.log('color' in card) 	// false
console.log('A' in obj)			// true
console.log('C' in obj)			// false