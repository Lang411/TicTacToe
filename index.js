$(document).ready(function(){
	
	$("#reset").click(function resetfunction(){
		location.reload(); 
	});
	
	function win(board,symbol){
		//quick and dirty win function
		var a = false;
		wincondition = [0,1,2];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		wincondition = [3,4,5];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		wincondition = [6,7,8];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		wincondition = [0,3,6];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		wincondition = [1,4,7];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		wincondition = [2,5,8];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		wincondition = [0,4,8];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		wincondition = [2,4,6];
		if (board[wincondition[0]]==symbol && board[wincondition[1]]==symbol && board[wincondition[2]]==symbol){
			a = true
		}
		if (a===true){
		}
		
		return a
	}
		
	function AIPlayer(symbol,board,enemySymbol){
		console.log('---AI players turn---');
		dispXsTurn.innerHTML = '';
		dispOsTurn.innerHTML = '&larr; AIs Turn!';
		console.log('Board: '+board);
		var canAIWin = false;
		var canAIBlock = false;
		var AIchoice = -99;
		
		//checking to see if AI can win
		var tempboard = board;
		for (i=0;i<9;i++){
			if (tempboard[i]===''){
				tempboard[i]= symbol;
				//console.log(tempboard);
				if (win(tempboard,symbol)===true){
					console.log('AI can win');
					AIchoice = i+1;
					canAIWin = true;
				}
				tempboard[i]= '';
			}
		}
		//block win
		tempboard = board;
		for (i=0;i<9;i++){
			if (tempboard[i]==='' && canAIWin===false){
				tempboard[i]= enemySymbol;
				//console.log(tempboard);
				if (win(tempboard,enemySymbol)===true){
					console.log('Player can win - Blocking:');
					AIchoice = i+1;
					canAIBlock = true;
				}
				tempboard[i]= '';
			}
		}
		
		//Neither are true so picking a random location
		if (canAIWin === false && canAIBlock===false){
			var crashavoid = 0
			while(AIchoice===-99 && crashavoid<100){
				var tempAIchoice = Math.floor(Math.random()*9)+1;
				console.log('AI clicked the '+tempAIchoice);
				if (board[tempAIchoice-1]===''){
					AIchoice = tempAIchoice;
				}
			crashavoid++
			}
		}

		board[AIchoice-1] = symbol;
			
		if (AIchoice === 1){
			one.innerHTML = symbol;
		}
		if (AIchoice === 2){
			two.innerHTML = symbol;
		}
		if (AIchoice === 3){
			three.innerHTML = symbol;
		}
		if (AIchoice === 4){
			four.innerHTML = symbol;
		}
		if (AIchoice === 5){
			five.innerHTML = symbol;

		}
		if (AIchoice === 6){
			six.innerHTML = symbol;
		}
		if (AIchoice === 7){
			seven.innerHTML = symbol;
		}
		if (AIchoice === 8){
			eight.innerHTML = symbol;
		}
		if (AIchoice === 9){
			nine.innerHTML = symbol;
		}
		dispXsTurn.innerHTML = 'Players Turn! &rarr;';
		dispOsTurn.innerHTML = '';
		if (win(board,symbol)===true){
			console.log('-----------------'+symbol+' Wins!----------------');
			var sound = 'file:///C:/Users/lkenney/Desktop/CODE/Simon%20Says/Assets/sounds/Correct-answer.mp3';
			var audio = new Audio(sound);
			audio.play();
			dispOsTurn.innerHTML = symbol+' Wins!';
			dispXsTurn.innerHTML = symbol+' Wins!';
		}
		
		boardfull = board.filter(function (value) {
			if (value == 'X' || value == 'O'){
				return true
			}
		}).length;
		if (boardfull === 9){
			//$( this ).switchClass('col-md-12', 'btn col-md-12');
			dispOsTurn.innerHTML = 'Tie - Game over';
			dispXsTurn.innerHTML = 'Tie - Game over';
			
			console.log('------Game Over-----');
			var sound = 'file:///C:/Users/lkenney/Desktop/CODE/Simon%20Says/Assets/sounds/Sad_Trombone-Joe_Lamb-665429450.mp3';
			var audio = new Audio(sound);
			audio.play();
		}
		
		return board
	}
	
	function humanPlayer (clk,symbol,board){
			console.log('You clicked the '+clk+1);
			if (board[clk]===''){
				board[clk] = symbol;
				if (win(board,symbol)===true){
					console.log('-----------------'+symbol+' Wins!----------------');
					var sound = 'file:///C:/Users/lkenney/Desktop/CODE/Simon%20Says/Assets/sounds/Correct-answer.mp3';
					var audio = new Audio(sound);
					audio.play();
					dispOsTurn.innerHTML = symbol+' Wins!';
					dispXsTurn.innerHTML = symbol+' Wins!';
					
				}
				else{
					AIPlayer(AISymbol,board,playerSymbol);
				}
				console.log('Board: '+board);
			}
			else {
				AIPlayer(AISymbol,board,playerSymbol);
			}
	}
	
	
	$("#startRestartButton").click(function startfunction(){
		//$("#startButton").toggleClass('btn startbtn', 'btn disabled startbtn');
		startRestartButton.innerHTML = 'RESET';
		$("#startRestartButton").click(function startfunction(){
			location.reload(); 
		});
		//$("#reset").switchClass('btn btn-danger  col-md-12','btn btn-danger col-md-12')
		console.log('---Start Game---');
		//$("#startButton").toggleClass( "disabled" );
		var board = ['','','','','','','','',''];

		playerSymbol = 'X';
		AISymbol = 'O';
		
		var whostarts = Math.floor(Math.random()*2)+1;
		if (whostarts === 1){
			console.log('---AI players turn---');
			dispOsTurn.innerHTML = '&larr; Os Turn!';
			AIPlayer(AISymbol,board,playerSymbol);
		}
		else {
			console.log('---Players turn---');
			dispXsTurn.innerHTML = 'Players Turn! &rarr;';
		}
		//dispXsTurn.innerHTML = 'Xs Turn! &rarr;';
		//dispOsTurn.innerHTML = '&larr; Os Turn!';
		
		$("#one").bind("click", function(){
			clk = 0;
			one.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#two").bind("click", function(){
			clk = 1;
			two.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#three").bind("click", function(){
			clk = 2;
			three.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#four").bind("click", function(){
			clk = 3;
			four.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#five").bind("click", function(){
			clk = 4;
			five.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#six").bind("click", function(){
			clk = 5;
			six.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#seven").bind("click", function(){
			clk = 6;
			seven.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#eight").bind("click", function(){
			clk = 7;
			eight.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
		
		$("#nine").bind("click", function(){
			clk = 8;
			nine.innerHTML = playerSymbol;
			humanPlayer (clk,playerSymbol,board)
		});
	
	});
	

});
