let name = 'nana'
let school = {
    name: 'yinkai',
    getNameFunc: function () {
        console.log(this.name);
        console.log(this);
        return function() {
            console.log(this === global);
            return this.name;
        }
    }
}

// console.log(school.getNameFunc()(school))
console.log(school.getNameFunc().call(school))