$('#div_id_type').after('<i class="fa-solid fa-hand-spock" id="fart-delete-button"></i>');
$('#id_type_3').after('<i class="fa-solid fa-link" id="link-icon"></i>');
$('#id_type_2').after('<i class="fa-solid fa-camera" id="image-icon"></i>');
$('#id_type_1').after('<i class="fa-solid fa-ear-listen" id="audio-icon"></i>');
$('#id_type_0').after('<i class="fa-solid fa-comment" id="comment-icon"></i>');



$('#add-fart-button').click(function() {
    $('#add-fart').submit();
});
$('#add-fart-type').click(function() {
    $('#add-fart').submit();
});



function commentActive() {
    $('input[name="type"]').val(["TEXT"]);
    $('.custom-radio label').removeClass('type-active');
    $('#add-fart-type').html('TEXT FART');

    $('#div_id_text').css('display', 'block');
    $('#div_id_audio').css('display', 'none');
    $('#div_id_image').css('display', 'none');
    $('#div_id_link').css('display', 'none');
    $('.custom-radio i').removeClass('type-icon-active');
    $('#comment-icon').addClass('type-icon-active');
}

function audioActive() {
    $('input[name="type"]').val(["AUDIO"]);
    $('.custom-radio label').removeClass('type-active');

    $('#add-fart-type').html('AUDIO FART');
    $('#div_id_text').css('display', 'none');
    $('#div_id_audio').css('display', 'block');
    $('#div_id_image').css('display', 'none');
    $('#div_id_link').css('display', 'none');
    $('.custom-radio i').removeClass('type-icon-active');
    $('#audio-icon').addClass('type-icon-active');
}

function imageActive() {
    $('input[name="type"]').val(["IMAGE"]);
    $('.custom-radio label').removeClass('type-active');

    $('#add-fart-type').html('IMAGE FART');
    $('#div_id_text').css('display', 'none');
    $('#div_id_audio').css('display', 'none');
    $('#div_id_image').css('display', 'block');
    $('#id_type_1').prop("checked", true);
    $('#div_id_link').css('display', 'none');
    $('.custom-radio i').removeClass('type-icon-active');
    $('#image-icon').addClass('type-icon-active');
}

function linkActive() {
    $('input[name="type"]').val(["LINK"]);
    $('.custom-radio label').removeClass('type-active');

    $('#add-fart-type').html('LINK FART');
    $('#div_id_text').css('display', 'none');
    $('#div_id_audio').css('display', 'none');
    $('#div_id_image').css('display', 'none');
    $('#div_id_link').css('display', 'block');
    $('.custom-radio i').removeClass('type-icon-active');
    $('#link-icon').addClass('type-icon-active');
}


$('#comment-icon').click(function() {
    commentActive();

})
$('#audio-icon').click(function() {
    audioActive();

})
$('#image-icon').click(function() {
    imageActive();

})
$('#link-icon').click(function() {
    linkActive();

})
$('#div_id_category').click(function() {
    let catOffset = $('#div_id_category').offset();
    let docHeight = $(window).height();
    console.log(docHeight);
    console.log(catOffset)
    $('.select2-results').css('height', ((docHeight - 104) - catOffset.top) + 'px')
    $('.select2-results__options').css('height', ((docHeight - 120) - catOffset.top) + 'px')
});

$('#div_id_topic').click(function() {
    let catOffset = $('#div_id_topic').offset();
    let docHeight = $(window).height();
    console.log(docHeight);
    console.log(catOffset)
    $('.select2-results').css('height', ((docHeight - 104) - catOffset.top) + 'px')
    $('.select2-results__options').css('height', ((docHeight - 120) - catOffset.top) + 'px')
});

$('#div_id_project').click(function() {
    let catOffset = $('#div_id_project').offset();
    let docHeight = $(window).height();
    console.log(docHeight);
    console.log(catOffset)
    $('.select2-results').css('height', ((docHeight - 104) - catOffset.top) + 'px')
    $('.select2-results__options').css('height', ((docHeight - 120) - catOffset.top) + 'px')
});

$(document).ready(function() {
    setTimeout(function() {
        $('.er-messages').css('height', '0rem')
    }, 2000);
    let currentType = $('#current-fart-type').html();
    console.log(currentType);
    switch (currentType) {
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
        case 'NEW':
            commentActive();
            break;
    }


});