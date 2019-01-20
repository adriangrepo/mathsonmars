/**
 * Created by a on 24/06/16.
 */

//var boolValues = [true, false]
//randomBooleanValue = Math.floor(Math.random() * boolValues.length + 1);
function initAnimation() {
    //if (randomBooleanValue) {
    window.onLoad = omgParticlesII ();
    //}
    //else {
        //var nodeNumber = randomIntFromInterval(5, 10);
        //untangle (nodeNumber);
    //quadPointTree()
    //}
}

function randomIntFromInterval(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}

function omgParticlesII(){
    console.log(">omgParticlesII()");
    var width = Math.max(960, innerWidth),
        height = Math.max(500, innerHeight);

    var x1 = width / 2,
        y1 = height / 2,
        x0 = x1,
        y0 = y1,
        i = 0,
        r = 200,
        τ = 2 * Math.PI;

    var canvas = d3.select(".activity_result_banner").append("canvas")
        .attr("width", width)
        .attr("height", height)
        .attr("position", "relative")
        .attr("z-index", "20")
        .on("ontouchstart" in document ? "touchmove" : "mousemove", move);

    var context = canvas.node().getContext("2d");
    context.globalCompositeOperation = "lighter";
    context.lineWidth = 2;

    d3.timer(function() {
        context.clearRect(0, 0, width, height);

        var z = d3.hsl(++i % 360, 1, .5).rgb(),
            c = "rgba(" + z.r + "," + z.g + "," + z.b + ",",
            x = x0 += (x1 - x0) * .1,
            y = y0 += (y1 - y0) * .1;

        d3.select({}).transition()
            .duration(2000)
            .ease(Math.sqrt)
            .tween("circle", function() {
                return function(t) {
                    context.strokeStyle = c + (1 - t) + ")";
                    context.beginPath();
                    context.arc(x, y, r * t, 0, τ);
                    context.stroke();
                };
            });
    });

    function move() {
        var mouse = d3.mouse(this);
        x1 = mouse[0];
        y1 = mouse[1];
        d3.event.preventDefault();
    }

}

function pathAnimation() {
    var w = 700;
    var h = 300;

    var svg = d3.select ("#line")
        .append ("svg")
        .attr ("width", w)
        .attr ("height", h)
        .attr ("id", "visualization")
        .attr ("xmlns", "http://www.w3.org/2000/svg");

    var data = d3.range (11).map (function () {
        return Math.random () * 10
    })
    var x = d3.scale.linear ().domain ([0, 10]).range ([0, 700]);
    var y = d3.scale.linear ().domain ([0, 10]).range ([10, 290]);
    var line = d3.svg.line ()
        .interpolate ("cardinal")
        .x (function (d, i) {
            return x (i);
        })
        .y (function (d) {
            return y (d);
        })

    var path = svg.append ("path")
        .attr ("d", line (data))
        .attr ("stroke", "steelblue")
        .attr ("stroke-width", "2")
        .attr ("fill", "none");

    var totalLength = path.node ().getTotalLength ();

    path
        .attr ("stroke-dasharray", totalLength + " " + totalLength)
        .attr ("stroke-dashoffset", totalLength)
        .transition ()
        .duration (2000)
        .ease ("linear")
        .attr ("stroke-dashoffset", 0);

    svg.on ("click", function () {
        path
            .transition ()
            .duration (2000)
            .ease ("linear")
            .attr ("stroke-dashoffset", totalLength);
    })
}

function untangle(nodeNumber) {
    w = 960,
        h = 600,
        p = 15,
        x = d3.scale.linear ().range ([0, w]),
        y = d3.scale.linear ().range ([0, h]),
        start,
        format = d3.format (",.1f"),
        moves = 0,
        highlightIntersections = false,
        count = 0, // intersections
        graph = scramble (planarGraph (nodeNumber));

    d3.select ("#vis").selectAll ("*").remove ();

    vis = d3.select ("#vis").append ("svg")
        .attr ("width", w + p * 2)
        .attr ("height", h + p * 2)
        .append ("g")
        .attr ("transform", "translate(" + [p, p] + ")");

    lines = vis.append ("g"),
        nodes = vis.append ("g"),
        counter = d3.select ("#count"),
        moveCounter = d3.select ("#move-count"),
        timer = d3.select ("#timer");

    d3.select ("#generate").on ("click", generate);
    d3.select ("#intersections").on ("change", function () {
        highlightIntersections = this.checked;
        update ();
    });

    generate (nodeNumber);

    d3.timer (function () {
        if (count) timer.text (format ((+new Date - start) / 1000));
    });


    function generate(nodeNumber) {
        moves = 0;
        start = +new Date;
        lastCount = null;
        graph = scramble (planarGraph (nodeNumber));
        update ();
    }

    function update() {
        count = intersections (graph.links);
        counter.text (count ? count + "." : "0! Well done!");

        var line = lines.selectAll ("line")
            .data (graph.links);
        line.enter ().append ("line");
        line.exit ().remove ();
        line.attr ("x1", function (d) {
            return x (d[0][0]);
        })
            .attr ("y1", function (d) {
                return y (d[0][1]);
            })
            .attr ("x2", function (d) {
                return x (d[1][0]);
            })
            .attr ("y2", function (d) {
                return y (d[1][1]);
            })
            .classed ("intersection", highlightIntersections ? function (d) {
                return d.intersection;
            } : true);

        var node = nodes.selectAll ("circle")
            .data (graph.nodes);
        node.enter ().append ("circle")
            .attr ("r", p - 1)
            .call (d3.behavior.drag ()
                .origin (function (d) {
                    return {x: x (d[0]), y: y (d[1])};
                })
                .on ("drag", function (d) {
                    // Jitter to prevent coincident nodes.
                    d[0] = Math.max (0, Math.min (1, x.invert (d3.event.x))) + Math.random () * 1e-4;
                    d[1] = Math.max (0, Math.min (1, y.invert (d3.event.y))) + Math.random () * 1e-4;
                    update ();
                })
                .on ("dragend", function () {
                    moveCounter.text (++moves + " move" + (moves !== 1 ? "s" : ""));
                }));
        node.exit ().remove ();
        node.attr ("cx", function (d) {
            return x (d[0]);
        })
            .attr ("cy", function (d) {
                return y (d[1]);
            })
            .classed ("intersection", highlightIntersections ?
                function (d) {
                    return d.intersection;
                } : count);
    }

// Scramble the node positions.
    function scramble(graph) {
        if (graph.nodes.length < 4) return graph;
        do {
            graph.nodes.forEach (function (node) {
                node[0] = Math.random ();
                node[1] = Math.random ();
            });
        } while (!intersections (graph.links));
        return graph;
    }

// Generates a random planar graph with *n* nodes.
    function planarGraph(n) {
        var points = [],
            links = [],
            i = -1,
            j;
        while (++i < n) points[i] = [Math.random (), Math.random ()];
        i = -1;
        while (++i < n) {
            addPlanarLink ([points[i], points[~~(Math.random () * n)]], links);
        }
        i = -1;
        while (++i < n) {
            j = i;
            while (++j < n) addPlanarLink ([points[i], points[j]], links);
        }
        return {nodes: points, links: links};
    }

// Adds a link if it doesn't intersect with anything.
    function addPlanarLink(link, links) {
        if (!links.some (function (to) {
                return intersect (link, to);
            }))
        {
            links.push (link);
        }
    }

// Counts the number of intersections for a given array of links.
    function intersections(links) {
        var n = links.length,
            i = -1,
            j,
            x,
            count = 0;
        // Reset flags.
        while (++i < n) {
            (x = links[i]).intersection = false;
            x[0].intersection = false;
            x[1].intersection = false;
        }
        i = -1;
        while (++i < n) {
            x = links[i];
            j = i;
            while (++j < n) {
                if (intersect (x, links[j])) {
                    x.intersection =
                        x[0].intersection =
                            x[1].intersection =
                                links[j].intersection =
                                    links[j][0].intersection =
                                        links[j][1].intersection = true;
                    count++;
                }
            }
        }
        return count;
    }

// Returns true if two line segments intersect.
// Based on http://stackoverflow.com/a/565282/64009
    function intersect(a, b) {
        // Check if the segments are exactly the same (or just reversed).
        if (a[0] === b[0] && a[1] === b[1] || a[0] === b[1] && a[1] === b[0]) return true;

        // Represent the segments as p + tr and q + us, where t and u are scalar
        // parameters.
        var p = a[0],
            r = [a[1][0] - p[0], a[1][1] - p[1]],
            q = b[0],
            s = [b[1][0] - q[0], b[1][1] - q[1]];

        // Solve p + tr = q + us to find an intersection point.
        // First, cross both sides with s:
        //   (p + tr) Ã— s = (q + us) Ã— s
        // We know that s Ã— s = 0, so this can be rewritten as:
        //   t(r Ã— s) = (q âˆ’ p) Ã— s
        // Then solve for t to get:
        //   t = (q âˆ’ p) Ã— s / (r Ã— s)
        // Similarly, for u we get:
        //   u = (q âˆ’ p) Ã— r / (r Ã— s)
        var rxs = cross (r, s),
            q_p = [q[0] - p[0], q[1] - p[1]],
            t = cross (q_p, s) / rxs,
            u = cross (q_p, r) / rxs,
            epsilon = 1e-6;

        return t > epsilon && t < 1 - epsilon && u > epsilon && u < 1 - epsilon;
    }

    function cross(a, b) {
        return a[0] * b[1] - a[1] * b[0];
    }
}

function quadPointTree(){
    width = 960,
    height = 500;

    data = d3.range(5000).map(function() {
        return [Math.random() * width, Math.random() * width];
    });

    quadtree = d3.geom.quadtree()
        .extent([[-1, -1], [width + 1, height + 1]])
        (data);

    brush = d3.svg.brush()
        .x(d3.scale.identity().domain([0, width]))
        .y(d3.scale.identity().domain([0, height]))
        .extent([[100, 100], [200, 200]])
        .on("brush", brushed);

    svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);

    svg.selectAll(".node")
        .data(nodes(quadtree))
        .enter().append("rect")
        .attr("class", "node")
        .attr("x", function(d) { return d.x; })
        .attr("y", function(d) { return d.y; })
        .attr("width", function(d) { return d.width; })
        .attr("height", function(d) { return d.height; });

    point = svg.selectAll(".point")
        .data(data)
        .enter().append("circle")
        .attr("class", "point")
        .attr("cx", function(d) { return d[0]; })
        .attr("cy", function(d) { return d[1]; })
        .attr("r", 4);

    svg.append("g")
        .attr("class", "brush")
        .call(brush);

    brushed();

    function brushed() {
        var extent = brush.extent();
        point.each(function(d) { d.scanned = d.selected = false; });
        search(quadtree, extent[0][0], extent[0][1], extent[1][0], extent[1][1]);
        point.classed("scanned", function(d) { return d.scanned; });
        point.classed("selected", function(d) { return d.selected; });
    }

// Collapse the quadtree into an array of rectangles.
    function nodes(quadtree) {
        var nodes = [];
        quadtree.visit(function(node, x1, y1, x2, y2) {
            nodes.push({x: x1, y: y1, width: x2 - x1, height: y2 - y1});
        });
        return nodes;
    }

// Find the nodes within the specified rectangle.
    function search(quadtree, x0, y0, x3, y3) {
        quadtree.visit(function(node, x1, y1, x2, y2) {
            var p = node.point;
            if (p) {
                p.scanned = true;
                p.selected = (p[0] >= x0) && (p[0] < x3) && (p[1] >= y0) && (p[1] < y3);
            }
            return x1 >= x3 || y1 >= y3 || x2 < x0 || y2 < y0;
        });
    }
}