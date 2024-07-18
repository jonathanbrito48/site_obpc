document.addEventListener('DOMContentLoaded', function () {
    const h1Element = document.getElementById('movingText');

    // Defina a posição para onde você deseja mover o texto e o novo tamanho (Segunda Animação)
    const novaPosicao = {
        top: -450, // Modifique conforme necessário
        right: -1060, // Modifique conforme necessário
        fontSize: 50 // Modifique conforme necessário
    };

    // Primeira Animação: Mudança gradual na cor do background
    h1Element.style.transition = 'background-color 3s ease-in-out';
    h1Element.style.backgroundColor = '#00000000';

    // Aguarde 3 segundos (duração da primeira animação) antes de iniciar a segunda animação
    setTimeout(function () {
        // Segunda Animação: Mova o texto para a nova posição e ajuste o tamanho durante o movimento
        h1Element.style.transition = 'all 3s ease-in-out';
        h1Element.style.transform = `translate(${novaPosicao.right}px, ${novaPosicao.top}px)`;
        h1Element.style.fontSize = novaPosicao.fontSize + 'px';
    }, 3000); // 3000 milissegundos = 3 segundos (duração da primeira animação)
});
