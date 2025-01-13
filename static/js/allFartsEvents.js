// Make filter submit on select
$('#id_category').change(function() {
    $('#er-fart-filter').submit();
});
$('#id_topic').change(function() {
    $('#er-fart-filter').submit();
});
$('#id_project').change(function() {
    $('#er-fart-filter').submit();
});

$('.fart-date').click(function() {
    $(this).siblings().toggleClass('fart-details-show');
});

$('#id_type_0').after('<i class="fa-solid fa-comment" id="comment-icon"></i>');
$('#id_type_1').after('<i class="fa-solid fa-ear-listen" id="audio-icon"></i>');
$('#id_type_2').after('<i class="fa-solid fa-camera" id="image-icon"></i>');
$('#id_type_3').after('<i class="fa-solid fa-link" id="link-icon"></i>');

function commentActive() {

    $('#comment-icon').toggleClass('type-icon-active');
}

function audioActive() {

    $('#audio-icon').toggleClass('type-icon-active');
}

function imageActive() {

    $('#image-icon').toggleClass('type-icon-active');
}

function linkActive() {

    $('#link-icon').toggleClass('type-icon-active');
}

$('#audio-icon').click(function() {
    if ($('#id_type_1').data('checked')) {
        $('#id_type_1').prop('checked', false);
    } else {
        $('#id_type_1').prop('checked', true);
    }
    audioActive()
    $('#er-fart-filter').submit();
})

$('#comment-icon').click(function() {
    if ($('#id_type_0').data('checked')) {
        $('#id_type_0').prop('checked', false);
    } else {
        $('#id_type_0').prop('checked', true);
    }
    commentActive();
    $('#er-fart-filter').submit();
})

$('#image-icon').click(function() {
    if ($('#id_type_2').data('checked')) {
        $('#id_type_2').prop('checked', false);
    } else {
        $('#id_type_2').prop('checked', true);
    }
    imageActive();
    $('#er-fart-filter').submit();
})

$('#link-icon').click(function() {
    if ($('#id_type_3').data('checked')) {
        $('#id_type_3').prop('checked', false);
    } else {
        $('#id_type_3').prop('checked', true);
    }
    linkActive();
    $('#er-fart-filter').submit();
})

$('#div_id_category').click(function() {
    let catOffset = $('#div_id_category').offset();
    let docHeight = $(window).height();
    console.log(docHeight);
    console.log(catOffset)
    $('.select2-results').css('height', ((docHeight - 76) - catOffset.top) + 'px')
    $('.select2-results__options').css('height', ((docHeight - 93) - catOffset.top) + 'px')
});

$('#div_id_topic').click(function() {
    let catOffset = $('#div_id_topic').offset();
    let docHeight = $(window).height();
    console.log(docHeight);
    console.log(catOffset)
    $('.select2-results').css('height', ((docHeight - 76) - catOffset.top) + 'px')
    $('.select2-results__options').css('height', ((docHeight - 93) - catOffset.top) + 'px')
});

$('#div_id_project').click(function() {
    let catOffset = $('#div_id_project').offset();
    let docHeight = $(window).height();
    console.log(docHeight);
    console.log(catOffset)
    $('.select2-results').css('height', ((docHeight - 76) - catOffset.top) + 'px')
    $('.select2-results__options').css('height', ((docHeight - 93) - catOffset.top) + 'px')
});


$(document).ready(function() {
    setTimeout(function() {
        $('.er-messages').css('height', '0rem')
    }, 2000);
    let filteredType = $('#filtered-type').html();
    console.log(filteredType);
    switch (filteredType) {
        case 'TEXT':

            commentActive();
            break;
        case 'AUDIO':

            audioActive();
            break;
        case 'IMAGE':

            imageActive();
            break;
        case 'LINK':

            linkActive();
            break;
    }


});