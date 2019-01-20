/**
 * Created by a on 10/04/16.
 */
Snap.plugin(function (Snap, Element, Paper, glob) {
    Paper.prototype.multitext = function (x, y, txt, max_width, attributes) {

        var svg = Snap();
        var abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        var temp = svg.text(0, 0, abc);
        temp.attr(attributes);
        var letter_width = temp.getBBox().width / abc.length;
        svg.remove();

        var words = txt.split(" ");
        var width_so_far = 0, current_line=0, lines=[''];
        for (var i = 0; i < words.length; i++) {

            var l = words[i].length;
            if (width_so_far + (l * letter_width) > max_width) {
                lines.push('');
                current_line++;
                width_so_far = 0;
            }
            width_so_far += l * letter_width;
            lines[current_line] += words[i] + " ";
        }

        var t = this.text(x,y,lines).attr(attributes);
        t.selectAll("tspan:nth-child(n+2)").attr({
            dy: "1.2em",
            x: x
        });
        return t;
    };
});

/*
window.onload = function () {
    var s = Snap("#snapsvg")
    //var s = Snap(800, 600);
    var bobo = s.paper.multitext(50, 50, "Tom found 18 gems. Esther found 2 gems. How many gems did they find in total?", 700,
        { "font-size": "30px" });

    var answer_rect = s.paper.rect(70, 120, 60, 50);
    answer_rect.attr({
        fill: 'coral',
        stroke: 'black',
        strokeWidth: 0.5
    });

// regular rectangle
var rect1 = s.paper.rect(20, 200, 50, 50);
var text1 = s.paper.text(20, 230, "1")
var rect2 = s.paper.rect(70, 200, 30, 50);
var text2 = s.paper.text(70, 230, "2")
var rect3 = s.paper.rect(100, 200, 50, 50);
var text3 = s.paper.text(100, 230, "3")
var rect4 = s.paper.rect(150, 200, 80, 50);
var text4 = s.paper.text(150, 230, "4")

rect1.attr({
    fill: 'coral',
    stroke: 'black',
    strokeWidth: 1
});

rect2.attr({
    fill: 'lightblue',
    stroke: 'black',
    strokeWidth: 1
});

rect3.attr({
    fill: 'mediumturquoise',
    stroke: 'black',
    strokeWidth: 1
});

rect4.attr({
    fill: 'red',
    stroke: 'black',
    strokeWidth: 1
});










};

*/



