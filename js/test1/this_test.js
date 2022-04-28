let name = 'nana'
// let school = {
//     name: 'yinkai',
//     getNameFunc: function () {
//         console.log(this.name);
//         console.log(this);
//         return () => {
//             console.log(this === global);
//             return this.name;
//         }
//     }
// }

// console.log(school.getNameFunc()(school))
// console.log(school.getNameFunc().call(school))
// console.log(school.getNameFunc().apply(school))
// console.log(school.getNameFunc().bind(school)())
// console.log(school.getNameFunc()())

class School {
    constructor () {
        this.name = 'nana';
    }

    getNameFunc () {
        console.log(this.name);
        console.log(this);
        return () => {
            console.log(this === global);
            console.log(this, '~~~~~~~~~');
            return this.name;
            // return name;
        };
    }
}


console.log(new School().getNameFunc()(),' love yinkai')