
const Player = (name, mark) => {
    const getMark = () => mark;
    const setMark = () => {
        let count = 0;
        const grid = document.querySelectorAll('.item');
        grid.forEach(gridbox => gridbox.addEventListener('click', e =>{
            if(count > 0){
                return;
            }
            if(gridbox.textContent.length === 0){
                gridbox.textContent = mark;
                count++;
                gameFlow.checkResult();
                
                
                    
            }
            
            
            }) )
        
    } 
    const hasWon = () => `${this.name} has won the game!`;
    return {setMark, hasWon, getMark};
}



const gameFlow = (() => {
    
    const startGame = () => {
        
        clear();
        for(let i=0; i<5; i++){
            player1.setMark();
            player2.setMark();
        }
            
        
    }
    const clear = () => {
        const grid = document.querySelectorAll('.item');
        grid.forEach(gridbox => gridbox.textContent = "");
    }
    const checkResult = () => {
        //p1 hor lines/
        console.log('im here');
        if(document.getElementById('0').textContent === player1.getMark() && 
        document.getElementById('1').textContent === player1.getMark() && 
        document.getElementById('2').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        else if(document.getElementById('3').textContent === player1.getMark() && 
        document.getElementById('4').textContent === player1.getMark() && 
        document.getElementById('5').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        else if(document.getElementById('6').textContent === player1.getMark() && 
        document.getElementById('7').textContent === player1.getMark() && 
        document.getElementById('8').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        //p1 ver lines/
        else if(document.getElementById('0').textContent === player1.getMark() && 
        document.getElementById('3').textContent === player1.getMark() && 
        document.getElementById('6').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        else if(document.getElementById('1').textContent === player1.getMark() && 
        document.getElementById('4').textContent === player1.getMark() && 
        document.getElementById('7').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        else if(document.getElementById('2').textContent === player1.getMark() && 
        document.getElementById('5').textContent === player1.getMark() && 
        document.getElementById('8').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        //p1 diagon lines
        else if(document.getElementById('0').textContent === player1.getMark() && 
        document.getElementById('4').textContent === player1.getMark() && 
        document.getElementById('8').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        else if(document.getElementById('2').textContent === player1.getMark() && 
        document.getElementById('4').textContent === player1.getMark() && 
        document.getElementById('6').textContent === player1.getMark()){
            alert(player1.hasWon);
            clear();
        }
        //p2 hor lines/
        else if(document.getElementById('0').textContent === player2.getMark() && 
        document.getElementById('1').textContent === player2.getMark() && 
        document.getElementById('2').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        else if(document.getElementById('3').textContent === player2.getMark() && 
        document.getElementById('4').textContent === player2.getMark() && 
        document.getElementById('5').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        else if(document.getElementById('6').textContent === player2.getMark() && 
        document.getElementById('7').textContent === player2.getMark() && 
        document.getElementById('8').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        //p2 ver lines/
        else if(document.getElementById('0').textContent === player2.getMark() && 
        document.getElementById('3').textContent === player2.getMark() && 
        document.getElementById('6').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        else if(document.getElementById('1').textContent === player2.getMark() && 
        document.getElementById('4').textContent === player2.getMark() && 
        document.getElementById('7').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        else if(document.getElementById('2').textContent === player2.getMark() && 
        document.getElementById('5').textContent === player2.getMark() && 
        document.getElementById('8').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        //p2 diagon lines
        else if(document.getElementById('0').textContent === player2.getMark() && 
        document.getElementById('4').textContent === player2.getMark() && 
        document.getElementById('8').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        else if(document.getElementById('2').textContent === player2.getMark() && 
        document.getElementById('4').textContent === player2.getMark() && 
        document.getElementById('6').textContent === player2.getMark()){
            alert(player2.hasWon);
            clear();
        }
        else if (document.getElementById('0').textContent.length !==0 &&
        document.getElementById('1').textContent.length !==0 &&
        document.getElementById('2').textContent.length !==0 &&
        document.getElementById('3').textContent.length !==0 &&
        document.getElementById('4').textContent.length !==0 &&
        document.getElementById('5').textContent.length !==0 &&
        document.getElementById('6').textContent.length !==0 &&
        document.getElementById('7').textContent.length !==0 &&
        document.getElementById('8').textContent.length !==0 ){
           
            alert("it's a draw");
            clear();
        }
    }
    return {startGame, checkResult};
})();

const player1 = Player('tom', 'x');
const player2 = Player('mark', 'o');


