// var parts = ['shoulder', 'knees'];
// var lyrics = ['head', ...parts, 'and', 'toes'];
// console.log(lyrics)

// function f(x, y, z) {
//     console.log(x + y + z)
// }
// let args = [2, 3, 4];
// f(...args)

// // let [a,b,c,d] = ['Li', 'Yinkai', 'Nana'];
// // let [a,b,...c] = ['Li', 'Yinkai', 'Nana', 'love'];
// // let [a,,,...c] = ['Li', 'Yinkai', 'Nana', 'love'];
// let [a=100,,,,,,,c=200] = ['Li', 'Yinkai', 'Nana', 'love'];
// console.log(a);
// // console.log(b)
// console.log(c)
// // console.log(d)

// const obj = {
//     a:1,
//     b:2,
//     c:3
// }

// var {a,b} = obj;
// console.log(a,b);

// var {a:m,b:n,c,d:x=200} = obj;
// console.log(m,n,c,x);


// let [a,[b,c],d] = [1,[2,3],4];
// let [a,...d] = [1,[2,3],4];
// console.log(a,d)

// var metadata = {
//     title: "Scratchpad",
//     translations: [
//         {
//             locale: "de",
//             localization_tags: [],
//             last_edit: "2014-04-14T08:43:37",
//             url: "/de/docs/Tools/Scratchpad",
//             title: "JavaScript-Umgebung"
//         }
//     ],
//     url: "/en-US/docs/Tools/Scratchpad"
// };
// //
// // var { title: enTitle, translations: [{ title: localeTitle }] } = metadata;
// // console.log(enTitle); // "Scratchpad"
// // console.log(localeTitle);
// // "JavaScript-Umgebung"
// // console.log(metadata.title, metadata.translations[0].title);
// // const {title, translations} = metadata;
// // console.log(title, translations)
// const {title:t1, translations:[{title:t2}]} = metadata;
// console.log(t1,'\n',t2)

const arr = [1,3,5,7,9];
// console.log(arr.map(x => x + 10))
// console.log(arr.filter(x => x > 5))
// console.log(arr.forEach(x => console.log(x)))
let newarr = [];
// console.log(arr.forEach(x => {
//     newarr.push(x * 2)
// }))
console.log(arr.forEach((x,y,z) => {
    console.log(x); //element
    console.log(y); //index
    // console.log(z); //arr
    console.log()

    newarr[y] = x * 2;
}))
console.log(newarr)