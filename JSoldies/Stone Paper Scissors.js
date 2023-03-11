let enough = enough

let A = Math.floor(Math.random()*3);
let B = Math.floor(Math.random()*3);

function handA() {let C;
if (A===0){C ='Scissors'}
else if (A===1){C ='Stone'}
else if (A===2){C ='Paper'}
else {C='Invalid'};
return C};

function handB() {let D;
if (B===0){D='Scissors'}
else if (B===1){D='Stone'}
else if (B===2){D='Paper'}
else {D='Invalid'};
return D};

let C = handA()
let D = handB()

console.log('player1 : '+C)
console.log('player2 : '+D)

function comparing(){
    if (C===D){enough='It is a Tie!'}
  else if (C==='Scissors'&&D==='Paper'){enough='player1 wins!'}
  else if (C==='Paper'&&D==='Stone'){enough='player1 wins!'}
  else if (C==='Stone'&&D==='Scissors'){enough='player1 wins!'}
  else if (D==='Scissors'&&C==='Paper'){enough='player2 wins!'}
  else if (D==='Paper'&&C==='Stone'){enough='player2 wins!'}
  else if (D==='Stone'&&C==='Scissors'){enough='player2 wins!'};
return enough}

console.log(comparing())






