// Modal
    $('.card__btn').click(function(e) {
            e.preventDefault();
        $('#exampleModal').arcticmodal(
        );
        a=document.getElementById("modal-card"+$(this).attr('id'));
        $('.modal-card').addClass('d-none');
        $(a).removeClass('d-none');
    })