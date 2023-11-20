function SendForWard() {
    fetch('/ForWard')
}

function SendBackWard() {
    fetch('/BackWard')
}

function SendRight() {
    fetch('/Right')
}

function SendLeft() {
    fetch('/Left')
}
function SendStop() {
    fetch('/Stop')
}


// ************************************************************************************************************
function SendValue() {
    var sliderValue = document.getElementById("speed").value;
    var speedNum = document.getElementById("speed-num");
    var speedCar = document.getElementById("speed-car");


    console.log(typeof(+sliderValue))
    fetch('/get_value', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({value: sliderValue})
    });
    speedNum.innerHTML = `${sliderValue} `
    if( +sliderValue < 50){
        speedCar.style.backgroundColor = "green"
    }
    else if(+sliderValue>50 && +sliderValue < 80){
        speedCar.style.backgroundColor = "blue"
    }
    else{
        speedCar.style.backgroundColor = "red"
    }

}