const Serialization = Sup => class extends Sup {
    constructor (...args) {
        super(...args);
        console.log('serialization ~~~~~~~~~~~')
        console.log(this, typeof(this), 'ttttttttttt');
        if (typeof(this.stringify) !== 'function') {
            throw new ReferenceError("Should define stringify.");
        }
    }
}


class Point {
    constructor(x,y) {
        console.log('Point ~~~~~~~~~~~')
        this.x = x;
        this.y = y;
    };
}


class Point3D extends Serialization(Point) {
    constructor (x,y,z) {
        super(x,y);
        console.log('Point3D ~~~~~~~~~~~')
        this.z = z;
    };

    stringify () {console.log(this.x, this.y, this.z, '==========')};
};


p3d = new Point3D(3,4,5);
p3d.stringify();
console.log(p3d, typeof(p3d));