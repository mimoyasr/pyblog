$.ajax({
            url: 'http://127.0.0.1:8000/allCats',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                cats = $("#cats");
                cats.html("");
                cats.append(cat_all())
                $(data).each(function(){
                    cats.append(category(this));
                });
            }
        });

$.ajax({
            url: 'http://127.0.0.1:8000/allPosts',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                console.log(data)
                posts = $('#posts');
                posts.html("");
                $(data).each(function(){
                    posts.append(post(this));
                });

            }
        });

    $(document).on('click', '.post-image', function(e) {
   post_id=parseInt($(this).attr('post-no'));
    $.ajax({
            url: 'http://127.0.0.1:8000/posts/'+post_id+'/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                console.log(data);
                modals = $('#modals_container');
                modals.html("");
                $(data).each(function(){
                    console.log(this);
                    modals.append(postModal(this));
                });
                $('#postModal').modal('toggle');

            }
        });


});

$(document).on('click', '.cat_trigger', function() {
       setActiveMenuItem('.cat_trigger',this);
       console.log($(this).attr("val"))
    });

function br() {
    return $("<br>")
}

function category(cat) {
    return $('<a href="http://127.0.0.1:8000/allCats/'+cat.fields.cat_name+'" class="cat_trigger list-group-item " val="'+cat.pk+'" >'+cat.fields.cat_name+'</a>')
}


function cat_all() {
    return $('<a href="#" class="cat_trigger list-group-item active" val="0">All</a>');
}


function post(data) {
    return $('  <div class="card mt-4">\n' +
        '            <img  post-no="'+data.pk+'" class="card-img-top img-fluid post-image" width="50" height="50" src="images/'+data.fields.picture+'" alt="">\n' +
        '            <div class="card-body">\n' +
        '              <h3 class="card-title">'+data.fields.title+'</h3>\n' +
        '              <p class="card-text">'+data.fields.content+'</p>\n' +
        '            </div>\n' +
        '        </div>')
}

function setActiveMenuItem(item, activeItem) {
    $(item).each(function() {
        if (this === activeItem) {
            if (!$(this).hasClass("acctive"))
                $(this).addClass("active");
        } else {
            $(this).removeClass("active");
        }
    });
}


// $('#productModal').modal('toggle');




function postModal(data) {
    ret =  $('<div class="modal fade" id="postModal" tabindex="-1" role="dialog" aria-labelledby="Cart" aria-hidden="true">\n' +
        '    <div class="modal-dialog modal-lg" role="document">\n' +
        '        <div class="modal-content">\n' +
        '            <div class="modal-header">\n' +
        '                <h5 class="modal-title" id="exampleModalLabel">'+data.fields.title+'</h5>\n' +
        '                <button type="button" class="close" data-dismiss="modal" aria-label="Close">\n' +
        '                    <span aria-hidden="true">&times;</span>\n' +
        '                </button>\n' +
        '            </div>\n' +
        '            <div class="modal-body" id="productContiner">\n' +
        '\n' +
        '            </div>\n' +
        '        </div>\n' +
        '    </div>\n' +
        '</div>')
        ret.find("#productContiner").append(post(data))
        return ret;
}
