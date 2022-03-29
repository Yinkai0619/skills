class Serialization {
    constructor () {
        console.log('serialization ~~~~~~~~~~~')
        if (typeof(this.stringify) !== 'function') {
            throw new ReferenceError("Should define stringify.");
        }
    }
}


class Point extends Serialization {
    constructor(x,y) {
        super();
        console.log('Point ~~~~~~~~~~~')
        this.x = x;
        this.y = y;
        // this.show = function () {console.log("point show")}
    };

    show () {
        console.log(this.x, this.y);
    }

    stringify () {
        console.log('-----------')
    };
}

// a = new Point(4,5);
// console.log(a);
// a.stringify();
// console.log(Point)

class Point3D extends Point {
    constructor (x,y,z) {
        super(x,y);
        console.log('Point3D ~~~~~~~~~~~')
        this.z = z;
        // this.show = function () {console.log("p3d show")}
        // this.show = () => console.log("p3d show");
    };

    stringify () {console.log(this.x, this.y, this.z, '==========')};
};


p3d = new Point3D(3,4,5);
p3d.stringify();
console.log(p3d, typeof(p3d));