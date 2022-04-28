class Point {
    constructor(x,y) {
        this.x = x;
        this.y = y;
        this.show = function () {console.log("point show")}
    };

    // show () {
    //     console.log(this.x, this.y);
    // }
}

// a = new Point(4,5);
// console.log(a);
// a.show();
// console.log(Point)

class Point3D extends Point {
    constructor (x,y,z) {
        super(x,y);
        this.z = z;
        // this.show = function () {console.log("p3d show")}
        // this.show = () => console.log("p3d show");
    };

    show () {console.log(this.x, this.y, this.z)};
};


p3d = new Point3D(3,4,5);
p3d.show();
console.log(p3d, typeof(p3d));