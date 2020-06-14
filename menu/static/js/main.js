// Подсветка пункта меню активной страницы
$(function () {
    $('#slow-down li a').each(function () {
    var location = window.location.href
    var link = this.href
    var result = location.match(link);
    if(result != null) {
    $(this).addClass('active');
    }
    });
    });

// Modal
    $('.card__btn').click(function(e) {
            e.preventDefault();
        $('#exampleModal').arcticmodal(
        );
        a=document.getElementById("modal-card"+$(this).attr('id'));
        $('.modal-card').addClass('d-none');
        $(a).removeClass('d-none');
    })

// Menu opener hamburger
    $('.menu-open').click(function () {
        $('.menu-collapse').toggleClass('d-none');
        $('.nav').toggleClass('menu-opened');

    });







