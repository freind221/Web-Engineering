let screen = document.getElementById('screen');
buttons = document.querySelectorAll('button');
let screenValue = '';
for (item of buttons) {
    item.addEventListener('click', (e) => {
        buttonText = e.target.innerText;
        console.log('Button text is ', buttonText);
        if (buttonText == 'X') {
            buttonText = '*';
            screenValue += buttonText;
            screen.value = screenValue;
        }
        else if (buttonText == 'C') {
            screenValue = "";
            screen.value = screenValue;
        }
        else if (buttonText == '=') {
            if(screen.value.search("^") != -1){
                let num = screen.value.split("^");
                screen.value=Math.pow(num[0], num[1]);
            }
            else if(screen.value.search("%") != -1){
                let num = screen.value.split("%");
                screen.value=num[0]%num[1];
            }
            else{
                screen.value = eval(screenValue);
            }
            
        }
        else if (buttonText == "sin") {
            var x = eval(screen.value);
            x = x * Math.PI / 180;
            screen.value = Math.sin(x);
            screenValue = screen.value
        }
        else if (buttonText == "cos") {
            var x = eval(screen.value);
            x = x * Math.PI / 180;
            screen.value = Math.cos(x);
            screenValue = screen.value
        }
        else if (buttonText == "tan") {
            var x = eval(screen.value);
            x = x * Math.PI / 180;
            screen.value = Math.tan(x);
            screenValue = screen.value
        }
        else if (buttonText == "lg2e") {
            var x = eval(screen.value);
           x = Math.LOG2E;
            screen.value =x;
            screenValue = screen.value
        }
        else if (buttonText == "L10e") {
            var x = eval(screen.value);
           x = Math.LOG10E;
            screen.value =x;
            screenValue = screen.value
        }
        else if (buttonText == "ln") {
            var x = eval(screen.value);
           x = Math.log10(x);
            screen.value =x;
            screenValue = screen.value
        }
        else if (buttonText == "log2") {
            var x = eval(screen.value);
            x =  Math.log2(x);
            screen.value =x;
            screenValue = screen.value
        }
        
        else if (buttonText == "loge") {
            var x = eval(screen.value);
            
            screen.value = Math.log(x);
            screenValue = screen.value
        }
        else if (buttonText == "exp") {
            var x = eval(screen.value);
            
            screen.value = Math.exp(x);
            screenValue = screen.value
        }
        else if (buttonText == "perc") {
            var x = eval(screen.value);
            x = x/100;
            screen.value = x;
            screenValue = screen.value
        }
        else if (buttonText == "sqrt") {
            var x = eval(screen.value);
            
            screen.value = Math.sqrt(x);
            screenValue = screen.value
        }
        else if (buttonText == "!") {
            var x = eval(screen.value);
            if(x<0)
            {
                screen.value = 'Error! Negative Number';
            }
            else if(x==0){
                screen.value = '1';
            }
            else{
                let fact = 1;
                for(i=1; i<=parseInt(x); i++){
                    fact*=i; 
                }
                screen.value = fact;
            }
            
        }
        else if (buttonText == "pi") {
            var x = eval(screen.value);
            x = Math.PI;
            screen.value =x;
            screenValue = screen.value
        }
        
            
            
        
        
        else {
            screenValue += buttonText;
            screen.value = screenValue;
        }

    })
}

