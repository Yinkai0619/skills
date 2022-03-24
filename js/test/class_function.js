// ES6之前：
function Point (x,y) {
    this.x = x;
    this.y = y;
    console.log(this);
    this.show = function () {console.log(this.x, this.y)}
}


function Point3D (x,y,z) {
    Point.call(this,x,y);
    this.z = z;
    this.show = function () {console.log(this.x, this.y, this.z)};
};

p3d = new Point3D(3,4,5);
console.log(111111,p3d, typeof(p3d));
p3d.show();

