

const poltronas = document.querySelectorAll(".c");
 console.log(poltronas);
    poltronas.forEach(function(poltrona) {
        
        poltrona.addEventListener('click', function() {
            console.log("pourra");
            
            const poltronaSelecionado = document.querySelector('.selecionado');
            poltronaSelecionado.classList.remove('selecionado');
            poltronaSelecionado.classList.add('c');
            poltrona.classList.add('selecionado');

          
        })
      })
    
            
           
       

    
    
    function removerSelecaoDoPoltrona() {
        const poltronaSelecionado = document.querySelector('.selecionado');
        poltronaSelecionado.classList.remove('selecionado');
        
    }