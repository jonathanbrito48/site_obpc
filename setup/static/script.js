$(document).ready(function(){
    $('.slick-carousel').slick({
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,         // Ativa o modo de reprodução automática
        autoplaySpeed: 5000,    // Define o intervalo de tempo em milissegundos entre os slides
        responsive: [
            {
                breakpoint: 768, // Define o breakpoint desejado
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true,
                    adaptiveHeight: true, // Isso ajustará automaticamente a altura conforme a largura
                }
            }
            // Adicione mais blocos responsive conforme necessário para outros breakpoints
        ]
    });
});

$(document).ready(function(){
    $('.youtube_videos').slick({
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 4,
        slidesToScroll: 3,
        autoplay: true,         // Ativa o modo de reprodução automática
        autoplaySpeed: 5000,    // Define o intervalo de tempo em milissegundos entre os slides
        responsive: [
            {
                breakpoint: 1024, // Define o breakpoint desejado
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    adaptiveHeight: true, // Isso ajustará automaticamente a altura conforme a largura
                }
            }
            // Adicione mais blocos responsive conforme necessário para outros breakpoints
        ]
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.carousel');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    let isDragging = false;
    let startX;
    let scrollLeft;
    let movementFactor = 1.5; // Ajuste para aumentar a sensibilidade do arrasto

    // Função para rolar para a esquerda (com botão)
    function scrollLeftButton() {
        carousel.scrollBy({
            left: -300, // Valor fixo para os botões
            behavior: 'smooth'
        });
    }

    // Função para rolar para a direita (com botão)
    function scrollRightButton() {
        carousel.scrollBy({
            left: 300, // Valor fixo para os botões
            behavior: 'smooth'
        });
    }

    // Event listeners para os botões
    prevButton.addEventListener('click', scrollLeftButton);
    nextButton.addEventListener('click', scrollRightButton);

    // Iniciar o arrasto com o mouse
    carousel.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.pageX - carousel.offsetLeft; // Posição inicial do clique
        scrollLeft = carousel.scrollLeft; // Posição atual do scroll
        carousel.classList.add('dragging');
    });

    // Detectar o movimento do mouse em tempo real
    carousel.addEventListener('mousemove', (e) => {
        if (!isDragging) return; // Só mover se estiver arrastando
        e.preventDefault(); // Prevenir seleção de texto
        const x = e.pageX - carousel.offsetLeft; // Posição atual do mouse
        const walk = (x - startX) * movementFactor; // Multiplicar pelo fator de movimento
        carousel.scrollLeft = scrollLeft - walk; // Atualiza a posição do scroll
    });

    // Finalizar o arrasto com o mouse
    document.addEventListener('mouseup', () => {
        isDragging = false;
        carousel.classList.remove('dragging');
    });

    // Finalizar o arrasto ao sair da área
    carousel.addEventListener('mouseleave', () => {
        isDragging = false;
        carousel.classList.remove('dragging');
    });

    // Iniciar o arrasto em dispositivos móveis (toque)
    carousel.addEventListener('touchstart', (e) => {
        isDragging = true;
        startX = e.touches[0].pageX - carousel.offsetLeft; // Posição inicial do toque
        scrollLeft = carousel.scrollLeft; // Posição atual do scroll
        carousel.classList.add('dragging');
    });

    // Detectar o movimento do toque em tempo real
    carousel.addEventListener('touchmove', (e) => {
        if (!isDragging) return; // Só mover se estiver arrastando
        const x = e.touches[0].pageX - carousel.offsetLeft; // Posição atual do toque
        const walk = (x - startX) * movementFactor; // Multiplicar pelo fator de movimento
        carousel.scrollLeft = scrollLeft - walk; // Atualiza a posição do scroll
    });

    // Finalizar o arrasto no toque
    carousel.addEventListener('touchend', () => {
        isDragging = false;
        carousel.classList.remove('dragging');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const videoLinks = document.querySelectorAll('.instagram-link');

    videoLinks.forEach(link => {
        const video = link.parentElement.querySelector('.post-video');
        
        if (video) {
            // Reproduzir o vídeo ao passar o mouse sobre a âncora
            link.addEventListener('mouseover', function() {
                video.play();
            });

            // Pausar o vídeo quando o mouse sair da âncora
            link.addEventListener('mouseout', function() {
                video.pause();
                video.currentTime = 0; // Reiniciar o vídeo quando o mouse sair
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const toggles = document.querySelectorAll('[data-toggle="submenu"]');

    toggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault(); // Impede o comportamento padrão do link

            const parentLi = this.parentElement;

            // Verifica se o submenu já está ativo
            if (parentLi.classList.contains('active')) {
                parentLi.classList.remove('active');
            } else {
                // Fecha todos os submenus abertos
                document.querySelectorAll('.menu-list li.active').forEach(activeLi => {
                    activeLi.classList.remove('active');
                });

                // Abre o submenu clicado
                parentLi.classList.add('active');
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.dropdown');
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const menuItems = document.querySelector('.menu_options_items');

    // Toggle para submenus em dispositivos móveis
    dropdowns.forEach(function (dropdown) {
        const dropdownSelect = dropdown.querySelector('.dropdown-select');
        
        dropdownSelect.addEventListener('click', function (event) {
            event.preventDefault();
            const isOpen = dropdown.classList.contains('show');
            dropdowns.forEach(d => {
                d.classList.remove('show');
                d.querySelector('.dropdown-options').style.maxHeight = null; // Fechar todos os submenus
            });

            if (!isOpen) {
                dropdown.classList.add('show');
                dropdown.querySelector('.dropdown-options').style.maxHeight = dropdown.querySelector('.dropdown-options').scrollHeight + 'px'; // Abrir o submenu clicado
            }
        });
    });
});