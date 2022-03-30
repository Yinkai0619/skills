let p1 = new Promise(function (resolve, reject) {
    setTimeout(() => {
        // resolve('ok.');     // fulfilled
        console.log("~~~~~~~~~~~~~~~~~~~~~~~~")
        reject('bad.')      // rejected
        console.log("~~~~~~~~~~~~~~~~~~~~~~~~")
    }, 3000);
})

// console.log("==========================")
// console.log(p1)

// setTimeout(() => {
//    console.log(p1) 
// }, 5000);

p1.then(
    value => console.log(1, value)
    // ,
    // reason => console.log(2, reason) 
).then(
    value => console.log(4, value)
    ,
    reason => console.log(5, reason) 
)

// p1.catch(reason => console.log(3, reason))

console.log('---------------------------------')