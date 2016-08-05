var camera, scene, renderer;
var mesh;

init();
animate();

function init() {

    camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );
    camera.position.z = 400;

    scene = new THREE.Scene();

    mesh = jointBody()
    scene.add( mesh );

    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

    window.addEventListener( 'resize', onWindowResize, false );

}

function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

}

function animate() {

    requestAnimationFrame( animate );

    //mesh.rotation.x += 0.01;
    mesh.rotation.y += 0.01;

    renderer.render( scene, camera );

}

function erf(x, start, finish, smoothness) {
    x = - x + (start + finish)/2
    x = smoothness * x / (start - finish)

    // save the sign of x
    var sign = (x >= 0) ? 1 : -1;
    x = Math.abs(x);

    // constants
    var a1 =  0.254829592;
    var a2 = -0.284496736;
    var a3 =  1.421413741;
    var a4 = -1.453152027;
    var a5 =  1.061405429;
    var p  =  0.3275911;

    // A&S formula 7.1.26
    var t = 1.0/(1.0 + p*x);
    var y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
    return (sign * y + 1)/2; 
}


function mainBody() {
    
    var material = new THREE.MeshNormalMaterial();

    var h = Math.ceil(Math.random()*60 + 40)
    var segs = 10
    var fat = h/10
    var comps = 4
    var creature = true

    h -= 1
    geometry = new THREE.CylinderGeometry( 3, 3, h*5, segs, h );

    var f = function(x, cut) {
        if (x < cut) return erf(x, 0, cut, 6)
        else return erf(1-x, 0, 1-cut, 6)
    }

    var cuts = []
    var sizes = []
    var sum = 0
    for (i = 0; i < comps; i++) {
        cuts.push(Math.random())
        var size = Math.random()*0.5 + 0.2
        sizes.push(size)
        sum += size
    }

    var sumf = function(x) {
        var out = 0
        for (var i = 0; i < comps; i++) {
            out += f(x, cuts[i])*sizes[i]
        }
        return out / sum
    }

    
    var idx = 0
    for (i = 0; i < h+1; i++) {
        var Ypos = geometry.vertices[idx].y

        var shift = fat*sumf(i/h)
        for (j = 0; j < segs; j++) {
            var vertex = geometry.vertices[idx]
            
            vertex.setY(0)

            vertex.multiplyScalar(shift) 
            if (creature) vertex.addScaledVector(new THREE.Vector3(1.5,0,0), shift)
            vertex.setY(Ypos)
            
            idx += 1
        }
    }


    var mesh = new THREE.Mesh( geometry, material );
    if (creature) mesh.rotation.z -= 1;

    return mesh
}


function jointBody() {
    
    var material = new THREE.MeshNormalMaterial();

    var h = Math.ceil(Math.random()*60 + 40)
    var segs = 30
    
    geometry = new THREE.CylinderGeometry( 3, 3, h*5, segs, h );

    var joints = 3
    var jointdata = []
    var totlength = 0
    for (var i = 0; i < joints; i++) {
        var rand1 = Math.random()
        var rand2 = Math.random()
        var max = 0
        for (j = 0; j < h+1; j++) {
            var x = j/h
            var val =  -x*(x-1)*(x*x + rand1)*(x*x + rand2)
            if (val > max) max = val
        }


        var size = Math.random()*10 + 20
        var length = Math.random()*0.6 + 0.4

        totlength += length
        jointdata.push({
            rand1: rand1,
            rand2: rand2,
            size: size/max,
            length: length,
        })
    }

    


    var jointf = function(x, i) {
        var start = 0
        for (var j = 0; j < i; j++) {
            start += jointdata[j].length/totlength
        }
        var end = start + jointdata[i].length/totlength

        if (start > 0.1*jointdata[i].length/totlength) start -= 0.1*jointdata[i].length/totlength

        if (x < start || x > end) return 0

        var z = (x - start)/(end-start)

        return -z*(z-1)*(z*z + jointdata[i].rand1)*(z*z + jointdata[i].rand2)*jointdata[i].size
    }

    var idx = 0
    for (i = 0; i < h+1; i++) {
        var Ypos = geometry.vertices[idx].y
        var shift = 0
        for (var j = 0; j < joints; j++) {
            shift += jointf(i/h, j)
        }

        for (j = 0; j < segs; j++) {
            var vertex = geometry.vertices[idx]
            vertex.setY(0)
            vertex.multiplyScalar(shift) 
            vertex.setY(Ypos)
            idx += 1
        }
    }
    
    var mesh = new THREE.Mesh( geometry, material );
    //mesh.rotation.z = Math.PI/2
    return mesh

}
