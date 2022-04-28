
export default function () {
    console.log("foo function")
}

// foo()


// function * counter() {
//     let i = 0;
//     while(true) {
//         yield ++i;
//     }
// }

// g = counter();
// console.log(g.next().value);
// console.log(g.next().value);
// console.log(g.next().value);


class A {
    show() {
        console.log("class A.")
    }
}

const B = 2000;

export { A, B }