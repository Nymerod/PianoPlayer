
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
const notes_white = ["do1.wav", "re1.wav", "mi1.wav", "fa1.wav", "sol1.wav", "la1.wav", "si1.wav", "do2.wav", "re2.wav", "mi2.wav", "fa2.wav", "sol2.wav", "la2.wav", "si2.wav"]
const notes_black = ["dos1.wav", "res1.wav", "fas1.wav", "sols1.wav", "las1.wav", "dos2.wav", "res2.wav", "fas2.wav", "sols2.wav", "las2.wav"]


function recting() {
    let white = [];
    let black = [];
    for (let i = 0; i < 2; i++) { 
        for (let j = 0; j < 7; j++) {
            ctx.beginPath();
            const x = 100 + (i * 7 + j) * 55;
            const y = 200;
            ctx.beginPath();
            ctx.rect(x, y, 50, 150)
            ctx.stroke();
            white.push({x, y, width: 50, height: 150});
        
            if (j === 2 || j === 6) {
                
            } else {

                ctx.beginPath();
                const x = 130 + (i * 7 + j) * 55;
                const y = 200;
                ctx.fillstyle = "black";
                ctx.fillRect(x, y, 35, 100);
                ctx.stroke();
                black.push({x, y, width: 35, height: 100});
            }
        }


    }
    return { white, black };
}


function isInsideRect(x, y, rect) {
    return x > rect.x && x < rect.x + rect.width && y > rect.y && y < rect.y + rect.height;
}


canvas.addEventListener('click', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    let keyClicked = false; 

    for (const b of keys.black) {
        
        if (isInsideRect(x, y, b)) {

            console.log("Black key clicked" , keys.black.indexOf(b))
            let audio = new Audio("./assets/" + notes_black[keys.black.indexOf(b)]);
            audio.play();
            keyClicked = true;
            break;
        }

    }

    if (! keyClicked){
        for (const w of keys.white) {
            if (isInsideRect(x, y, w)) {
                let audio = new Audio("./assets/" + notes_white[keys.white.indexOf(w)])
                audio.play();
                break;
            }

        }
        document.addEventListener("keypress", function onEvent(event) {
            const hotkeys_white = ["w", "x", "c", "v", "b", "n", ",", "y", "u","i","o","p","^","$"]
            for (let i = 0; i < hotkeys_white.length; i++ ) {
                if (event.key === (hotkeys_white[i])) {
                    let audio = new Audio(notes_white[i]);
                    audio.play();


                }

            }
            if (event.key === "ArrowLeft") {

            }
           
        });
    
    }});
let keys = recting();
