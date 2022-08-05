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


// $('.likin').click(function () {
//     const post_id = $(this).attr('id')
//     console.log(post_id)
//     $.ajax({
//         type: 'POST',
//         url: "{% url 'like' %}",
//         data: {
//             'content_id': $(this).attr('name'),
//             'operation': 'like_submit',
//             'csrfmiddlewaretoken': '{{ csrf_token }}'
//         },
//         dataType: "json",
//         success: function (response) {
//             selector = document.getElementsByName(response.content_id);
//             // data: {
//             //     'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
//             //     'post_id': post_id,
//             // },
//             // success: function (response) {
//             if (response.liked == true) {
//                 $().css("color", "blue");
//             } else if (response.liked == false) {
//                 $(selector).css("color", "black");
//             }
//         }
//         ,
//         error: function (response) {
//
//         }
//     })
// })