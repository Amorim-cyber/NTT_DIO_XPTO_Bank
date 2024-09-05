class ElementController{
    status = "menu";

    exit(){

        var caixa_texto = document.getElementById("caixa_texto");
        var botao_ok = document.getElementById("botao_ok");

        caixa_texto.style.display = 'none';
        botao_ok.hidden = true;
    }

    async return(){

        var caixa_texto = document.getElementById("caixa_texto");
        var botao_ok = document.getElementById("botao_ok");

        await new Promise(r => setTimeout(r, 10));
        caixa_texto.value = '';
        botao_ok.setAttribute('py-click','banco.executar_controle\(\)');
        this.status = 'menu';
    }

    async input_value(type){
        var caixa_texto = document.getElementById("caixa_texto");
        var botao_ok = document.getElementById("botao_ok");

        await new Promise(r => setTimeout(r, 10));
        caixa_texto.value = '';
        if (type == 1){
            botao_ok.setAttribute('py-click','banco.sacar_valor\(\)');
        }else{
            botao_ok.setAttribute('py-click','banco.depositar_valor\(\)');
        }
        
        this.status = 'standard_msg';
    }

    async clear(){

        var caixa_texto = document.getElementById("caixa_texto");
        var botao_ok = document.getElementById("botao_ok");

        await new Promise(r => setTimeout(r, 10));
        caixa_texto.value = '';
        botao_ok.setAttribute('py-click','banco.voltar\(\)');
        this.status = 'standard_msg';

    }

    async error(){

        var caixa_texto = document.getElementById("caixa_texto");
        var botao_ok = document.getElementById("botao_ok");

        await new Promise(r => setTimeout(r, 10));
        caixa_texto.value = '';
        botao_ok.setAttribute('py-click','banco.voltar\(\)');
        this.status = 'standard_msg';
    }

    active(){

        var caixa_texto = document.getElementById("caixa_texto");

        var option = caixa_texto.value;

        switch(this.status){

            case 'menu':
                switch(option){
                    case '0':
                        this.exit();
                        break;
                    case '1':
                        this.clear();
                        break;
                    case '2':
                        this.input_value(1);
                        break;
                    case '3':
                        this.input_value(2);
                        break;
                    default:
                        this.error();
                }
                break;
            case 'standard_msg':
                switch(option){
                    case '0':
                        this.exit();
                        break;
                    case '1':
                        this.return();
                        break;
                    default:
                        this.error();
                }
        }

       
    }

}

let control = new ElementController();