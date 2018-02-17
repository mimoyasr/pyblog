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
   post_id=$(this).attr('post-no');
    $.ajax({
            url: 'http://127.0.0.1:8000/posts/'+post_id+'/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                modals = $('#modals_container');
                modals.html("");
                $(data).each(function(){
                    modals.append(postModal(this));
                    getComments(this.pk);
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
    console.log(cat);
    return $('<a href="http://127.0.0.1:8000/allCats/'+cat.fields.cat_name+'" class="cat_trigger list-group-item " val="'+cat.pk+'" >'+cat.fields.cat_name+'</a>')
}


function cat_all() {
    return $('<a href="#" class="cat_trigger list-group-item active" val="0">All </a>');
}


function post(data) {
    categorySpan=$('<span></span>');
    getCategory(data.fields.category,printCategoryname,categorySpan)
    post_div=$('  <div class="card mt-4">\n' +
        '            <img  post-no="'+data.pk+'" class="card-img-top img-fluid post-image" width="50px" height="50px" src="./images/'+data.fields.picture+'" alt="">\n' +
        '            <div class="card-body">\n' +
        '              <h3 class="card-title">'+data.fields.title+'</h3>\n' +
        '              <p class="card-text">'+data.fields.content+'</p>\n' +
        '              <p class="card-text">Category: <span class="postCat"></span></p>\n' +
        '              <a href="#" class="btn btn-success">Leave a Comment</a>\n' +
        '            </div>\n' +
        '        </div>');
    post_div.find('.postCat').append(categorySpan);
    return post_div;
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
function comments(data){
    usernameSpan = $("<span></span>");
    getUser(data.fields.user,printusername,usernameSpan);
    ret =  $( '<div class="card-body">\n' +
        '              <p>'+data.fields.text+'</p>\n' +
        '              <small class="text-muted">Posted by <span class="username"></span> on '+data.fields.created_date+'</small>\n' +
        '              <hr>\n' +
        '            </div>');
    ret.find(".username").append(usernameSpan);
    return ret;
}

function getComments(post_id){
    $.ajax({
            url: 'http://127.0.0.1:8000/comments/'+post_id+'/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                console.log(data);
                $(data).each(function(){
                    $('#comments').append(comments(this));
                });

            }
        });
}

function getUser(user_id,handle,element){

        $.ajax({
            url: 'http://127.0.0.1:8000/user/'+user_id+'/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response)[0];
                console.log(data);
                handle(data,element);
            }
        });
}

function getCategory(cat_id,handle,element){
            $.ajax({
            url: 'http://127.0.0.1:8000/category/'+cat_id+'/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response)[0];
                console.log(data);
                handle(data,element);
            }
        });
}


function printusername(userObject,element) {
     $(element).append(data.fields.username);
}

function printCategoryname(catObject,element) {
      $(element).append(data.fields.cat_name)
}

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
        '            <div class="modal-body" id="postContiner">\n' +
        '            </div>\n' +
        '            <div><div class="card-header">' +
        '              Post Comments </div>'+
        '               <div  id="comments"></div>'+
        '             </div>'+
        '        </div>\n' +
        '    </div>\n' +
        '</div>');
        ret.find("#postContiner").append(post(data));
        return ret;
}
