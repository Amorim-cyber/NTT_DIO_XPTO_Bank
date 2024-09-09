class ElementController{
    status = "menu";
    data_index = 1;

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

    async input_user_data(){

        var caixa_texto = document.getElementById("caixa_texto");
        var botao_ok = document.getElementById("botao_ok");
        var status_ = document.getElementById("status_");

        await new Promise(r => setTimeout(r, 10));
        caixa_texto.value = '';

        switch(this.data_index){
            case 1:
                caixa_texto.setAttribute('type','text');
                botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=1\)');         
                break;
            case 2:
                caixa_texto.setAttribute('type','date');
                botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=2\)');         
                break;
            case 3:
                caixa_texto.setAttribute('type','number');
                botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=3\)');         
                break;
            case 4:
                caixa_texto.setAttribute('type','text');
                if(status_.innerHTML == 1){ this.turn_back(botao_ok);}
                else {botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=4\)'); }        
                break;
            case 5:
                botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=5\)');         
                break;
            case 6:
                botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=6\)');         
                break;
            case 7:
                botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=7\)');         
                break;
            case 9:
                botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=8\)');
                break;
            case 10:
                if(status_.innerHTML == 1){ this.turn_back(botao_ok); return;}
                else{botao_ok.setAttribute('py-click','banco.cadastrar_dado\(tipo\=9\)');}
                break;
        }

        if (this.data_index==8 || this.data_index==11){
            this.clear();
            this.data_index = 1;
        }else{
            this.status = 'data_msg';
            this.data_index++;
        }
        
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

    turn_back(botao_ok){
        botao_ok.setAttribute('py-click','banco.voltar\(\)');
        this.status = 'standard_msg';
        status_.innerHTML = '0';
        this.data_index = 1;
        caixa_texto.setAttribute('type','number');
    }

    async active(){

        var caixa_texto = document.getElementById("caixa_texto");
        var option = caixa_texto.value;

        await new Promise(r => setTimeout(r, 10));
        switch(this.status){

            case 'menu':
                switch(option){
                    case '0':
                        this.exit();
                        break;
                    case '1':
                    case '4':
                        this.clear();
                        break;
                    case '2':
                        this.input_value(1);
                        break;
                    case '3':
                        this.input_value(2);
                        break;
                    case '5':
                        this.input_user_data();
                        break;
                    case '6':
                        this.data_index = 9;
                        this.input_user_data();
                        break;
                    default:
                        this.error();
                }
                break;
            case 'standard_msg':
                caixa_texto.setAttribute('type','number');
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
                break;
            case 'data_msg':
                this.input_user_data();
                break;
        }

       
    }

}

let control = new ElementController();