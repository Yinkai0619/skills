let p1 = new Promise(function (resolve, reject) {
    setTimeout(() => {
    //    resolve('ok') // value
       console.log('~~~~~~~~~~~~~~~~~~')
       reject('bad')    // reason
       console.log('~~~~~~~~~~~~~~~~~~')
    }, 3000);
})

console.log('==========================')
console.log(p1)

// setTimeout(() => {
//     console.log(p1)
// }, 5000);

p1.then(
    value => {
        console.log(1, value);
        return Promise.reject(value + '!')
    },
    reason => {
        console.log(2, reason);
        return Promise.reject('ok~~')
    }
).catch(reason => console.log(5, reason))
// .then(
//     value => console.log(3, value),
//     reason => console.log(4, reason)
// )

// p1.catch(
//     reason => console.log(reason)
// )
console.log('--------------------------')