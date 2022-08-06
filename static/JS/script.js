function liked(blogId) {
    let csrf = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: "POST",
        url: "/like/",
        data: {
            'blogId': blogId,
            'csrfmiddlewaretoken': csrf
        },
        dataType: "json",
        success: function (response) {
            $('#like-count-' + blogId).html(response.like_count + " likes")
            if (response.liked) {
                $('#like-btn-' + blogId).html("<i class=\"fa fa-thumbs-up\"></i> Like")
            } else {
                $('#like-btn-' + blogId).html("<i class=\"fa fa-thumbs-down\"></i> Unlike")
            }
        }
    })
}

function deleteConfirm(){
    return confirm('Are you sure you want to delete this?');
}