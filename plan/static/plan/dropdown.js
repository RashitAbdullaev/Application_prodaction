$('.dropdown').click(function () {

        $(this).toggleClass("active")
        $(this).find('.dropdown-menu').slideToggle(300);
});

$('.dropdown').focusout(function () {
    $(this).toggleClass("active")
    $(this).find('.dropdown-menu').slideUp(300);
});

$('.dropdown .dropdown-menu li').click(function () {
    $(this).parents('.dropdown').find('span').text($(this).text());
    $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
});

/*End Dropdown Menu*/


