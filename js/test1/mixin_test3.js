class A {
    constructor () {
        // if (typeof(this.show) === 'function') {
        //     console.log('ok')
        // } else {
        //     throw new ReferenceError('E1');
        // }
    };

    show () {};
}

// a = new A();

const A1 = class {
    constructor () {
        this.x = 100;
    }
}

// console.log(A,A1);
// console.log(new A1().x);

const B1 = class extends A1{
    constructor () {
        super()
        // this.x = 200;
    }
}

console.log(B1);
console.log(new B1().x);

const C = (Sup) => class extends Sup { }
const D = Sup => class extends Sup {};

let cls = D(A1);
let obj = new cls();
console.log(obj.x, "~~~~~")